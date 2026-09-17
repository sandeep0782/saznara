from PIL import Image, ImageOps
import os

root_path = r"/Users/krishna/Downloads/Sudha-002"

image_exts = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}

for folder_path, _, files in os.walk(root_path):

    if os.path.abspath(folder_path) == os.path.abspath(root_path):
        continue

    folder_name = os.path.basename(folder_path)

    image_files = sorted(
        f for f in files
        if os.path.splitext(f)[1].lower() in image_exts
    )

    for count, file_name in enumerate(image_files, 1):

        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(
            folder_path,
            f"{folder_name}-{count}.jpg"
        )

        try:
            with Image.open(old_path) as img:

                # Correct EXIF rotation
                img = ImageOps.exif_transpose(img)

                # Fully decode
                img.load()

                # JPEG = RGB
                if img.mode != "RGB":
                    if "A" in img.getbands():
                        bg = Image.new("RGB", img.size, "white")
                        rgba = img.convert("RGBA")
                        bg.paste(rgba, mask=rgba.getchannel("A"))
                        img = bg
                    else:
                        img = img.convert("RGB")

                # Create a completely new JPEG
                img.save(
                    new_path,
                    format="JPEG",
                    quality=90,
                    optimize=False,
                    progressive=False
                )

            # Verify the generated file
            with Image.open(new_path) as check:
                check.load()

                if check.format != "JPEG":
                    raise ValueError(
                        f"Generated file is {check.format}, not JPEG"
                    )

                if check.mode != "RGB":
                    raise ValueError(
                        f"Generated file is {check.mode}, not RGB"
                    )

            print(f"OK: {file_name} -> {os.path.basename(new_path)}")

            # Only remove source after successful verification
            if os.path.abspath(old_path) != os.path.abspath(new_path):
                os.remove(old_path)

        except Exception as e:
            print(f"FAILED: {file_name} | {e}")

print("Done!")
