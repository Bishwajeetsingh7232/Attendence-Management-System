from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #======================variables=============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #background image
        img=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\attend.jpg")
        img=img.resize((1530,810),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=810)
        
        #title of the page
        title_lbl=Label(bg_img,text="ATTENDANCE SYSTEM",font=("Times new roman",35,"bold"),bg="gray",fg="black")
        title_lbl.place(x=0,y=30,width=1530,height=45)

        #create frame
        main_frame=Frame(bg_img,bd=2,bg="gray")
        main_frame.place(x=20,y=100,width=1490,height=750)

        #label frame
        #Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="grey",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=650)

        img_left=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\Att.png")
        img_left=img_left.resize((700,285),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        s1_img=Label(self.root,image=self.photoimg_left)
        s1_img.place(x=40,y=140,width=710,height=285)

        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="silver",relief=RIDGE,font=("times new roman",12,"bold"))
        Current_course_frame.place(x=10,y=300,width=700,height=320)

        #Student ID
        attendanceid_label=Label(Current_course_frame,text="Attendance ID: ",font=("times new roman",12,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(Current_course_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student name
        sname_label=Label(Current_course_frame,text="Name: ",font=("times new roman",12,"bold"),bg="white")
        sname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        sname_entry=ttk.Entry(Current_course_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        sname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #date
        sdate=Label(Current_course_frame,text="Date: ",font=("times new roman",12,"bold"),bg="white")
        sdate.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        sdate_entry=ttk.Entry(Current_course_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        sdate_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #department
        sroll_label=Label(Current_course_frame,text="Department: ",font=("times new roman",12,"bold"),bg="white")
        sroll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        sroll_entry=ttk.Entry(Current_course_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        sroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(Current_course_frame,text="Time:",bg="white",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time=ttk.Entry(Current_course_frame,width=22,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #attendance
        attendance_label=Label(Current_course_frame,text="Attendance Status",bg="white",font=("times new roman",12,"bold"))
        attendance_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
    
        self.atten_status=ttk.Combobox(Current_course_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",12, "bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        self.atten_status.current(0)

        #buttons
        btn_frame=Frame(Current_course_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=2,y=250,width=690,height=35)

        save_button=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="lightblue")
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="lightblue")
        update_button.grid(row=0,column=1)

        delete_button=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="lightblue")
        delete_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="lightblue")
        reset_button.grid(row=0,column=3)

        #Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="grey",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=650)

        #create frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="gray")
        table_frame.place(x=10,y=10,width=695,height=600)

        #==============scroll bar table=============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("Student_id","RollNumber","name","Dept","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Student_id",text="Attendance Id")
        self.AttendanceReportTable.heading("RollNumber",text="Roll Number")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("Dept",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")        
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("Student_id",width=100)
        self.AttendanceReportTable.column("RollNumber",width=150)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("Dept",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        #==========fetch data=======================


    def fetchData(self,rows):                                 #it insert the current data in csv file
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import data from csv file 
    def importCsv(self):
        global mydata
        mydata.clear()                        #clear previously stored data
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)       #cwd=current working directory
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])



    #===============reset data===========
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()