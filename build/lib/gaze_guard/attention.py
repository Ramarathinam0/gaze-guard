import threading
import time
from collections import deque
from .camera import Camera
from .detector import FaceDetector


class AttentionController:
    def __init__(self, buffer_size=5, delay=0.1):
        self.camera = Camera()
        self.detector = FaceDetector()
        self.running = True

        self.delay = delay

        # history buffer for stability
        self.history = deque(maxlen=buffer_size)

        self.attentive = False
        self.prev_state = False

        # callbacks
        self.on_attention_gain = None
        self.on_attention_loss = None

        # start background thread
        thread = threading.Thread(target=self._run)
        thread.daemon = True
        thread.start()

    def _run(self):
        while self.running:
            frame = self.camera.get_frame()
            face_count = self.detector.get_face_count(frame)

            # logic
            if face_count == 1:
                detected = True
            else:
                detected = False

            self.history.append(detected)

            # Calculate confidence score
            confidence = sum(self.history) / len(self.history)
            
            # Update state based on confidence threshold
            new_state = confidence > 0.6

            if new_state != self.prev_state:
                if new_state and self.on_attention_gain:
                    self.on_attention_gain()
                elif not new_state and self.on_attention_loss:
                    self.on_attention_loss()

            self.attentive = new_state
            self.prev_state = new_state

            time.sleep(self.delay)

    def is_user_attentive(self):
        return self.attentive

    def stop(self):
        self.running = False