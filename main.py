#!/usr/bin/env python3
"""
Kids Animated Video Generator
------------------------------
Usage:
    python main.py                        # random topic
    python main.py --topic "space"        # specific topic
    python main.py --topic "animals" --output my_video.mp4
    python main.py --list-topics          # show available topics
"""

import argparse
import json
import os
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def check_env():
    pass  # No API keys required — Pollinations.ai and built-in templates are both free


def main():
    parser = argparse.ArgumentParser(description="Generate animated kids videos")
    parser.add_argument("--topic", type=str, help="Video topic (default: random)")
    parser.add_argument("--output", type=str, help="Output .mp4 path (default: auto-named)")
    parser.add_argument("--list-topics", action="store_true", help="List available topics")
    parser.add_argument(
        "--keep-assets",
        action="store_true",
        help="Keep generated images and audio files",
    )
    args = parser.parse_args()

    # Deferred imports so missing-dep errors are clear
    from story_generator import TOPICS, generate_story, get_random_topic
    from image_generator import generate_scene_image
    from audio_generator import generate_background_music, generate_narration
    from video_assembler import assemble_video

    if args.list_topics:
        print("Available topics:")
        for t in TOPICS:
            print(f"  - {t}")
        return

    check_env()

    topic = args.topic or get_random_topic()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = args.output or f"kids_video_{timestamp}.mp4"

    print(f"\n{'='*50}")
    print(f"  Kids Video Generator")
    print(f"{'='*50}")
    print(f"  Topic  : {topic}")
    print(f"  Output : {output_path}")
    print(f"{'='*50}\n")

    # Use a temp directory for intermediate assets
    assets_dir = tempfile.mkdtemp(prefix="kidsvidgen_")
    story_path = os.path.join(assets_dir, "story.json")

    try:
        # 1. Generate story
        print("Step 1/4: Writing story...")
        story = generate_story(topic)
        with open(story_path, "w") as f:
            json.dump(story, f, indent=2)
        print(f"  Title: \"{story['title']}\"")
        print(f"  Scenes: {len(story['scenes'])}\n")

        # 2. Generate scene images
        print("Step 2/4: Generating scene images (HuggingFace Stable Diffusion)...")
        print("  (This may take 2-5 minutes — each image takes ~30-60 seconds)\n")
        for scene in story["scenes"]:
            generate_scene_image(scene["image_prompt"], scene["scene_number"], assets_dir)
            time.sleep(2)  # be kind to the free API

        # 3. Generate narration audio
        print("\nStep 3/4: Generating narration audio...")
        for scene in story["scenes"]:
            path = generate_narration(scene["narration"], scene["scene_number"], assets_dir)
            print(f"  ✓ Narration {scene['scene_number']} saved")

        # 4. Generate background music
        print("\n  Generating background music...")
        bg_path = os.path.join(assets_dir, "background_music.wav")
        generate_background_music(duration_seconds=120.0, output_path=bg_path)
        print("  ✓ Background music ready")

        # 5. Assemble video
        print("\nStep 4/4: Assembling final video...")
        assemble_video(story, assets_dir, output_path)

        size_mb = Path(output_path).stat().st_size / (1024 * 1024)
        print(f"\n{'='*50}")
        print(f"  Done! Video saved to: {output_path}")
        print(f"  File size: {size_mb:.1f} MB")
        print(f"{'='*50}\n")

        if args.keep_assets:
            print(f"  Assets kept at: {assets_dir}")
        else:
            import shutil
            shutil.rmtree(assets_dir, ignore_errors=True)

    except KeyboardInterrupt:
        print("\n\nCancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError: {e}")
        print(f"Assets preserved at: {assets_dir}")
        raise


if __name__ == "__main__":
    main()
