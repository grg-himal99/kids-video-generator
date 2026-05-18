import os

import numpy as np
from moviepy.audio.fx.all import audio_loop
from moviepy.editor import (
    AudioFileClip,
    ColorClip,
    CompositeAudioClip,
    CompositeVideoClip,
    ImageClip,
    concatenate_videoclips,
)
from PIL import Image, ImageDraw, ImageFont

VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720
FPS = 24
FONT_SIZE = 52
CAPTION_Y_OFFSET = 90  # pixels from bottom


def _load_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/Windows/Fonts/arialbd.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def _render_caption(image_path: str, caption: str) -> np.ndarray:
    img = Image.open(image_path).convert("RGB").resize((VIDEO_WIDTH, VIDEO_HEIGHT), Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    font = _load_font(FONT_SIZE)

    # Measure text
    bbox = draw.textbbox((0, 0), caption, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (VIDEO_WIDTH - text_w) // 2
    y = VIDEO_HEIGHT - CAPTION_Y_OFFSET - text_h

    # Draw semi-transparent background bar
    bar_pad = 16
    bar_x0 = x - bar_pad
    bar_y0 = y - bar_pad
    bar_x1 = x + text_w + bar_pad
    bar_y1 = y + text_h + bar_pad
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    bar_draw = ImageDraw.Draw(overlay)
    bar_draw.rectangle([bar_x0, bar_y0, bar_x1, bar_y1], fill=(0, 0, 0, 140))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Outline
    for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
        draw.text((x + dx, y + dy), caption, font=font, fill=(0, 0, 0))
    draw.text((x, y), caption, font=font, fill=(255, 255, 255))

    return np.array(img)


def _render_title_frame(title: str) -> np.ndarray:
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), color=(255, 200, 60))
    draw = ImageDraw.Draw(img)
    font_large = _load_font(80)
    font_sub = _load_font(38)

    # Title
    bbox = draw.textbbox((0, 0), title, font=font_large)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (VIDEO_WIDTH - tw) // 2
    y = (VIDEO_HEIGHT - th) // 2 - 40
    for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3)]:
        draw.text((x + dx, y + dy), title, font=font_large, fill=(180, 100, 0))
    draw.text((x, y), title, font=font_large, fill=(255, 255, 255))

    # Subtitle
    sub = "A Story for Kids"
    bbox2 = draw.textbbox((0, 0), sub, font=font_sub)
    sx = (VIDEO_WIDTH - (bbox2[2] - bbox2[0])) // 2
    sy = y + th + 20
    draw.text((sx, sy), sub, font=font_sub, fill=(100, 60, 0))

    return np.array(img)


def create_scene_clip(image_path: str, narration_path: str, caption: str) -> CompositeVideoClip:
    narration = AudioFileClip(narration_path)
    duration = narration.duration + 1.2  # padding after narration ends

    frame = _render_caption(image_path, caption)
    clip = (
        ImageClip(frame)
        .set_duration(duration)
        .fadein(0.4)
        .fadeout(0.4)
        .set_audio(narration.set_start(0.4))
    )
    return clip


def create_title_clip(title: str, duration: float = 3.5) -> ImageClip:
    frame = _render_title_frame(title)
    return ImageClip(frame).set_duration(duration).fadein(0.5).fadeout(0.5)


def assemble_video(story: dict, assets_dir: str, output_path: str) -> str:
    clips = [create_title_clip(story["title"])]

    for scene in story["scenes"]:
        n = scene["scene_number"]
        image_path = os.path.join(assets_dir, f"scene_{n:02d}.png")
        narration_path = os.path.join(assets_dir, f"narration_{n:02d}.mp3")
        print(f"  Compositing scene {n}/{len(story['scenes'])}...")
        clips.append(create_scene_clip(image_path, narration_path, scene["title_text"]))

    final = concatenate_videoclips(clips, method="compose")

    # Mix in background music at low volume
    bg_path = os.path.join(assets_dir, "background_music.wav")
    if os.path.exists(bg_path):
        bg = audio_loop(AudioFileClip(bg_path), duration=final.duration).volumex(0.20)
        if final.audio:
            final = final.set_audio(CompositeAudioClip([final.audio, bg]))
        else:
            final = final.set_audio(bg)

    print(f"\nRendering {output_path} ...")
    final.write_videofile(
        output_path,
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile=os.path.join(assets_dir, "tmp_audio.m4a"),
        remove_temp=True,
        verbose=False,
        logger=None,
    )
    return output_path
