import io
import os
import time
from urllib.parse import quote

import requests
from PIL import Image

# Pollinations.ai — completely free, no API key needed
POLLINATIONS_URL = "https://image.pollinations.ai/prompt/{prompt}?width={w}&height={h}&nologo=true&model=flux-realism"
VIDEO_WIDTH = 1280
VIDEO_HEIGHT = 720


def generate_scene_image(prompt: str, scene_number: int, output_dir: str) -> str:
    full_prompt = (
        "photorealistic, cinematic photography, sharp focus, professional DSLR, "
        f"no text, no watermark, {prompt}"
    )
    encoded = quote(full_prompt)
    url = POLLINATIONS_URL.format(prompt=encoded, w=VIDEO_WIDTH, h=VIDEO_HEIGHT)

    for attempt in range(4):
        print(f"  Generating image for scene {scene_number}... (attempt {attempt + 1})")
        try:
            response = requests.get(url, timeout=120)
        except requests.Timeout:
            print("  Request timed out, retrying...")
            time.sleep(15)
            continue

        if response.status_code == 200 and response.headers.get("content-type", "").startswith("image"):
            image = Image.open(io.BytesIO(response.content)).convert("RGB")
            image = image.resize((VIDEO_WIDTH, VIDEO_HEIGHT), Image.LANCZOS)
            path = os.path.join(output_dir, f"scene_{scene_number:02d}.png")
            image.save(path)
            print(f"  ✓ Scene {scene_number} image saved")
            return path
        elif response.status_code == 429:
            print("  Rate limited, waiting 30s...")
            time.sleep(30)
        else:
            print(f"  Error {response.status_code}, retrying...")
            time.sleep(10)

    raise RuntimeError(f"Failed to generate image for scene {scene_number} after 4 attempts")
