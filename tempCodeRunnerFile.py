#background image
        img=Image.open(r"D:\Projects_AMS\Attendance Management System\Images\istockphoto-1296650678-1024x1024.jpg")
        img=img.resize((1530,810),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=810)
