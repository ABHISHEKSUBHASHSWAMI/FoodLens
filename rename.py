import os

def rename_images_in_folders(directory):
    for root, dirs, files in os.walk(directory):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            folder_name = folder.replace('_', ' ').title()
            
            # Iterate through images in the folder
            for i, filename in enumerate(os.listdir(folder_path)):
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    new_filename = f"{folder_name}_{i+1}.jpg"  # Change extension if needed
                    old_filepath = os.path.join(folder_path, filename)
                    new_filepath = os.path.join(folder_path, new_filename)
                    os.rename(old_filepath, new_filepath)

if __name__ == "__main__":
    directory = "Indian Food Images"  # Replace with your directory path
    rename_images_in_folders(directory)
