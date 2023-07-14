import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import pyautogui
import numpy as np

cnt_cars = 0
idi = []
idi.append(cnt_cars)
idi[cnt_cars] = 0
cbox = 0 
xcoord = []
ccoox = []
ccoox.append(0)
ccooy = []
ccooy.append(0)
a=0
    
while True:
    img = pyautogui.screenshot(region=(400, 600, 1200, 460))
    im = np.array(img)
    bbox, label, conf = cv.detect_common_objects(im)
    obj = cv.detect_common_objects(im)
    print(label)
    # print(len(obj[1]))
    # for i in range(len(label)):
    #     if obj[1][i] == 'car' or obj[1][i] == 'truck':
    #         parado = 0
    #         for j in range(len(ccoox)):
    #             difx = abs(abs(ccoox[j]) - abs(obj[0][i][0]))
    #             dify = abs(abs(ccooy[j]) - abs(obj[0][i][2]))
    #             if difx < 50 and dify < 50:
    #                 a=1
    #                 idi[cnt_cars] = 1
    #                 if difx != 0 and dify != 0:
    #                     parado = 1
    #         if parado == 0:
    #             if a == 1:
    #                 ccoox[i] = obj[0][i][0]
    #                 ccooy[i] = obj[0][i][2]
    #                 a = 0
    #             else:
    #                 ccoox.append(obj[0][i][0])
    #                 ccooy.append(obj[0][i][2])
    #                 a = 0
    #                 cnt_cars += 1
    #                 idi.append(cnt_cars)
    #             print(ccoox, ccooy)        

                    
                    

            # if idi[cnt_cars] == 0:
            #     cnt_cars += 1
            #     idi.append(cnt_cars)
            #     idi[cnt_cars] = 1
            
    print('Nº de coches: ', cnt_cars)        
    output_image = draw_bbox(im, bbox, label, conf)
    cv2.imshow('Detection', output_image)
    
    # for i in enumerate(label):
    #     # print(i[0])
    #     # cv2.imshow('Detection', output_image)
    #     if i[1] == 'car' and id(i) not in idi:
    #         idi.append(id(i))
    #         print(idi[len(idi)-1], i[0])
    #         # cnt_cars += 1
    #         output_image = draw_bbox(im, bbox, label, conf)
    #         # plt.imshow(output_image)
    #         # plt.show()
    #         # print('Number of cars in the image is '+ str(label.count('car')))
    #         cv2.imshow('Detection', output_image)
    #         # print(label, conf, cnt_cars)
    
    
    
    
    
    if cv2.waitKey(1) == ord('q'): # si el usuario presiona q paramos de grabar.

        break
        

cv2.destroyAllWindows() # cerrar la ventana