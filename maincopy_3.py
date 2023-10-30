#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA

import copy
import csv
import math
import time
import os
from random import randint
from PIL import Image
from PIL import ImageDraw
import cv2
import numpy as np
from classescopy_3 import Detection, Track, computeIOU,face_confidence,FaceRecognition
from colorama import Fore, Back, Style


def main():

    # --------------------------------------
    # Initialization
    # --------------------------------------
    #load faces
    face_recognition = FaceRecognition()
    
    cap = cv2.VideoCapture(0)
    # Create face detector
    detector_filename = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    # Parameters
    deactivate_threshold = 5.0 # secs
    iou_threshold = 0.3
    video_frame_number = 0
    person_count = 0
    tracks = []
    list=[]
    list_unknown=0
    
    # Diretório das imagens
    pasta_imagens = './faces/'
    # Obter lista de nomes de arquivos de imagem na pasta
    imagens = [f for f in os.listdir(pasta_imagens) if f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif'))]

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
        image_rgb_copy=copy.deepcopy(image_rgb)

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
            #saber quem lá está

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
                # Using IOU
                # --------------------------------------
                iou = computeIOU(detection, track.detections[-1])
                #print('IOU( ' + detection.detection_id + ' , ' + track.track_id + ') = ' + str(iou))
                if iou > iou_threshold: # This detection belongs to this tracker!!!
                    track.update(detection) # add detection to track
                    idxs_detections_to_remove.append(idx_detection)
                    break # do not test this detection with any other track
        idxs_detections_to_remove.reverse()
        #print('idxs_detections_to_remove ' + str(idxs_detections_to_remove))
        for idx in idxs_detections_to_remove:
            #print(detections)
            #print('deleting detection idx ' + str(idx))
            del detections[idx]

        # --------------------------------------
        # Create new trackers
        # --------------------------------------
        for detection in detections:
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            track = Track('Person' + str(person_count), detection, color=color)
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
            rec_start,rec_end=detection.draw(image_gui, (255,0,0))
            
        #--------------------------
        #reconecimento das pessoas nas deteções
        #--------------------------
        list,list_unknown,image_gui=face_recognition.run_recognition(image_rgb_copy,image_gui,list,list_unknown)


        # Draw list of tracks
        for track in tracks:
            if not track.active:
                continue
            track.draw(image_gui)
            

        if video_frame_number == 0:
            cv2.namedWindow('GUI',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('GUI',960,1080)
            #cv2.setWindowProperty('GUI', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Add frame number and time to top left corner
        cv2.putText(image_gui, 'Frame ' + str(video_frame_number) + ' Time ' + str(frame_stamp) + ' secs',
                    (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2, cv2.LINE_AA)
        
        # Redimensionar o frame do vídeo
        frame = cv2.resize(image_gui, (640,360))
        x_offset = 960 
        for image_nome in imagens:
            imagem=Image.open(os.path.join(pasta_imagens,image_nome))
            imagem = imagem.resize((960, 1080))
            imagem_array=np.array(imagem)
            #frame[0:540, x_offset:x_offset + 960] = imagem_array
            x_offset += 960  # Adicionar largura da imagem ao deslocamento

        cv2.imshow('GUI',frame)
            
        key = cv2.waitKey(1)
        if key == 27: # esc
            break

        video_frame_number += 1

    
if __name__ == "__main__":
    main()

