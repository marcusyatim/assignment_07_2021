# Programming Test Round
This repository is to present my solutions to the Assignment_07_2021 as part of the programming test requirement for prospective Python programmer.

## PDF Form Filling
Refer to `pdf_form_filling.py` for code that directly answers the question and `filled_pdf_form.pdf` for the result.

Additionally, I have taken the liberty to include an `enhance_pdf_form_filling.py` that basically produces the same end result. However, it includes terminal input for the user. This way, we can use the script to work for most types of PDF forms, not only the sample one given. 

Requirements: `pip install pdfrw`

To run: `python enhance_pdf_form_filling.py`

## Image Data Extraction
Run `image_data_extraction.py` to print solution to the question. 

Requirements:
1) For Windows user, download and install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki. Ensure download path is `C:\Program Files\Tesseract-OCR\tesseract.exe`. Else, have to manually edit Tesseract path in the code. For Mac and Linux users, no need to download and also, remove Tesseract path from code.
2) `pip install pytesseract`
3) `pip install opencv-python`

To run: `python image_data_extraction.py`
