import easyocr

reader = easyocr.Reader(['en'])

def read_plate(image):

    results = reader.readtext(image)

    plates = []

    for res in results:
        text = res[1]
        plates.append(text)

    return plates