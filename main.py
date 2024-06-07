from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
from Student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background image
        img=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\istockphoto-1296650678-1024x1024.jpg")
        img=img.resize((1530,810),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=810)

        #title of the page
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("Times new roman",35,"bold"),bg="gold2",fg="black")
        title_lbl.place(x=0,y=25,width=1530,height=45)

        #student button
        imgb1=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\Button1.png")
        imgb1=imgb1.resize((220,220),Image.LANCZOS)
        self.photoimgb1=ImageTk.PhotoImage(imgb1)

        b1=Button(bg_img,image=self.photoimgb1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=150,width=220,height=220)

        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=200,y=350,width=220,height=40)

        #face detector button
        imgb2=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B2.png")
        imgb2=imgb2.resize((220,220),Image.LANCZOS)
        self.photoimgb2=ImageTk.PhotoImage(imgb2)

        b2=Button(bg_img,image=self.photoimgb2,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=150,width=220,height=220)

        b2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=350,width=220,height=40)

        #Attendance button
        imgb3=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B3.png")
        imgb3=imgb3.resize((220,220),Image.LANCZOS)
        self.photoimgb3=ImageTk.PhotoImage(imgb3)

        b3=Button(bg_img,image=self.photoimgb3,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=150,width=220,height=220)

        b3=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b3.place(x=800,y=350,width=220,height=40)

        #Help DEsk button
        imgb4=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B4.png")
        imgb4=imgb4.resize((220,220),Image.LANCZOS)
        self.photoimgb4=ImageTk.PhotoImage(imgb4)

        b4=Button(bg_img,image=self.photoimgb4,cursor="hand2")
        b4.place(x=1100,y=150,width=220,height=220)

        b4=Button(bg_img,text="Help Desk",cursor="hand2",font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b4.place(x=1100,y=350,width=220,height=40)

        #Train Data Button
        imgb5=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B5.png")
        imgb5=imgb5.resize((220,220),Image.LANCZOS)
        self.photoimgb5=ImageTk.PhotoImage(imgb5)

        b5=Button(bg_img,image=self.photoimgb5,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=450,width=220,height=220)

        b5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b5.place(x=200,y=650,width=220,height=40)

        #Photos Button
        imgb6=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B6.png")
        imgb6=imgb6.resize((220,220),Image.LANCZOS)
        self.photoimgb6=ImageTk.PhotoImage(imgb6)

        b6=Button(bg_img,image=self.photoimgb6,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=450,width=220,height=220)

        b6=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b6.place(x=500,y=650,width=220,height=40)

        #Developer Button
        imgb7=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B7.png")
        imgb7=imgb7.resize((220,220),Image.LANCZOS)
        self.photoimgb7=ImageTk.PhotoImage(imgb7)

        b7=Button(bg_img,image=self.photoimgb7,cursor="hand2")
        b7.place(x=800,y=450,width=220,height=220)

        b7=Button(bg_img,text="Developer",cursor="hand2",font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b7.place(x=800,y=650,width=220,height=40)

        #Exit Button
        imgb8=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B8.png")
        imgb8=imgb8.resize((220,220),Image.LANCZOS)
        self.photoimgb8=ImageTk.PhotoImage(imgb8)

        b8=Button(bg_img,image=self.photoimgb8,cursor="hand2")
        b8.place(x=1100,y=450,width=220,height=220)

        b8=Button(bg_img,text="Exit",cursor="hand2",font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b8.place(x=1100,y=650,width=220,height=40)


    def open_img(self):
        os.startfile("data")
        # ======================FUNCTION BUTTONS====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()