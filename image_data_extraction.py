import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extract_data(path_to_img):
    # Retrieve text data from image
    img = cv2.imread(path_to_img)
    text = pytesseract.image_to_string(img)

    # Split text data by new line and process data
    text = text.title().splitlines()
    for index, item in enumerate(text):
        # Extract card number
        if "Identity" in item:
            card_number_list = [str(i) for i in item.split() if i.isdigit()]
            card_number = ''.join(card_number_list)

        # Extract name
        if "Name" in item:
            i = index
            name = ''
            while len(name) == 0:
                i += 1
                name = str(text[i])

        # Extract gender
        if "Sex" in item:
            gender = str(text[index+1].split()[-1])
        
        # Extract DOB
        if "Date Of Birth" in item:
            date_of_birth = str(text[index+1].split()[-2])

        # Extract country
        if "Country" in item:
            country_of_birth = str(text[index+1])
    
    extracted_data = [card_number, name, gender, date_of_birth, country_of_birth]

    return extracted_data

def main():
    path_to_img = 'paw_ic1.png'
    # path_to_img = 'paw_ic2.jpg'
    data_required = ['card_number', 'name', 'gender', 'date_of_birth', 'country_of_birth']
    extracted_data = extract_data(path_to_img)
    extracted_data = dict(zip(data_required, extracted_data))
    print (extracted_data)
    
if __name__ == '__main__':
    main()