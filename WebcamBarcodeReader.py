import cv2
import pyzbar.pyzbar as pb

font_duplex = cv2.FONT_HERSHEY_DUPLEX
font_simple = cv2.FONT_HERSHEY_PLAIN


# Add text shadow to the cv2 text function
def setText(_img, _string, _pos, _font, _scale, _color, _thickness):
    txt_shadow = cv2.putText(_img, _string, _pos, _font, _scale, (0, 0, 0), _thickness + 1)
    txt = cv2.putText(_img, _string, _pos, _font, _scale, _color, _thickness)


# Global variable for barcode
code = 0

def gen(frame):
    while True:
        # Try to decode every frame from the camera with pyzbar
        decoded = pb.decode(frame)

        if decoded != []:
            # Barcode found in frame > add info to objects[] for every barcode that was seen
            objects = []

            for decode in decoded:
                # b'541838' > 541838
                name = str(decode.data).replace("b'", "")
                barcode = name.replace("'", "")

                # Get type and rect
                type = decode.type
                rect = decode.rect
                objects.append({'barcode': barcode, 'type': type, 'rect': rect})

            for o in objects:
                # Add text to barcode rect
                setText(frame, f"{o['barcode']}", (o['rect'].left - 50, o['rect'].top - 50), font_duplex, 1, (255, 255, 255), 2)
                setText(frame, f"{o['type']}", (o['rect'].left - 50, o['rect'].top - 20), font_simple, 2, (255, 255, 255), 2)

                # Change global barcode variable to last barcode in objects[]
                global code
                code = o['barcode']

                # optional: choose object

        return [frame, code]
