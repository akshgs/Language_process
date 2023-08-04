from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd
from keras.models import load_model 
from PIL import Image, ImageOps  
app=Flask(__name__)
@app.route('/')
def text():
    return render_template('text.html')
@app.route('/images',methods=['post'])
def images():
    name=(request.values['name'])
    path="static/img/"+name
    print(path)
    from pytesseract import pytesseract
    from PIL import Image
    tesseract_path = r"C:\Users\akash\AppData\Local\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = tesseract_path
    img1 = Image.open(path)
    text1 = pytesseract.image_to_string(img1)
    print("Image 1 text:\n", text1)
    return render_template('text.html',pre=text1)
if __name__ =='__main__':
    app.run(port=8000)
