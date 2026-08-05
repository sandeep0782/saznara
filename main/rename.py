import os

from PIL import Image, ImageOps

root_path = r'/Users/krishna/Desktop/Botanical/'

image_exts = {".jpg", ".jpeg", ".png", ".webp", ".heic"}

for folder_path, _, files in os.walk(root_path):
    if folder_path == root_path:
        continue

    folder_name = os.path.basename(folder_path)

    image_files = sorted(
        [f for f in files if os.path.splitext(f)[1].lower() in image_exts]
    )

    count = 1

    for file_name in image_files:
        old_path = os.path.join(folder_path, file_name)
        new_name = f"{folder_name}-{count}.jpg"
        new_path = os.path.join(folder_path, new_name)

        if os.path.exists(new_path):
            print(f"Skipping: {new_name} already exists")
            count += 1
            continue

        try:
            with Image.open(old_path) as img:
                # Auto-rotate using EXIF metadata
                img = ImageOps.exif_transpose(img)

                # JPEG doesn't support transparency
                if img.mode in ("RGBA", "LA"):
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.getchannel("A"))
                    img = background
                elif img.mode == "P":
                    img = img.convert("RGBA")
                    background = Image.new("RGB", img.size, (255, 255, 255))
                    background.paste(img, mask=img.getchannel("A"))
                    img = background
                else:
                    img = img.convert("RGB")

                img.save(
                    new_path,
                    format="JPEG",
                    quality=95,
                    optimize=True,
                    progressive=True,
                    subsampling=0,
                )

            if os.path.abspath(old_path) != os.path.abspath(new_path):
                os.remove(old_path)

            print(f"Converted: {file_name} -> {new_name}")

        except Exception as e:
            print(f"Failed: {file_name} | {e}")

        count += 1

print("Done!")
