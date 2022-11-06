from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import shutil
import os

def mainframe():
    # exec(open('Attendance.py').read())
    import Attendance

def copycsv():
    shutil.copy("C:/Users/priti/PycharmProjects/FacialRecognitionAttendance/Attendance.csv",
                "C:/Users/priti/Desktop/Attendance")

def deletecsv():
    os.remove("C:/Users/priti/Desktop/Attendance/Attendance.csv")

class Face_Recognition:

    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        img=Image.open("C:/Users/priti/PycharmProjects/FacialRecognitionAttendance/Stock Images/mainbg.jpg")
        img=img.resize((1280,720))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1280,height=720)

        #Button 1: Main Button(Opens Mainframe).
        img1=Image.open("C:/Users/priti/PycharmProjects/FacialRecognitionAttendance/Stock Images/b1.jpg")
        img1=img1.resize((200,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(bg_img,image=self.photoimg1,cursor="hand2",command=mainframe)
        b1.place(x=120,y=300,width=200,height=200)

        #Button 2: Provides csv export option.
        img2=Image.open("C:/Users/priti/PycharmProjects/FacialRecognitionAttendance/Stock Images/b2.jpg")
        img2=img2.resize((200,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(bg_img,image=self.photoimg2,cursor="hand2",command=copycsv)
        b2.place(x=540,y=300,width=200,height=200)

        #Button 3: Deletion option for csv file.
        img3=Image.open("C:/Users/priti/PycharmProjects/FacialRecognitionAttendance/Stock Images/b3.jpg")
        img3=img3.resize((200,200))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(bg_img,image=self.photoimg3,cursor="hand2",command=deletecsv)
        b3.place(x=960,y=300,width=200,height=200)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()