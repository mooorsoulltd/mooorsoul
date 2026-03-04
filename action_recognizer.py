import cv2
import numpy as np

class ActionRecognizer:
    def __init__(self):
        pass

    def calculate_optical_flow(self, prev_frame, curr_frame):
        # Convert frames to grayscale
        prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
        curr_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

        # Calculate optical flow using Farneback method
        flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        return flow

    def detect_action(self, video_path):
        cap = cv2.VideoCapture(video_path)
        ret, prev_frame = cap.read()

        while True:
            ret, curr_frame = cap.read()
            if not ret:
                break

            flow = self.calculate_optical_flow(prev_frame, curr_frame)
            # Here you can add your logic to analyze the flow and detect actions

            # Update previous frame
            prev_frame = curr_frame

        cap.release()