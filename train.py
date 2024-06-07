from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #top image
        img=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\tech.jpg")
        img=img.resize((1530,325),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=325)

        #title of the page
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=30,width=1530,height=75)

        #button
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("Times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=0,y=320,width=1530,height=65)

        #bottom image
        img_bottom=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\B7.png")
        img_bottom=img_bottom.resize((1530,525),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        img_bottom=Label(self.root,image=self.photoimg_bottom)
        img_bottom.place(x=0,y=380,width=1530,height=525)


    def train_classifier(self):
        data_dir=("data")          #store datasamples into data directory
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]   

        #according to algorithm image and ids should be matched
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')   #convert gray scale image
            imageNp=np.array(img,'uint8')  #uint8 is a datatype
            id=int(os.path.split(image)[1].split('.')[1])   #convert into grid scale


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)                    #numpy provides 88% info extra

#=======================train the classifier and save===========
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")          #trained data written in this file
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets completed!!")




        

        






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()