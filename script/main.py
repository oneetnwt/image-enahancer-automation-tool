from PIL import Image, ImageEnhance, ImageFilter
import os

# Get the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the images and the output directory
path = os.path.join(script_dir, '../imgs')
pathOut = os.path.join(script_dir, '../editedImgs')

#Ensure the output directory exists
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Process each image in the input directory
for filename in os.listdir(path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):  # Process only image files
        img = Image.open(os.path.join(path, filename))

        edit = img.filter(ImageFilter.SHARPEN)

        factor = 1
        enhancer = ImageEnhance.Brightness(edit)
        edit = enhancer.enhance(factor)

        clean_name = os.path.splitext(filename)[0]
        edit.save(os.path.join(pathOut, f'{clean_name}_edited.jpg'))