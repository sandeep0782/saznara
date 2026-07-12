import os

root_path = r'/Users/sandeep/Desktop/New Listing/DUCK'

# image extensions to target
image_exts = {".jpg", ".jpeg", ".png", ".webp", ".heic"}

for folder_path, _, files in os.walk(root_path):
    # skip root if it contains files (optional safety)
    if folder_path == root_path:
        continue

    folder_name = os.path.basename(folder_path)
    files = sorted(files)

    count = 1

    for file_name in files:
        old_path = os.path.join(folder_path, file_name)
        ext = os.path.splitext(file_name)[1].lower()

        # skip non-images
        if ext not in image_exts:
            continue

        new_name = f"{folder_name}-{count}{ext}"
        new_path = os.path.join(folder_path, new_name)

        # avoid overwriting if file already exists
        if os.path.exists(new_path):
            print(f"Skipping (exists): {new_path}")
            continue

        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")

        count += 1


