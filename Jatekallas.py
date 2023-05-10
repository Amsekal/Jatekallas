import sys
sys.path.append('C://Users//hallgato//AppData//Roaming//Python//Python311//site-packages')
import cv2
import numpy as np
import time


def grayScale(kep):
    img_grayscale = cv2.imread(kep,0)

    up_width = 500
    up_height = 500
    up_points = (up_width, up_height)
    resized_up = cv2.resize(img_grayscale, up_points, interpolation= cv2.INTER_LINEAR)
 

    cv2.imshow('graycsale image',resized_up)
    
  
    cv2.waitKey(0)
    
    
    cv2.destroyAllWindows()
    ret, thresh1 = cv2.threshold(resized_up, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary Threshold', thresh1) 
    
    cv2.imwrite('Gray.png',resized_up)
  
def korKereses(kep):
    img = cv2.imread(kep, cv2.IMREAD_COLOR)
    
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
    gray_blurred = cv2.blur(gray, (3, 3))
    
    
    detected_circles = cv2.HoughCircles(gray_blurred, 
                    cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
                param2 = 30, minRadius = 20, maxRadius = 40)
    i=0
    korok=[]

    
    if detected_circles is not None:
    
        
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            korok.append(a)
            korok.append(b)
            i=i+1

    
            
            cv2.circle(img, (a, b), r, (0, 255, 0), 2)
            
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
            cv2.imshow("Detected Circle", img)
            cv2.waitKey()
            
    return korok,i


def pozicio(x,y,k):

    xx=0
    yy=0

    if x<k:
        xx=1
    if x<k*2 and x>k:
        xx=2
    if x<k*3 and x>k*2:
        xx=3
    if x<k*4 and x>k*3:
        xx=4
    if x<k*5 and x>k*4:
        xx=5
    if x<k*6 and x>k*5:
        xx=6
    if x<k*7 and x>k*6:
        xx=7
    if x>k*7:
        xx=8
                
                   
    if y<k:
        yy=1
    if y<k*2 and y>k:
        yy=2
    if y<k*3 and y>k*2:
        yy=3
    if y<k*4 and y>k*3:
        yy=4
    if y<k*5 and y>k*4:
        yy=5
    if yy<k*6 and y>k*5:
        yy=6
    if y<k*7 and y>k*6:
        yy=7
    if y>k*7:
        yy=8
    return xx,yy

def main():
    print("1. Dáma")
    print("2. Go")
    print("3. Hnefatafl")
    game = input("Válassz játékot:")
    k=65
    x=0
    y=0
    tabla=np.zeros((8,8))
    fekete=0
    feher=0
    korok=[]
    korokszama=0

    if game == "1":

        grayScale("dama2.png")
        korok,korokszama=korKereses("Gray.png")
        img=cv2.imread("Gray.png",0)
        print("Bábuk száma:",korokszama)

        for i in range(0,len(korok),2):
                x=0
                y=0
                #print(korok[i]," ",korok[i+1],": ",img[korok[i+1],korok[i]])
                if img[korok[i+1],korok[i]]<120:
                    fekete=fekete+1

                    x,y=pozicio(korok[i],korok[i+1],k)
                    tabla[y-1][x-1]=1
                else:
                    feher=feher+1
                    x,y=pozicio(korok[i],korok[i+1],k)

                    tabla[y-1][x-1]=2
                        
                
            
        print("fekete: ",fekete)
        print("feher: ",feher)

        if fekete==0:
            print("Nyert a fehér")
        elif feher==0:
            print("Nyert a fekete")
        else:
            print("Játék folyamatban")
        #print(img.item(346,154))
        print(tabla)
    
    if game == "2":
        grayScale("go.png")
        korok,korokszama=korKereses("Gray.png")

        print("Bábuk száma:",korokszama)
        img=cv2.imread("Gray.png",0)
        for i in range(0,len(korok),2):
                x=0
                y=0
                if img[korok[i+1],korok[i]]<120:
                    fekete=fekete+1
                else:
                    feher=feher+1
        print("fekete: ",fekete)
        print("feher: ",feher)

        if fekete>feher:
            print("Fekete áll nyerésre")
        if fekete<feher:
            print("Fehér áll nyerésre")
        if fekete==feher:
            print("Egyenlő állás")

    if game == "3":
        kiraly=0
        grayScale("hnefa2.png")
        korok,korokszama=korKereses("Gray.png")

        print("Bábuk száma:",korokszama)
        img=cv2.imread("Gray.png",0)
        for i in range(0,len(korok),2):
                x=0
                y=0
                if img[korok[i+1],korok[i]]<180 and img[korok[i+1],korok[i]]!=0:
                    fekete=fekete+1
                else:
                    feher=feher+1
                    if img[korok[i+1],korok[i]]==0:
                        kiraly=1
                        x,y=pozicio(korok[i],korok[i+1],k)
                        if x==1 or x==8:
                            if y==1 or y==8:
                                kiraly=2
        print("fekete: ",fekete)
        print("feher: ",feher)
        if kiraly==1:
            print("A király még játékban van")
        if kiraly==0:
            print("Nyert a fekete")
        if kiraly==2:
            print("Nyert a fehér")
    
    
   # print(img[korok[0],korok[1]])
if __name__ == "__main__":
    main()