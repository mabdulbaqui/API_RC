from flask import Flask, render_template, request, redirect, url_for
import threading
import cv2
import time
import os
import serial

app = Flask(__name__)

# Connect to Arduino
ser = serial.Serial('COM6', 9600)

# Dummy value to simulate value changing, as we're not using Arduino
value = 280
recording = False
<<<<<<< HEAD
=======
speed = 0  # Global variable for speed
>>>>>>> 2f10285 (Initial commit)

# Create a global variable for the OpenCV VideoCapture object
cap = None


@app.route("/", methods=['GET', 'POST'])
def index():
<<<<<<< HEAD
    global value, recording
=======
    global value, recording, speed  # Declare speed as global
>>>>>>> 2f10285 (Initial commit)

    # Read Arduino value
    arduino_reading = ser.readline().decode().strip()

    # Check if this is a POST request
    if request.method == 'POST':
        # Check which button was pressed
<<<<<<< HEAD
=======
        # ... (rest of your existing code)

        # Logic for existing buttons
>>>>>>> 2f10285 (Initial commit)
        if 'add' in request.form:
            value += 5
            val = f"S.{value}"
            ser.write(bytes(val, 'utf-8'))

        elif 'subtract' in request.form:
            value -= 5
            val = f"S.{value}"
            ser.write(bytes(val, 'utf-8'))

        elif 'start_robot' in request.form:
            ser.write(b"M.255\n")
            val = f"S.281"
            ser.write(bytes(val, 'utf-8'))

        elif 'stop_robot' in request.form:
            ser.write(b"M.0\n")
<<<<<<< HEAD
=======

>>>>>>> 2f10285 (Initial commit)
        elif 'start_recording' in request.form:
            recording = True
            print("Start recording command")
            # Start the capture thread
            threading.Thread(target=capture_frames).start()
<<<<<<< HEAD
=======

>>>>>>> 2f10285 (Initial commit)
        elif 'stop_recording' in request.form:
            recording = False
            print("Stop recording command")
            # Release the camera when recording is stopped
            if cap is not None:
                cap.release()

<<<<<<< HEAD
    return render_template('index.html', value=value, arduino_reading=arduino_reading)
=======
        # Logic for new buttons
        elif 'speed_up' in request.form:
            # Increase the speed by 5
            speed += 5
            print(f"Speed increased to {speed}")
            # Optionally, send a command to Arduino with new speed
            # Example:
            # ser.write(bytes(f"speed.{speed}", 'utf-8'))

        elif 'speed_down' in request.form:
            # Decrease the speed by 5
            speed -= 5
            print(f"Speed decreased to {speed}")
            # Optionally, send a command to Arduino with new speed
            # Example:
            # ser.write(bytes(f"speed.{speed}", 'utf-8'))

    return render_template('index.html', value=value, arduino_reading=arduino_reading, speed=speed)
>>>>>>> 2f10285 (Initial commit)


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


# Start Flask application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
