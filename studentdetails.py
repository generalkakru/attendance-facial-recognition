from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Student_Details:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Student Details")

        img=Image.open("C:/Users/priti/Desktop/Mini Project Final/Stock Images/mainbg.jpg")
        img=img.resize((1280,720))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1280,height=720)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=180,width=1280,height=580)

        #Left Label Frame
        leftframe=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Course Details", font=("Barlow",12))
        leftframe.place(x=10,y=10,width=680,height=510)

        #Current Course
        course=LabelFrame(leftframe,bd=2,relief=RIDGE,text="Current Course Information", font=("Barlow",12))
        course.place(x=10,y=10,width=660,height=160)

        dep_label=Label(course,text="Department",font=("Barlow",12))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(course,font=("Barlow",12))
        dep_combo["values"]=("Select Department","CS","IT","Mechanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        course_label=Label(course,text="Course",font=("Barlow",12))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(course,font=("Barlow",12))
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        year_label=Label(course,text="Year",font=("Barlow",12))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(course,font=("Barlow",12))
        year_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        sem_label=Label(course,text="Semester",font=("Barlow",12))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(course,font=("Barlow",12))
        sem_combo["values"]=("Select Semester","Sem 1","Sem 2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student Information
        class_student_frame=LabelFrame(leftframe,bd=2,relief=RIDGE,text="Student Information", font=("Barlow",12))
        class_student_frame.place(x=10,y=180,width=660,height=300)

        #A
        stdname=Label(class_student_frame,text="Student Name",font=("Barlow",12))
        stdname.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stdname_entry=ttk.Entry(class_student_frame,width=20,font=("Barlow",12))
        stdname_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #B
        stddiv=Label(class_student_frame,text="Division",font=("Barlow",12))
        stddiv.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stddiv_entry=ttk.Entry(class_student_frame,width=20,font=("Barlow",12))
        stddiv_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #C
        stdroll=Label(class_student_frame,text="Roll Number",font=("Barlow",12))
        stdroll.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        stdroll_entry=ttk.Entry(class_student_frame,width=20,font=("Barlow",12))
        stdroll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #D
        stdgender=Label(class_student_frame,text="Gender",font=("Barlow",12))
        stdgender.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        stdgender_entry=ttk.Entry(class_student_frame,width=20,font=("Barlow",12))
        stdgender_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #E
        stdphn=Label(class_student_frame,text="Contact",font=("Barlow",12))
        stdphn.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        stdphn_entry=ttk.Entry(class_student_frame,width=20,font=("Barlow",12))
        stdphn_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Radio Buttons
        rb1=ttk.Radiobutton(class_student_frame,text="Take Sample",value="yes")
        rb1.grid(row=6,column=0)


if __name__ == "__main__":
    root=Tk()
    obj=Student_Details(root)
    root.mainloop()