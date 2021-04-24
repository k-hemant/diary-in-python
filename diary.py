import tkinter as tk
from tkinter.ttk import *
import webbrowser
import datetime

x = str(datetime.datetime.now())
print("My Diary")
print("Today's Date  : " + x)

win = tk.Tk()
win.wm_iconbitmap('diary.ico')
win.title("Personal Diary    Today's Date : " + x)



canvas = tk.Canvas(win, width=500, height=300, background="white")
canvas.pack(side="bottom", fill="both", expand=True)


    
btn = Button(win, text="My Diary", command=lambda: webbrowser.open('diary.html'))

btn.pack()

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    f = open("diary.html", "a")
    f.write("<font face='Arial'><b><font color='#5500FF'>Date : "+ x +"</font></b><br>"+ inp +"<br></font><hr>")
    f.close()
    webbrowser.open('diary.html')
    lbl.config(text = "Inserted in your Diary Successfully.")
  

inputtxt = tk.Text(win,height = 15,width = 50)
  
inputtxt.pack()
  

printButton = tk.Button(win,text = "Add to Diary",command = printInput,bg='blue', fg='white', font=('helvetica', 9, 'bold'))
printButton.pack()
  

lbl = tk.Label(win, text = "")
lbl.pack()


win.mainloop()

