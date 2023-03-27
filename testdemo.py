from tkinter import *
window = Tk()

window.geometry("400x300+20+10")
window.title("My First Graphical User Interface")

txt = Entry(text="I am text field")
txt.place(x=100,y=100)
btn = Button(text = "I am button"),
