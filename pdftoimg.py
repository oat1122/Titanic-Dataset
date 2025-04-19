from pdf2image import convert_from_path
import os

# Path to PDF file
pdf_path = "dasss/titanic.pdf"

# Convert PDF to list of images (one per page)
images = convert_from_path(pdf_path)

# Save images and prepare for display
image_paths = []
output_dir = "./dasss"
os.makedirs(output_dir, exist_ok=True)

for i, img in enumerate(images):
    output_path = os.path.join(output_dir, f"page_{i+1}.png")
    img.save(output_path, 'PNG')
    image_paths.append(output_path)

image_paths
