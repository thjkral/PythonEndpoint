import cv2
import pyzbar.pyzbar as pb

import imagezmq
import imutils

# from imutils.video import VideoStream
# https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/

font_duplex = cv2.FONT_HERSHEY_DUPLEX
font_simple = cv2.FONT_HERSHEY_PLAIN


# Add text shadow to the cv2 text function
def setText(_img, _string, _pos, _font, _scale, _color, _thickness):
    txt_shadow = cv2.putText(_img, _string, _pos, _font, _scale, (0, 0, 0), _thickness + 1)
    txt = cv2.putText(_img, _string, _pos, _font, _scale, _color, _thickness)


# Global variable for barcode
code = 0


def gen():
    # Get cam
    camera = cv2.VideoCapture(0)
    while True:
        # Camera.read() returns (True, array([pixels])
        success, frame = camera.read()

        if not success:
            # show msg > "no camera found (plug in your webcam and enable it in your browser)"
            break
        else:
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

            # Encode .png to .jpg
            ret, buffer = cv2.imencode(".jpg", frame)

            # Yield as byte array
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            # If barcode found: Stop camera and function
            # Else: Yield frame without barcode info
            if decoded != []:
                camera.release()
                return
