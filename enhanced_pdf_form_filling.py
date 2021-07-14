import pdfrw
from pdfrw.objects.pdfobject import PdfObject

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'             

def main():
    path_to_source_pdf = input('Please enter path to source PDF: ')
    pdf = pdfrw.PdfReader(path_to_source_pdf)
    for page in pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    update = input('Please enter input for this field - {}: '.format(key))
                    annotation.update(pdfrw.PdfDict(AP='', V=update))
    path_to_dest_pdf = input('Please enter path to destination PDF: ')
    pdfrw.PdfWriter().write(path_to_dest_pdf, pdf)    

if __name__ == '__main__':
    main()