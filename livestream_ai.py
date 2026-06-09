from flask import Flask, Response
from picamera2 import Picamera2
import cv2
import time

from models import SCRFD, Attribute
from utils.helpers import Face, draw_face_info

app = Flask(__name__)

print("Loading models...")
detection_model = SCRFD(model_path="weights/det_10g.onnx")
attribute_model = Attribute(model_path="weights/genderage.onnx")
print("Models loaded")
frame_count = 0
cached_frame = None
picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (320, 240)}
)

picam2.configure(config)
picam2.start()

time.sleep(2)

def process_frame(frame):
    try:
        boxes_list, points_list = detection_model.detect(frame)

        for boxes, keypoints in zip(boxes_list, points_list):
            *bbox, conf = boxes

            gender, age = attribute_model.get(frame, bbox)

            face = Face(
                kps=keypoints,
                bbox=bbox,
                age=age,
                gender=gender
            )

            draw_face_info(frame, face)

    except Exception as e:
        print("Inference error:", e)

    return frame
def generate():
    global frame_count, cached_frame

    while True:
        frame = picam2.capture_array()

        if frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        frame_count += 1

        # Run CNN only every 5th frame
        if frame_count % 5 == 0:
            processed = frame.copy()
            processed = process_frame(processed)
            cached_frame = processed

        # Use last processed frame in between
        if cached_frame is not None:
            display_frame = cached_frame
        else:
            display_frame = frame

        ret, buffer = cv2.imencode(
            '.jpg',
            display_frame,
            [cv2.IMWRITE_JPEG_QUALITY, 60]
        )

        if not ret:
            continue

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            buffer.tobytes() +
            b'\r\n'
        )


@app.route('/')
def video_feed():
    return Response(
        generate(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        threaded=True
    )
