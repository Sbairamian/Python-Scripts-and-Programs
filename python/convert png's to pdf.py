import os
from PIL import Image

def convert_pngs_to_pdf(png_dir, output_pdf_path):
    # Get all PNG files from the directory
    png_files = [os.path.join(png_dir, f) for f in os.listdir(png_dir) if f.lower().endswith('.png')]
    png_files.sort() # Sort files to ensure order in the PDF

    if not png_files:
        print("No PNG images found in the directory.")
        return

    # Open all images and convert to RGB (necessary for saving as PDF)
    images = []
    for file_path in png_files:
        img = Image.open(file_path)
        if img.mode == 'RGBA':
            # Create a white background and paste the image to handle transparency
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3]) # 3 is the alpha channel
            images.append(background)
        else:
            images.append(img.convert('RGB'))

    # Save the first image, appending the rest
    if images:
        images[0].save(
            output_pdf_path,
            "PDF",
            save_all=True,
            append_images=images[1:],
            resolution=100.0
        )
        print(f"Successfully created PDF: {output_pdf_path}")
    else:
        print("Could not process images.")

# --- Usage Example ---
# Replace 'path/to/your/pngs' with the actual path to your PNG image folder
png_directory = r'C:\Users\SevBairamian\Desktop\CMMC Evidence\3.1.x - Access Controls\3.1.1\Blurred Devices'
# Define the output PDF name and location
output_pdf_file = r'C:\Users\SevBairamian\Desktop\CMMC Evidence\3.1.x - Access Controls\3.1.1\Blurred Devices\3.1.2 - Authorized Devices.pdf'

convert_pngs_to_pdf(png_directory, output_pdf_file)