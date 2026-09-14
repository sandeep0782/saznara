import os

from PIL import Image, ImageOps

root_path = r"/Users/krishna/Desktop/Images/Kaveri"

image_exts = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".heic",
    ".heif",
}

for folder_path, _, files in os.walk(root_path):
    if os.path.abspath(folder_path) == os.path.abspath(root_path):
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

        # Don't overwrite existing files
        if os.path.exists(new_path):
            print(f"Skipping: {new_name} already exists")
            count += 1
            continue

        try:
            # ------------------------------------------------
            # OPEN ORIGINAL
            # ------------------------------------------------
            with Image.open(old_path) as img:
                # Correct orientation using EXIF
                img = ImageOps.exif_transpose(img)

                # ------------------------------------------------
                # CONVERT TO RGB
                # ------------------------------------------------
                if img.mode in ("RGBA", "LA"):
                    # Transparent areas become pure white
                    background = Image.new("RGB", img.size, (255, 255, 255))

                    background.paste(img, mask=img.getchannel("A"))

                    img = background

                elif img.mode == "P":
                    # Handle palette images
                    if "transparency" in img.info:
                        img = img.convert("RGBA")

                        background = Image.new("RGB", img.size, (255, 255, 255))

                        background.paste(img, mask=img.getchannel("A"))

                        img = background

                    else:
                        img = img.convert("RGB")

                else:
                    img = img.convert("RGB")

                # ------------------------------------------------
                # SAVE AS REAL JPEG
                # ------------------------------------------------
                img.save(
                    new_path,
                    format="JPEG",
                    quality=95,
                    optimize=True,
                    progressive=False,
                    subsampling=0,
                )

            # ------------------------------------------------
            # VERIFY OUTPUT
            # ------------------------------------------------
            with Image.open(new_path) as check:
                is_valid = check.format == "JPEG" and check.mode == "RGB"

                print(
                    f"Verified: {new_name} | "
                    f"Format: {check.format} | "
                    f"Mode: {check.mode} | "
                    f"Size: {check.size}"
                )

            # ------------------------------------------------
            # DELETE ORIGINAL ONLY AFTER SUCCESSFUL VERIFICATION
            # ------------------------------------------------
            if is_valid:
                if os.path.abspath(old_path) != os.path.abspath(new_path):
                    os.remove(old_path)

                print(f"Converted: {file_name} -> {new_name}")

            else:
                print(f"ERROR: {new_name} is not a valid JPEG. Original kept.")

                if os.path.exists(new_path):
                    os.remove(new_path)

        except Exception as e:
            print(f"Failed: {file_name} | {e}")

        count += 1

print("Done!")
