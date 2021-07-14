import pdfrw

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

def fill_pdf(pdf_input, path_to_source_pdf, path_to_dest_pdf):
    pdf = pdfrw.PdfReader(path_to_source_pdf)
    for page in pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                
                    # print(key)
                    ### Output: 
                    ### NIRC/FIN
                    ### Email Address1
                    ### Email Address2
                    ### Country Code1
                    ### Country Code2
                    ### Mobile1
                    ### Mobile2
                    ### Accomodation
                    ### Arrival Date
                    ### HD2
                    ### Barcode

                    if key in pdf_input.keys():
                        annotation.update(pdfrw.PdfDict(AP='', V=pdf_input[key]))
    pdfrw.PdfWriter().write(path_to_dest_pdf, pdf)              

def main():
    # Create pdf_input
    pdf_input = {
        'NIRC/FIN': 'S1234567A',
        'Email Address1': 'foo@bar.com',
        'Email Address2': 'foo@bar.com',
        'Country Code1': '65',
        'Country Code2': '65',
        'Mobile1': '12345678',
        'Mobile2': '12345678',
        'Accomodation': 'Hotel',
        'Arrival Date': '14/7/2021',
        'HD2': 'NA'
    }

    # Initialise paths to pdfs
    path_to_source_pdf = "sample pdf form.pdf"
    path_to_dest_pdf = "filled_pdf_form.pdf"

    # Fill pdf
    fill_pdf(pdf_input, path_to_source_pdf, path_to_dest_pdf)

if __name__ == '__main__':
    main()