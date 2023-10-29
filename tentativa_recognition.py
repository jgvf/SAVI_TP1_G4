#!/usr/bin/env python3

import face_recognition
import os , sys
import cv2
import numpy as np
import math



def face_confidence(face_distance, face_match_threshold=0.6):
    range= (1.0 - face_match_threshold)
    linear_value = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_value * 100, 2)) + '%'
    else:
        value = (linear_value + ((1.0 - linear_value) * math.pow((linear_value - 0.5)*2, 0.2))) * 100
        return str(round(value, 2)) + '%'
    

class FaceRecognition:
    face_locations = []
    face_encodings = []
    face_names = []
    known_face_encodings = []
    known_face_names = []
    process_current_frame = True 

    def __init__(self):
        pass
        # encode faces

    
    def encode_faces(self):
        for image in os.listdir('faces')
        face_image = face_recognition.load_image_file(f'faces/{image}')
        face_encoding = face_recognition.face_encodings(face_image)[0]

        self.known_face_encodings.append(face_encoding)
    
    print(self.known_face_names)

if __name__ == '__main__':
    fr = FaceRecognition()

    
    








