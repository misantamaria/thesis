from pdf2image import convert_from_path
import img2pdf
import os

# Convertir PDF a imágenes
images = convert_from_path("./S3-zeroshot_2.pdf", dpi=300)

# Guardar imágenes temporalmente
image_paths = []
for i, image in enumerate(images):
    path = f"temp_page_{i}.png"
    image.save(path, "PNG")
    image_paths.append(path)

# Convertir imágenes de vuelta a PDF con el tamaño deseado
with open("S3-zeroshot_2_resized.pdf", "wb") as f:
    f.write(img2pdf.convert(image_paths, with_pdfrw=True))

# Eliminar archivos temporales
for path in image_paths:
    os.remove(path)