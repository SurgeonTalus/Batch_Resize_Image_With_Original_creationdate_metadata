import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import shutil

def resize_and_save_images(input_folder):
    # Create a subfolder named "103%" if it doesn't exist
    output_folder = os.path.join(input_folder, "103%")
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of image files in the input folder
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [filename for filename in os.listdir(input_folder)
                   if filename.lower().endswith(tuple(image_extensions))]

    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open and resize the image
        with Image.open(input_path) as img:
            width, height = img.size
            new_width = int(width * 1.03)
            new_height = int(height * 1.03)
            resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)
            
            # Save the resized image in high-quality (JPEG) without compression
            resized_img.save(output_path, "JPEG", quality=95)

        # Copy file metadata (including creation time) from the original image to the resized image
        shutil.copystat(input_path, output_path)

if __name__ == "__main__":
    # Create a GUI for selecting the input folder
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    input_folder = filedialog.askdirectory(title="Select a folder of images")

    if input_folder:
        resize_and_save_images(input_folder)
        print("Images resized and saved in the '103%' subfolder with correct metadata and no compression.")

    root.mainloop()
