#!/usr/bin/env python3

import cv2

def main():
    cam = cv2.VideoCapture(0)

    while True:
        check, frame = cam.read()
        frame=cv2.flip(frame,1)

        cv2.imshow('video', frame)

        key = cv2.waitKey(1)
        if key == 27: # esc
            break
            
    cam.release()
    cv2.destroyAllWindows()


if __name__ =="__main__":
    main()
