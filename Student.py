from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #==========variables===============
        self.var_Dept=StringVar()
        self.var_Course=StringVar()
        self.var_Batch=StringVar()
        self.var_Semester=StringVar()
        self.var_Student_id=StringVar()
        self.var_Name=StringVar()
        self.var_Section=StringVar()
        self.var_RollNumber=StringVar()
        self.var_Gender=StringVar()
        self.var_Teacher=StringVar()        

        #Background Image
        img=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\bgs.png")
        img=img.resize((1530,810),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=810)

        #title of the page
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=30,width=1530,height=45)

        #create frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=100,width=1490,height=750)

        #label frame
        #Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="lightblue",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=650)

        img_left=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\S1.png")
        img_left=img_left.resize((700,150),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        s1_img=Label(self.root,image=self.photoimg_left)
        s1_img.place(x=40,y=140,width=710,height=150)

        #current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=10,y=165,width=700,height=150)

        #DEpartment
        dept_label=Label(Current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Dept,font=("times new roman",12,"bold"),width=17,state="readonly")
        dept_combo["values"]=("Select Department","CSE","CS-AIML","IT","ECE")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label=Label(Current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","B.Tech","M.Tech","BPharma","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(Current_course_frame,text="Batch",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Batch,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2025","2026","2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(Current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Semester","Semester-I","Semester-II","Semester-III","Semester-IV","Semester-V","Semester-VI","Semester-VII","Semester-VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Info
        class_stu_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_stu_frame.place(x=10,y=315,width=700,height=280)

        #Student ID
        sid_label=Label(class_stu_frame,text="Student ID: ",font=("times new roman",12,"bold"),bg="white")
        sid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        sid_entry=ttk.Entry(class_stu_frame,textvariable=self.var_Student_id,width=20,font=("times new roman",12,"bold"))
        sid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        sname_label=Label(class_stu_frame,text="Student Name: ",font=("times new roman",12,"bold"),bg="white")
        sname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        sname_entry=ttk.Entry(class_stu_frame,textvariable=self.var_Name,width=20,font=("times new roman",12,"bold"))
        sname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Student Section
        sdiv_label=Label(class_stu_frame,text="Student Section: ",font=("times new roman",12,"bold"),bg="white")
        sdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #sdiv_entry=ttk.Entry(class_stu_frame,textvariable=self.var_Section,width=20,font=("times new roman",12,"bold"))
        #sdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        sdiv_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_Section,font=("times new roman",12,"bold"),width=17,state="readonly")
        sdiv_combo["values"]=("Select Section","A","B","C","D","E","F")
        sdiv_combo.current(0)
        sdiv_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Student Roll Number
        sroll_label=Label(class_stu_frame,text="Student Roll Number: ",font=("times new roman",12,"bold"),bg="white")
        sroll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        sroll_entry=ttk.Entry(class_stu_frame,textvariable=self.var_RollNumber,width=20,font=("times new roman",12,"bold"))
        sroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender

        sgen_label=Label(class_stu_frame,text="Student Gender: ",font=("times new roman",12,"bold"),bg="white")
        sgen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        sgen_combo=ttk.Combobox(class_stu_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        sgen_combo["values"]=("Select Gender","Male","Female","Other")
        sgen_combo.current(0)
        sgen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
    

        #Teacher Name
        teacher_label=Label(class_stu_frame,text="Teacher: ",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_stu_frame,textvariable=self.var_Teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=4,column=0)

        radiobtn2=ttk.Radiobutton(class_stu_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=4,column=1)

        #button frame
        btn_frame=Frame(class_stu_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=2,y=170,width=690,height=70)

        save_button=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="lightblue")
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="lightblue")
        update_button.grid(row=0,column=1)

        delete_button=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="lightblue")
        delete_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="lightblue")
        reset_button.grid(row=0,column=3)

        btn_frame1=Frame(class_stu_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=2,y=200,width=690,height=35)

        take_photo_button=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="lightblue")
        take_photo_button.grid(row=0,column=0)

        update_photo_button=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="lightblue")
        update_photo_button.grid(row=0,column=1)


        #Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="lightblue",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=650)

        img_right=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\S2.png")
        img_right=img_right.resize((700,150),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        s2_img=Label(Right_frame,image=self.photoimg_right)
        s2_img.place(x=2,y=0,width=710,height=150)

        #===========Searching System================

        #search frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=160,width=700,height=70)

        search_label=Label(search_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="red")
        search_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select ","Roll Number","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=4,padx=10,pady=5,sticky=W)

        search_button=Button(search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="lightblue")
        search_button.grid(row=0,column=5,padx=2)

        showall_button=Button(search_frame,text="Show All",width=11,font=("times new roman",13,"bold"),bg="lightblue")
        showall_button.grid(row=0,column=6,padx=2)

        #===============table frame====================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=240,width=700,height=380)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("Dept","Course","Batch","Semester","Id","Name","Section","Roll","Gender","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Dept",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Batch",text="Batch")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Id",text="Student Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Section",text="Section")
        self.student_table.heading("Roll",text="Roll Number")
        self.student_table.heading("Gender",text="Gender")        
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="PhotoSampleStatus") 
        self.student_table["show"]="headings" 

        self.student_table.column("Dept",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Batch",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Section",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)        
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=150) 
        #self.student_table["show"]="headings"   

        self.student_table.pack(fill=BOTH,expand=1)  
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        #==================Function Declaration==========
    def add_data(self):
        if self.var_Dept.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Qwerty@123#4567",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_Dept.get(),
                                                                                                    self.var_Course.get(),
                                                                                                    self.var_Batch.get(),
                                                                                                    self.var_Semester.get(),
                                                                                                    self.var_Student_id.get(),
                                                                                                    self.var_Name.get(),
                                                                                                    self.var_Section.get(),
                                                                                                    self.var_RollNumber.get(),
                                                                                                    self.var_Gender.get(),
                                                                                                    self.var_Teacher.get(),
                                                                                                    self.var_radio1.get()
                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #=============fetch data==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Qwerty@123#4567",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============get cursor==============

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Dept.set(data[0])
        self.var_Course.set(data[1]),
        self.var_Batch.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_Student_id.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Section.set(data[6]),
        self.var_RollNumber.set(data[7]),
        self.var_Gender.set(data[8]),
        self.var_Teacher.set(data[9]),
        self.var_radio1.set(str(data[10]))

    #==============update Function==============

    def update_data(self):
        if self.var_Dept.get() == "Select Department" or self.var_Name.get() == "" or self.var_Student_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", port=3306, user="root", password="Qwerty@123#4567", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "UPDATE student SET Dept=%s, Course=%s, Batch=%s, Semester=%s, Name=%s, Section=%s, RollNumber=%s, Gender=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s"
                    val = (
                        self.var_Dept.get(),
                        self.var_Course.get(),
                        self.var_Batch.get(),
                        self.var_Semester.get(),
                        self.var_Name.get(),
                        self.var_Section.get(),
                        self.var_RollNumber.get(),
                        self.var_Gender.get(),
                        self.var_Teacher.get(),
                        self.var_radio1.get(),
                        self.var_Student_id.get()
                    )
                else:
                    if not Update:
                        return
                    my_cursor.execute(sql, val)
                    #conn.commit()
                    #self.fetch_data()
                    #conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #=======delete function======                                                    
    def delete_data(self):
        if self.var_Student_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="Qwerty@123#4567",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_Student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=========reset function===========
    def reset_data(self):
        self.var_Dept.set("Select Department")
        self.var_Course.set("Select Course"),
        self.var_Batch.set("Select Year"),
        self.var_Semester.set("Select Semester"),
        self.var_Student_id.set(""),
        self.var_Name.set(""),
        self.var_Section.set("Select Section"),
        self.var_RollNumber.set(""),
        self.var_Gender.set("Male"),
        self.var_Teacher.set(""),
        self.var_radio1.set(str(""))


    #===============generate data set or take photo sMPLE============
    def generate_dataset(self):
        if self.var_Dept.get() == "Select Department" or self.var_Name.get() == "" or self.var_Student_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", port=3306, user="root", password="Qwerty@123#4567", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student SET Dept=%s,Course=%s,Batch=%s,Semester=%s,Name=%s,Section=%s,RollNumber=%s,Gender=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_Dept.get(),
                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                        self.var_Batch.get(),
                                                                                                                                                                                        self.var_Semester.get(),
                                                                                                                                                                        
                                                                                                                                                                                        self.var_Name.get(),
                                                                                                                                                                                        self.var_Section.get(),
                                                                                                                                                                                        self.var_RollNumber.get(),
                                                                                                                                                                                        self.var_Gender.get(),
                                                                                                                                                                                        self.var_Teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),  
                                                                                                                                                                                        self.var_Student_id.get()==id+1
                                                                                                                                                                                        #str(id+1)                                  
                                                                                                                                                                                        )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

            #===========load predefined data on face frontals from opencv======

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    # convert image into grayscale
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                   
                    #Scaling factor=1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"  #store image in jpg format
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                print(f"An error occurred: {str(es)}")



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()