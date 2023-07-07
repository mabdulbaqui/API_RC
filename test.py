<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import threading
import cv2
import time
import os

app = Flask(__name__)

# Dummy value to simulate value changing, since we're not using Arduino
value = 280
recording = False

# Create a global variable for the OpenCV VideoCapture object
cap = None


@app.route("/", methods=['GET', 'POST'])
def index():
    global value, recording

    # Mocked reading from Arduino
    arduino_reading = "Mocked Arduino Reading"
=======
from flask import Flask, render_template, request
import threading
import os
import time

app = Flask(__name__)

# Dummy value to simulate changing values without Arduino
value = 280
speed = 0
recording = False

@app.route("/", methods=['GET', 'POST'])
def index():
    global value, recording, speed

    # Simulate an Arduino reading
    arduino_reading = "Simulated reading"
>>>>>>> 2f10285 (Initial commit)

    # Check if this is a POST request
    if request.method == 'POST':
        # Check which button was pressed
        if 'add' in request.form:
            value += 5
<<<<<<< HEAD
            print(f"Simulated sending value to Arduino: S.{value}")  # Print statement to simulate sending to Arduino

        elif 'subtract' in request.form:
            value -= 5
            print(f"Simulated sending value to Arduino: S.{value}")  # Print statement to simulate sending to Arduino

        elif 'start_robot' in request.form:
            print("Simulated start robot command to Arduino")  # Print statement to simulate sending to Arduino

        elif 'stop_robot' in request.form:
            print("Simulated stop robot command to Arduino")  # Print statement to simulate sending to Arduino
        elif 'start_recording' in request.form:
            recording = True
            print("Start recording command")
            # Start the capture thread
            threading.Thread(target=capture_frames).start()
        elif 'stop_recording' in request.form:
            recording = False
            print("Stop recording command")
            # Release the camera when recording is stopped
            if cap is not None:
                cap.release()

    return render_template('index.html', value=value, arduino_reading=arduino_reading)


def capture_frames():
    global cap

    cap = cv2.VideoCapture(1)

    # Set the frame size to 1280x720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Check if the camera is opened
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    # Create a new directory with the current timestamp
    directory_name = f"capture_{int(time.time())}"
    os.makedirs(directory_name)

    while recording:
        # Capture a single frame
        ret, frame = cap.read()

        # Check if the frame was captured successfully
        if not ret:
            print("Error: Could not capture frame")
            break

        # Filename with timestamp and current value
        filename = f"frame_{int(time.time())}_value_{value}.jpg"

        # Create the full path to save the image
        full_path = os.path.join(directory_name, filename)

        # Save the frame
        cv2.imwrite(full_path, frame)
        print(f"Frame saved as {full_path}")

        # Sleep for a bit to not overwhelm the system
        time.sleep(0.1)

    # Release the camera when done
    cap.release()
=======

        elif 'subtract' in request.form:
            value -= 5

        elif 'start_robot' in request.form:
            print("Start robot command")

        elif 'stop_robot' in request.form:
            print("Stop robot command")

        elif 'start_recording' in request.form:
            recording = True
            print("Start recording command")
            # Start the simulated capture thread
            threading.Thread(target=simulated_capture_frames).start()

        elif 'stop_recording' in request.form:
            recording = False
            print("Stop recording command")

        elif 'speed_up' in request.form:
            # Increase the speed by 5
            speed += 5
            print(f"Speed increased to {speed}")

        elif 'speed_down' in request.form:
            # Decrease the speed by 5
            speed -= 5
            print(f"Speed decreased to {speed}")

    return render_template('index.html', value=value, arduino_reading=arduino_reading, speed=speed)


def simulated_capture_frames():
    # Simulate the recording of frames
    while recording:
        # Simulate the saving of a frame
        print(f"Simulated saving of frame at value {value}")

        # Sleep for a bit to not overwhelm the system
        time.sleep(1)
>>>>>>> 2f10285 (Initial commit)


# Start Flask application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
