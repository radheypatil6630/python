import datetime
from tkinter import *
import calendar

def showCalendar():
    year=int(year_field.get())
    print(calendar.calendar(year))

    '''born=datetime.datetime.strptime('%d %m %y')
    return(calendar.day_name[born])'''
    print("day of 31 dec (mon= 0 & so on) =",calendar.weekday(year,month,day))
new=Tk()
new.config(background='#856ff8')
new.title("Calendar")
new.geometry("300x250")

day=31
month=12
cal=Label(new,text="Calendar",bg="#856ff8",font=("times",28,"bold"))
year=Label(new,text="Enter year",bg="pink",font=("calibri",12))
year_field=Entry(new,bg="red",fg="Black",font=("times",10,"bold","italic"))
button=Button(new,text="Show Calendar",fg="Black",bg="yellow",command=showCalendar)

cal.place(x=80,y=20)
year.place(x=50,y=90)
year_field.place(x=140,y=90)
button.place(x=90,y=130)
new.mainloop()