import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import os


root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Face Detection')
frame.config(background='light blue')
label = Label(frame, text="Face Detection",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)
label = Label(frame, text="Hey! press Esc/Enter key to exit from the opencv terminal",bg='white',font=('Times 10 bold'))
label.pack(side=TOP)

filename = PhotoImage(file="background.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)




def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n Mentor-Rashmi \n 1.nithin goud")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()
  

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       k = cv2.waitKey(1) & 0xff
       if k==27 or k==13:
          break


   capture.release()
   cv2.destroyAllWindows()


def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
           

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       k = cv2.waitKey(1) & 0xff 
       if k==27:
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()      
 
def imgdet():
    
    root.withdraw()
    file_path = filedialog.askopenfilename()

    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 

    cv2.imshow('img', img)
    cv2.waitKey()

    
def agedet():
    os.system("detect.py")

   
   



but1=Button(frame,padx=5,pady=5,width=20,bg='black',fg='white',relief=GROOVE,command=webdet,text='Open Cam & Detect',font=('helvetica 15 bold'))
but1.place(x=130,y=150)
#250
but2=Button(frame,padx=5,pady=5,width=20,bg='black',fg='white',relief=GROOVE,command=webdetRec,text='Detect & Record',font=('helvetica 15 bold'))
but2.place(x=130,y=220)
#322

but3=Button(frame,padx=5,pady=5,width=20,bg='black',fg='white',relief=GROOVE,command=imgdet,text='upload image',font=('helvetica 15 bold'))
but3.place(x=130,y=290)

but4=Button(frame,padx=5,pady=5,width=20,bg='black',fg='white',relief=GROOVE,command=agedet,text='gender and age detect',font=('helvetica 15 bold'))
but4.place(x=130,y=360)

but4=Button(frame,padx=5,pady=5,width=20,bg='black',fg='white',relief=GROOVE,command=exitt,text='exit',font=('helvetica 15 bold'))
but4.place(x=130,y=430)







root.mainloop()

