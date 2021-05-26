from app import app
from flask import Flask, render_template, Response
import os
import cv2

# paste camera stream url in quotations ("url") or use 0 to use webcam 
cam_url = os.getenv('CAMERA_STREAM_URL', '0')


def process_frame(frame):
    # do the image processing here
    return frame


@app.route('/')
def home():
    return render_template('index.html')


def stream():
    cap = cv2.VideoCapture(cam_url)
    while True:
        cv2.waitKey(1)
        success, frame = cap.read()
        frame = process_frame(frame)
        if success:
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/live_stream/', methods=["GET"])
def live_stream():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
