from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl , xlrd
from openpyxl import Workbook
import pathlib

background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("Student Registration")
root.geometry("1250x700+5+5")
root.config(bg=background)

file=pathlib.Path('Students_data.xlsx')
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1'] = "Registration No."
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date of Registration"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Father's Name"
    sheet['J1'] = "Mother's Name"
    sheet['K1'] = "Father's Occupation"
    sheet['L1'] = "Mother's Occupation"

    file.save('Students_data.xlsx')

#Exit
def Exit():
    root.destroy()

#Upload
def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="Select image file", filetype=(("JPG File", "*.jpg"),
                                                                             ("PNG File", "*.png"),
                                                                             ("All Files", "*.txt")))
    img = (Image.open(filename))
    resized_image=img.resize((190,190))
    photo2 = ImageTk.PhotoImage(resized_image)
    lbl.config(image=photo2)
    lbl.image=photo2




#gender
def selection():
    value=radio.get()
    if value==1:
        gender="Male"

    else:
        gender="Female"


#top frames
Label(root, text="Email: parvatcomputertechnology@gmail.com", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text="STUDENT REGISTRATION", width=10, height=2, bg="#c36464", fg="#fff", font="Arial 20 bold").pack(side=TOP, fill=X)

#search box to update
Search = StringVar()
Entry(root, textvariable=Search, width=15, bd=2, font="Arial 20").place(x=820, y=70)
Srch = Button(root, text="Search \U0001F50E", compound=LEFT, width=12, bg="#68ddfa", font="Arial 13 bold")
Srch.place(x=1060, y=70.5)

# imageicon4 = PhotoImage(file="")
# Update_button = Button(root, image=imageicon4, bg="#c36464").place(x=110, y=64)

#Registration and Date
Label(root, text="Registration No.", font="Arial 13", fg=framebg, bg=background).place(x=30, y=150)
Label(root, text="Date: ", font="Arial 13", fg=framebg, bg=background).place(x=500, y=150)

Registration=StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font="Arial 10")
reg_entry.place(x=160, y=150)

#registration_no()
# today = date.today()
# d1 = today.strftime("%d/%m/%Y")
# date_entry = Entry(root, textvariable=Date, width=15, font="Arial 10").place(x=550, y=150)
#
# Date.set(d1)

#Student details
obj = LabelFrame(root, text="Student's Details", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(obj, text="Full Name:", font="Arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj, text="Date of Birth:", font="Arial 13", bg=framebg, fg=framefg).place(x=30, y=100)
Label(obj, text="Gender:", font="Arial 13", bg=framebg, fg=framefg).place(x=30, y=150)

Label(obj, text="Class:", font="Arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(obj, text="Religion:", font="Arial 13", bg=framebg, fg=framefg).place(x=500, y=100)
Label(obj, text="Skills:", font="Arial 13", bg=framebg, fg=framefg).place(x=500, y=150)

Name=StringVar()
name_entry = Entry(obj, textvariable=Name, width=20, font="Arial 10").place(x=160, y=50)

DOB=StringVar()
dob_entry = Entry(obj, textvariable=DOB, width=20, font="Arial 10").place(x=160, y=100)

radio=IntVar()
R1=Radiobutton(obj, text="Male", variable=radio, value=1, bg=framebg, fg=framefg, command=selection).place(x=150, y=150)
R2=Radiobutton(obj, text="Female", variable=radio, value=2, bg=framebg, fg=framefg, command=selection).place(x=200, y=150)

Religion=StringVar()
religion_entry = Entry(obj, textvariable=Religion, width=20, font="Arial 10").place(x=630, y=100)

Skill=StringVar()
skill_entry = Entry(obj, textvariable=Skill, width=20, font="Arial 10").place(x=630, y=150)

Class = Combobox(obj, values=['1','2','3','4','5','6','7','7','8','9','10','11','12'], font="Roboto 10", width=17, state="r")
Class.place(x=630, y=50)
Class.set("Select Class")

#Parents details
obj2 = LabelFrame(root, text="Parent's Details", font=20, bd=2, width=900, bg=framebg, fg=framefg, height=220, relief=GROOVE)
obj2.place(x=30, y=470)

Label(obj2, text="Father's Name:", font="Arial 13", bg=framebg, fg=framefg).place(x=30, y=50)
Label(obj2, text="Occupation:", font="Arial 13", bg=framebg, fg=framefg).place(x=30, y=100)

F_Name=StringVar()
f_entry = Entry(obj2,textvariable=F_Name, width=20, font="Arial 10")
f_entry.place(x=160, y=50)

Father_Occupation=StringVar()
F0_entry = Entry(obj2, textvariable=Father_Occupation, width=20, font="Arial 10")
F0_entry.place(x=160, y=100)

Label(obj2, text="Mother's Name:", font="Arial 13", bg=framebg, fg=framefg).place(x=500, y=50)
Label(obj2, text="Occupation:", font="Arial 13", bg=framebg, fg=framefg).place(x=500, y=100)

M_Name=StringVar()
m_entry = Entry(obj2,textvariable=M_Name, width=20, font="Arial 10")
m_entry.place(x=630, y=50)

Mother_Occupation=StringVar()
M0_entry = Entry(obj2, textvariable=Mother_Occupation, width=20, font="Arial 10")
M0_entry.place(x=630, y=100)

#image
f=Frame(root, bd=3, bg="Black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)
img=PhotoImage(file="Images/upload photo.png")
lbl=Label(f, bg="Black", image=img)
lbl.place(x=0, y=0)

#button
Button(root, text="Upload", width=19, height=2, font="Arial 12 bold", bg="lightblue", command=showimage).place(x=1000, y=370)
saveButton = Button(root, text="Save", width=19, height=2, font="Arial 12 bold", bg="lightgreen")
saveButton.place(x=1000, y=450)
Button(root, text="Reset", width=19, height=2, font="Arial 12 bold", bg="lightpink").place(x=1000, y=530)
Button(root, text="Exit", width=19, height=2, font="Arial 12 bold", bg="grey", command=Exit).place(x=1000, y=610)

root.mainloop()
