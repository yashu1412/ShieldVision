import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        # Use MobileNet-SSD pretrained model for person, dog, cat detection
        self.net = cv2.dnn.readNetFromCaffe(
            '/app/src/core/models/deploy.prototxt',
            '/app/src/core/models/mobilenet_iter_73000.caffemodel'
        )
        self.class_names = [
            'background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair',
            'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
            'train', 'tvmonitor'
        ]
        self.target_classes = {'person', 'dog', 'cat'}

    def detect(self, frame, conf_threshold=0.5):
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        self.net.setInput(blob)
        detections = self.net.forward()
        results = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                idx = int(detections[0, 0, i, 1])
                label = self.class_names[idx]
                if label in self.target_classes:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype('int')
                    results.append({'label': label, 'confidence': float(confidence), 'box': (startX, startY, endX, endY)})
        return results
