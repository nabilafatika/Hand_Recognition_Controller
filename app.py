from flask import Flask, render_template, request
import threading
import time

app = Flask(__name__)

# Global variable to control the gesture controller
controller_running = False
controller_thread = None

def run_gesture_controller():
    global controller_running
    # Imports from Gesture_Controller.py
    from Hand_Controller import GestureController
    gc1 = GestureController()
    while controller_running:
        gc1.start()
    # Clean up code to release the camera
    gc1.stop()  # Make sure this method stops the camera and other resources

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    global controller_running, controller_thread
    if not controller_running:
        controller_running = True
        controller_thread = threading.Thread(target=run_gesture_controller)
        controller_thread.start()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
