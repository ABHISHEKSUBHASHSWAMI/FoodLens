import os
import shutil

def copy_images_to_test_folder(source_folder, test_folder, num_images=10):
    # Get a list of subfolders in the source folder
    subfolders = [f.path for f in os.scandir(source_folder) if f.is_dir()]

    for subfolder in subfolders:
        # Get the class name (the last part of the subfolder path)
        class_name = os.path.basename(subfolder)
        # Create a subdirectory for the class in the test folder
        class_test_folder = os.path.join(test_folder, class_name)
        os.makedirs(class_test_folder, exist_ok=True)

        images = [f for f in os.listdir(subfolder) if os.path.isfile(os.path.join(subfolder, f))]
        selected_images = images[:num_images]  # Select the first 'num_images' images

        for image in selected_images:
            source_image_path = os.path.join(subfolder, image)
            destination_image_path = os.path.join(class_test_folder, image)

            # Copy the image to the test folder for the respective class
            shutil.copy(source_image_path, destination_image_path)
            print(f"Copied {image} to {destination_image_path}")

# Example usage:
source_folder = 'dataset/train/' 
test_folder = 'dataset/test/'    

# Create the test folder if it doesn't exist
if not os.path.exists(test_folder):
    os.makedirs(test_folder)

# Copy 10 images from each subfolder to the test folder
copy_images_to_test_folder(source_folder, test_folder, num_images=12)
