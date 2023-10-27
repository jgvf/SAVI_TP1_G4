#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import copy
import sys



def main():
  
    template_1=cv2.imread('./database/joao_figueiredo/1.jpg')
    template_2=cv2.imread('./database/emanuel/1.jpg')
    #template_3=cv2.imread('./database/joao_figueiredo/1.jpg')
    template_1=cv2.resize(template_1,(200,200))
    template_2=cv2.resize(template_2,(200,200))

    cv2.imshow('template_1',template_1)
    cv2.imshow('template_2',template_2)
    while(True):
        key = cv2.waitKey(1)
        if key == 27: # esc
            break
                

    cv2.destroyAllWindows()


if __name__ =="__main__":
    main()
