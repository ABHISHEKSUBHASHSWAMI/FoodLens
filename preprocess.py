from PIL import Image, ImageFilter
import os

def resize_and_sharpen_images(directory, width, height):
    count=0
    for root, dirs, files in os.walk(directory):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                
                count+=1
                # Check if the file is an image (you can extend this list as needed)
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    try:
                        img = Image.open(file_path)
                        
                        # Apply sharpening filter
                        #img = img.filter(ImageFilter.SHARPEN)
                        
                        # Resize the sharpened image
                        img_resized = img.resize((width, height))
                        
                        # Save the resized image, overwriting the original image
                        img_resized.save(file_path)
                        print(count)
                    except Exception as e:
                        print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    directory = "dataset/test"  # Replace with your directory path
    target_width = 256
    target_height = 256
    resize_and_sharpen_images(directory, target_width, target_height)
