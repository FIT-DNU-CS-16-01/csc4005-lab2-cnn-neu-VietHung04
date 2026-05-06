import os
import shutil

CLASS_NAMES = {
    "0": "Crazing",
    "1": "Inclusion",
    "2": "Patches",
    "3": "Pitted_Surface",
    "4": "Rolled-in_Scale",
    "5": "Scratches"
}

SOURCE_DIR = "dataset"
TARGET_DIR = "classification_dataset"

for split in ["train", "valid"]:

    image_dir = os.path.join(SOURCE_DIR, split, "images")
    label_dir = os.path.join(SOURCE_DIR, split, "labels")

    for label_file in os.listdir(label_dir):

        if not label_file.endswith(".txt"):
            continue

        label_path = os.path.join(label_dir, label_file)

        with open(label_path, "r") as f:
            line = f.readline().strip()

        class_id = line.split()[0]

        class_name = CLASS_NAMES[class_id]

        class_folder = os.path.join(
            TARGET_DIR,
            class_name
        )

        os.makedirs(class_folder, exist_ok=True)

        image_name = label_file.replace(".txt", ".jpg")

        src_image = os.path.join(image_dir, image_name)

        dst_image = os.path.join(class_folder, image_name)

        if os.path.exists(src_image):
            shutil.copy(src_image, dst_image)

print("DONE!")