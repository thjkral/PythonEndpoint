import cv2
import pyzbar

# from imutils.video import VideoStream
# https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/

font_duplex = cv2.FONT_HERSHEY_DUPLEX
font_simple = cv2.FONT_HERSHEY_PLAIN


def setText(_img, _string, _pos, _font, _scale, _color, _thickness):
  # cv2.putText(img, string, pos, font, scale, color, thickness)
  txt_shadow = cv2.putText(_img, _string, _pos, _font, _scale, (0, 0, 0), _thickness + 1)
  txt = cv2.putText(_img, _string, _pos, _font, _scale, _color, _thickness)


code = 0


def gen():
  camera = cv2.VideoCapture(0)
  while True:
    success, frame = camera.read()
    if not success:
      # todo show picture > no camera found, plug in your webcam and enable it in your browser
      break
    else:
      # decoded = pb.decode(frame)
      # if decoded != []:
      #   objects = []
      #   for decode in decoded:
      #     name = str(decode.data).replace("b'", "")
      #     name = name.replace("'", "")
      #     type = decode.type
      #     rect = decode.rect
      #     objects.append({'name': name, 'type': type, 'rect': rect})
      #
      #   for o in objects:
      #     setText(frame, f"{o['name']}", (o['rect'].left - 50, o['rect'].top - 50), font_duplex, 1, (255, 255, 255), 2)
      #     setText(frame, f"{o['type']}", (o['rect'].left - 50, o['rect'].top - 20), font_simple, 2, (255, 255, 255), 2)
      #     global code
      #     code = o['name']

      ret, buffer = cv2.imencode(".jpg", frame)
      frame = buffer.tobytes()
      yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
      # if decoded != []:
      #   camera.release()
      #   return