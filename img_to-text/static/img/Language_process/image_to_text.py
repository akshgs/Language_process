
from pytesseract import pytesseract
from PIL import Image
tesseract_path = r"C:\Users\akash\AppData\Local\Tesseract-OCR\tesseract.exe"
path_img1 = "download.jpeg"
pytesseract.tesseract_cmd = tesseract_path
img1 = Image.open(path_img1)
text1 = pytesseract.image_to_string(img1)
print("Image 1 text:\n", text1)
