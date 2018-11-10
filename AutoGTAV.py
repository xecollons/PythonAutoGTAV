import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, S, D, A

def process_img(original_image):
    #We convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    #edge detection
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def screen_record():
    last_time = time.time()
    while(True):
        #800x600 windowed mode
        screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        PressKey(W)
        time.sleep(3)
        PressKey(W)
        time.sleep(3)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        #now the im updates ocurr every 6 seconds because of the sleeps
        cv2.imshow('window',new_screen)
        #cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
