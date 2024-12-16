# Gesture-Based Volume Control

This project implements a gesture-based system to control the system volume using computer vision and hand tracking. By detecting the distance between specific landmarks on your hand (thumb and index finger), the system adjusts the volume dynamically.

## Features
- Hand tracking using **MediaPipe**
- Distance-based gesture recognition to control system volume
- Visual feedback for hand landmarks and volume bar

## Requirements

Make sure to have the following libraries installed before running the project:

- `opencv-python`
- `mediapipe`
- `numpy`
- `pycaw`


## How It Works

1. **Hand Detection**: The code uses MediaPipe's Hands module to detect hand landmarks.
2. **Distance Calculation**: It calculates the distance between the thumb (landmark 4) and index finger (landmark 8).
3. **Volume Adjustment**: The calculated distance is mapped to the system's volume range using the `pycaw` library.
4. **Visual Feedback**: The program provides visual feedback by:
   - Drawing hand landmarks and connections.
   - Displaying a dynamic volume bar on the screen.

## Usage

1. **Run the Code**
   Execute the script in your Python environment:
   ```bash
   python gesture_volume_control.py
   ```
2. **Interact with the System**:
   - Show your hand to the camera.
   - Adjust the distance between your thumb and index finger to control the volume.
   - Close the program by pressing any key while the video window is active.


## Limitations

- Requires a good-quality camera for accurate hand tracking.
- Works best in well-lit environments.
- Might not differentiate between hands if both are in the camera frame.

## Future Improvements

- Add support for multiple gestures.
- Enhance tracking under low-light conditions.
- Integrate additional functionalities like play/pause or next/previous using gestures.

## Author
[Parth Lathiya]
