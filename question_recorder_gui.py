from tkinter import *
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib
matplotlib.use("TkAgg")
import question_recorder as qr

root = Tk()
root.geometry("1400x400")
root.title("Question recording system v1.2")

def record_question():
    name        = name_entry.get()
    department  = department_entry.get()
    subject     = subject_entry.get()
    question    = question_entry.get()
    topic       = topic_entry.get()
    
    if date_entry.get() != "":
        date   = date_entry.get()

    else:
        date   = str(datetime.now().strftime(("%d-%m-%Y")))


    qr.student(name).add_question(department, subject, question, topic, date)

    subject_entry.delete(0, "end")
    question_entry.delete(0, "end")
    topic_entry.delete(0, "end")

def analyse():
    name    =   name_entry.get()

    #pulling the dataframe
    question_record = qr.student(name).question_frame()

    fig = Figure(figsize = (5,5), dpi = 100)
    main_plot = fig.add_subplot(111)

    # checking if there is any data
    if sum(question_record["department"] == "TYT") > 0 or sum(question_record["department"] == "AYT")> 0:  
        main_plot.plot(question_record["date"], question_record["question"], label="TYT")
        
    #Canvas
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=RIGHT)  

    #toolbars
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=RIGHT)



#name part
name_label = Label(root, text = "Name")
name_label.place(x = 100, y = 10)

name_entry = Entry(root, bd = 2)
name_entry.place(x = 100, y = 50)


#Department part
department_label = Label(root, text = "Department (TYT/AYT)")
department_label.place(x = 300, y = 10)

department_entry = Entry(root, bd = 2)
department_entry.place(x = 300, y = 50)


#Subject part
subject_label = Label(root, text = "Subject")
subject_label.place(x = 500, y = 10)

subject_entry = Entry(root, bd = 2)
subject_entry.place(x = 500, y = 50)


#Question amount part
question_label = Label(root, text = "Question Amount")
question_label.place(x = 700, y = 10)

question_entry = Entry(root, bd = 2)
question_entry.place(x = 700, y = 50)

#Topic part
topic_label = Label(root, text = "Topic (Not Obligatory)")
topic_label.place(x = 700, y= 110)

topic_entry = Entry(root, bd = 2)
topic_entry.place(x = 700, y = 160)

#Date part
date_label = Label(root, text = "Date (DD-MM-YYYY format) {Not obligatory to enter, in default will add the current date}")
date_label.place(x = 100, y = 110)

date_entry = Entry(root, bd = 2)
date_entry.place(x = 100, y = 160)

#Add question button
record_question_button = Button(root, text = "Add", command = record_question)
record_question_button.place(x = 850, y = 50)


#Analysing button
analiz_button = Button(root, text = "Analyse", command = analyse)
analiz_button.place(x = 100, y = 300)




root.mainloop()