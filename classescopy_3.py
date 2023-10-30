#!/usr/bin/env python3

import face_recognition
import os , sys
import copy
import csv
import time
import math
import pyttsx3
import cv2
import numpy as np

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
        self.engine = pyttsx3.init()
        self.encode_faces()#ler a base de dados
        #self.run_recognition(frame)#encontrar as pessoas
        self.engine.say(f" welcome noobs!")
        self.engine.runAndWait()

    def encode_faces(self):
        for image in os.listdir('faces'):
            face_mane=[]
            face_encoding=[]
            known_face_encodings = []
            known_face_names = []
            face_image = face_recognition.load_image_file(f'faces/{image}')
            face_encoding = face_recognition.face_encodings(face_image)[0]
            # Remova a extensão ".jpeg" do nome do arquivo
            nome_completo = os.path.basename(image)
            nome_sem_extensao = os.path.splitext(nome_completo)[0]
            
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(nome_sem_extensao)
        print(self.known_face_names)

    def run_recognition(self,frame,image_gui,list,unknown_list):
  
        if self.process_current_frame:
           # print('entrou no if run recognition')
            samll_frame = cv2.resize(frame, (100, 100), fx=0.25, fy=0.25)
            rgb_small_frame =samll_frame[:, :, ::-1]

            #find all faces in current frame
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(samll_frame, self.face_locations)

            self.face_names = []
            self.list_runed=list
            i=unknown_list
            for face_encoding in self.face_encodings:
                #print('encontrou alguem')
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = ('Unknown_'+str(i))
                confidence = 'Unknown_'
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding) 
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                    confidence= face_confidence(face_distances[best_match_index])
                if name == ('Unknown_'+str(i)):
                    print('i=',i)
                    i+=1
                    #deteteu um Unknown o que significa que temos que atualizar a base de dados
                    cv2.imwrite('./faces/'+str(name)+'.jpeg',frame)
                    self.encode_faces()
                    
                if not name in self.list_runed:
                    self.list_runed.append(name)
                    self.engine.say(f"Olá, {name}!")
                    print('já cumprimentei @:',name)
                    self.engine.runAndWait()
                    
                self.face_names.append(f'{name} ({confidence})')
                print('encontrei o ',name,' e tenho: ',confidence,'de certeza')
                unknown_list=i
           

        self.process_current_frame = not self.process_current_frame
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                top*= 4
                right*= 4 
                bottom*= 4
                left*= 4

                cv2.putText(image_gui, name, (left+80, bottom - 180), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 1)
        return(self.list_runed,unknown_list,image_gui)
    
 


def computeIOU(d1, d2):
    # box1 and box2 should be in the format (x1, y1, x2, y2)
    x1_1, y1_1, x2_1, y2_1 = d1.left, d1.top, d1.right, d1.bottom
    x1_2, y1_2, x2_2, y2_2 = d2.left, d2.top, d2.right, d2.bottom
    
    # Calculate the area of the first bounding box
    area1 = (x2_1 - x1_1) * (y2_1 - y1_1)
    
    # Calculate the area of the second bounding box
    area2 = (x2_2 - x1_2) * (y2_2 - y1_2)
    
    # Calculate the coordinates of the intersection
    x1_i = max(x1_1, x1_2)
    y1_i = max(y1_1, y1_2)
    x2_i = min(x2_1, x2_2)
    y2_i = min(y2_1, y2_2)
    
    # Check if there is an intersection
    if x1_i < x2_i and y1_i < y2_i:
        # Calculate the area of the intersection
        area_i = (x2_i - x1_i) * (y2_i - y1_i)
        
        # Calculate the area of the union
        area_u = area1 + area2 - area_i
        
        # Calculate IoU
        iou = area_i / area_u
        return iou
    else:
        return 0.0


class Detection():
    def __init__(self, left, right, top, bottom, id, stamp):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.cx = int((left + right)/2)
        self.cy = int((top + bottom)/2)
        self.detection_id = id
        self.stamp = stamp

    def draw(self, image, color, draw_position='bottom', text=None):
        start_point = (self.left, self.top)
        end_point = (self.right, self.bottom)
        cv2.rectangle(image, start_point, end_point, color, 3)

        if text is None:
            text = 'Det ' + self.detection_id

        if draw_position == 'bottom':
            position = (self.left, self.bottom + 30)
        else:
            position = (self.left, self.top-10)


        cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

        # Draw center of box
        cv2.line(image, (self.cx, self.cy), (self.cx, self.cy), color, 3) 
        return(start_point , end_point)
    
    def getLowerMiddlePoint(self):
        return (self.left + int((self.right - self.left)/2) , self.bottom)


class Track():

    # Class constructor
    def __init__(self, id, detection,  color=(255, 0, 0)):
        self.track_id = id
        self.color = color
        self.detections = [detection]
        self.active = True

        #print('Starting constructor for track id ' + str(self.track_id))

    def draw(self, image):

        #Draw only last detection
        self.detections[-1].draw(image, self.color, text=self.track_id, draw_position='top')

        for detection_a, detection_b in zip(self.detections[0:-1], self.detections[1:]):
            start_point = detection_a.getLowerMiddlePoint()
            end_point = detection_b.getLowerMiddlePoint()
            cv2.line(image, start_point, end_point, self.color, 3) 
        

    def update(self, detection):
        self.detections.append(detection)

