#!/usr/bin/env python3


import copy
import csv
import math
import time
from random import randint
import os,sys

import cv2
import numpy as np
from classes import Detection, Track, computeIOU
from colorama import Fore, Back, Style

from tentativa_recognition_copy_2 import FaceRecognition, face_confidence
import pyttsx3
import face_recognition



def main():
    # --------------------------------------
    # Initialization
    # --------------------------------------
    print('a')
    #cap = cv2.VideoCapture(0)
    print('b')
    # Create face detector
    detector_filename = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    #detector = cv2.CascadeClassifier(detector_filename)
    
    
    #detector_filename = './haarcascade_frontalface_default.xml' 
    #detector = cv2.CascadeClassifier(detector_filename)

    # Parameters
    #distance_threshold = 100
    deactivate_threshold = 5.0 # secs
    iou_threshold = 0.3

    video_frame_number = 0
    person_count = 0
    tracks = []

     # Initialize FaceRecognition class
    face_recognition_instance = FaceRecognition()

    engine = pyttsx3.init() # object creation

    # --------------------------------------
    # Execution
    # --------------------------------------

    while(True): # iterate video frames

        
        result, image_rgb = cap.read() # Capture frame-by-frame
        if result is False:
            break
        image_rgb=cv2.flip(image_rgb,1)
        frame_stamp = round(float(cap.get(cv2.CAP_PROP_POS_MSEC))/1000,2)
        height, width, _ = image_rgb.shape
        image_gui = copy.deepcopy(image_rgb) # good practice to have a gui image for drawing

    
        # ------------------------------------------------------
        # Detect persons using haar cascade classifier
        # ------------------------------------------------------
        image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
        haar_detections = detector_filename.detectMultiScale(
            image_gray, scaleFactor=1.1, minNeighbors=10,minSize=(30, 30))

        # ------------------------------------------------------
        # Create list of detections
        # ------------------------------------------------------
        detections = []
        detection_idx = 0
        for x,y,w,h in haar_detections:
            detection_id = str(video_frame_number) + '_' +  str(detection_idx)
            detection = Detection(x, x+w, y, y+h, detection_id, frame_stamp)
            detections.append(detection)
            detection_idx += 1

        all_detections = copy.deepcopy(detections)

        # ------------------------------------------------------
        # Association step. Associate detections with tracks
        # ------------------------------------------------------
        idxs_detections_to_remove = []
        for idx_detection, detection in enumerate(detections):
            for track in tracks:
                if not track.active:
                    continue
                # --------------------------------------
                # Using distance between centers
                # --------------------------------------
                # How to measure how close a detection is to a tracker?
#                 distance = math.sqrt( (detection.cx-track.detections[-1].cx)**2 + 
#                                       (detection.cy-track.detections[-1].cy)**2 )
# 
#                 if distance < distance_threshold: # This detection belongs to this tracker!!!
#                     track.update(detection) # add detection to track
#                     idxs_detections_to_remove.append(idx_detection)
#                     break # do not test this detection with any other track

                # --------------------------------------
                # Using IOU
                # --------------------------------------
                iou = computeIOU(detection, track.detections[-1])
                print('IOU( ' + detection.detection_id + ' , ' + track.track_id + ') = ' + str(iou))
                if iou > iou_threshold: # This detection belongs to this tracker!!!
                    track.update(detection) # add detection to track
                    idxs_detections_to_remove.append(idx_detection)
                    break # do not test this detection with any other track

        idxs_detections_to_remove.reverse()

        print('idxs_detections_to_remove ' + str(idxs_detections_to_remove))
        for idx in idxs_detections_to_remove:
            print(detections)
            print('deleting detection idx ' + str(idx))
            del detections[idx]

        # --------------------------------------
        # Create new trackers
        # --------------------------------------
        for detection in detections:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            track = Track('T' + str(person_count), detection, color=color)
            tracks.append(track)
            person_count += 1

        # --------------------------------------
        # Deactivate tracks if last detection has been seen a long time ago
        # --------------------------------------
        for track in tracks:
            time_since_last_detection = frame_stamp - track.detections[-1].stamp
            if time_since_last_detection > deactivate_threshold:
                track.active = False
               
        # --------------------------------------
        # Visualization
        # --------------------------------------

        # Draw list of all detections (including those associated with the tracks)
        for detection in all_detections:
            detection.draw(image_rgb, (255,0,0))

        # Draw list of tracks
        for track in tracks:
            if not track.active:
                continue
            track.draw(image_rgb)
            # Face Recognition
            if face_recognition_instance.process_current_frame:
                # Resize the frame and perform face recognition
                small_frame = cv2.resize(image_gui, (100, 100), fx=0.9, fy=0.9)
                rgb_small_frame = small_frame[:, :, ::-1]

                # Find all faces in the current frame
                face_recognition_instance.face_locations = face_recognition.face_locations(rgb_small_frame)
            face_recognition_instance.face_encodings = face_recognition.face_encodings(small_frame, face_recognition_instance.face_locations)

            face_recognition_instance.face_names = []
            for face_encoding in face_recognition_instance.face_encodings:
                matches = face_recognition.compare_faces(face_recognition_instance.known_face_encodings, face_encoding)
               
                face_distances = face_recognition.face_distance(face_recognition_instance.known_face_encodings, face_encoding) 
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = face_recognition_instance.known_face_names[best_match_index]
                    confidence = face_confidence(face_distances[best_match_index])

                    # Change color of detection track to green
                    for track in tracks:
                        if track.active:
                            track.color = (0, 255, 0)  # Green color for the known person
                            track_name = f'{name} ({confidence})'
                            track.draw(image_rgb)
                            # Display name and confidence on the detection track
                            cv2.putText(image_rgb, track_name, (track.detections[-1].cx - 100, track.detections[-1].cy + 150),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, ), 2, cv2.LINE_AA)
                
                    # Say Hello
                    #if count == 0:
                        #engine.setProperty('rate', 125)     # setting up new voice rate
                        #engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
                        #engine.say("Hello" + name)  
                        #engine.runAndWait()
                        #engine.stop()
                        #count= 1
                else:
                    
                     name = 'Unknown'
                     confidence = 'Unknown'
                     # Change color of detection track to red
                     for track in tracks:
                        if track.active:
                            track.color = (0, 0, 255)  # Red color for the track
                            track_name = f'{name} ({confidence})'
                            track.draw(image_rgb)
                            # Display name and confidence on the detection track
                            cv2.putText(image_rgb, track_name, (track.detections[-1].cx - 100, track.detections[-1].cy + 150),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
                            
                face_recognition_instance.face_names.append(f'{name} ({confidence})')

            face_recognition_instance.process_current_frame = not face_recognition_instance.process_current_frame        

        if video_frame_number == 0:
            cv2.namedWindow('GUI',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('GUI', int(width/2), int(height/2))

        # Add frame number and time to top left corner
        cv2.putText(image_rgb, 'Frame ' + str(video_frame_number) + ' Time ' + str(frame_stamp) + ' secs',
                    (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 2, cv2.LINE_AA)

        cv2.imshow('GUI',image_rgb)
            
        key = cv2.waitKey(1)
        if key == 27: # esc
            break

        video_frame_number += 1

    
if __name__ == "__main__":
    main()