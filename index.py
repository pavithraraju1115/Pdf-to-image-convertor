
#pip install PyMuPDF
import fitz
import os

pdffile = "somatosensory.pdf"
output_folder = "output"  # Specify the desired output folder

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

doc = fitz.open(pdffile)
zoom = 4
mat = fitz.Matrix(zoom, zoom)
count = len(doc)

for i in range(count):
    val = os.path.join(output_folder, f"image_{i+1}.png")
    page = doc[i]
    pix = page.get_pixmap(matrix=mat)
    pix.save(val)

doc.close()