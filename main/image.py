import os
from PIL import Image

# ==========================
# Configuration
# ==========================
INPUT_FOLDER = r"/Users/sandeep/Desktop/untitled folder 4"
OUTPUT_FOLDER = r"/Users/sandeep/Desktop/untitled folder 5"

WIDTH = 1080
HEIGHT = 1440

MAX_SIZE = 2 * 1024 * 1024  # 2 MB

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


for filename in os.listdir(INPUT_FOLDER):

    if not filename.lower().endswith(SUPPORTED_EXTENSIONS):
        continue

    input_path = os.path.join(INPUT_FOLDER, filename)

    name = os.path.splitext(filename)[0]
    output_path = os.path.join(OUTPUT_FOLDER, f"{name}.jpg")

    try:
        img = Image.open(input_path)

        if img.mode != "RGB":
            img = img.convert("RGB")

        # High quality resize
        img = img.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

        quality = 100

        while quality >= 70:

            img.save(
                output_path,
                "JPEG",
                quality=quality,
                optimize=True,
                progressive=True
            )

            if os.path.getsize(output_path) <= MAX_SIZE:
                break

            quality -= 2

        print(f"✔ {filename} -> Quality={quality}, Size={os.path.getsize(output_path)/1024:.1f} KB")

    except Exception as e:
        print(f"✘ Error processing {filename}: {e}")

print("\nFinished processing all images.")