#iJ

from tkinter import *
from pynput.keyboard import Listener
import tkinter
from PIL import ImageTk, Image  
import time
import mouse

#enable/disable arrows to move the cursor:
arrows = True

root = tkinter.Tk()
root.title("⇱")
root.geometry("180x200")
root.resizable(False,False)
root.configure(bg='#191919')

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="#191919", width=700, height=400)
canvas.pack()

mouseimg = ImageTk.PhotoImage(file="img/mouse.png")
leftimg = ImageTk.PhotoImage(file="img/left.png")
middleimg = ImageTk.PhotoImage(file="img/middle.png")
rightimg = ImageTk.PhotoImage(file="img/right.png")

headlinelabel = Label(root, bg='#191919', text="Setup", font=("Bahnschrift", 14, "bold"), fg="white")
headlinelabel.place(x=2, y=2 ,height=25, width=176)

infolabel = Label(root, bg='#191919', text="Press the key you want to bind \nto the left mouse button:", font=("Bahnschrift", 9), fg="white")
infolabel.place(x=2, y=30 ,height=30, width=170)

clearmouse = canvas.create_image(90,100,image=mouseimg)


left = ""
middle = ""
right = ""

def setup():
    def on_press(key):
        global left, middle, right

        if left == "":
            left = key
            infolabel.config(text = f"The left mouse button \nbinded with: {str(left).upper()}")
            root.update()
            time.sleep(1)
            infolabel.config(text = "Press the key you want to bind \nto the middle mouse button:")         
            canvas.delete(leftmouse)
            canvas.itemconfigure(middlemouse, state="normal")  
            root.update()

        elif middle == "":
            middle = key
            infolabel.config(text = f"The middle mouse button \nbinded with: {str(middle).upper()}")
            root.update()
            time.sleep(1)
            infolabel.config(text = "Press the key you want to bind \nto the right mouse button:")         
            canvas.delete(middlemouse)
            canvas.itemconfigure(rightmouse, state="normal")   
            root.update()

        elif right == "":
            right = key
            infolabel.config(text = f"The right mouse button \nbinded with: {str(right).upper()}")
            root.update()
            time.sleep(1)     
            canvas.delete(rightmouse)
            root.update()
            virtualmouse()
        return left, middle, right

    leftmouse = canvas.create_image(90,100,image=leftimg)
    middlemouse = canvas.create_image(90,100,image=middleimg, state="hidden")
    rightmouse = canvas.create_image(90,100,image=rightimg, state="hidden")

    listener = Listener(on_press=on_press)
    listener.start()

    

def virtualmouse():
    global left, middle, right, arrows
    
    leftmouse = canvas.create_image(90,100,image=leftimg, state="hidden")
    middlemouse = canvas.create_image(90,100,image=middleimg, state="hidden")
    rightmouse = canvas.create_image(90,100,image=rightimg, state="hidden")
    
    infolabel.destroy()

    headlinelabel.config(text = f"Left:\t{str(left).upper():<13}\nMiddle:\t{str(middle).upper():<13}\nRight:\t{str(right).upper():<13}", font=("Courier New", 8), anchor="w")
    headlinelabel.place(x=2, y=5 ,height=50, width=176)
    root.update()

    def on_press(key):

        if str(key).upper() == str(left).upper():
            mouse.hold(button='left')
            canvas.itemconfigure(leftmouse, state="normal")

        if str(key).upper() == str(middle).upper():
            mouse.click("middle")
            canvas.itemconfigure(middlemouse, state="normal")

        if str(key).upper() == str(right).upper():
            mouse.click("right")
            canvas.itemconfigure(rightmouse, state="normal")

        if arrows == True:

            if str(key).upper() == "KEY.UP":
                current_position = mouse.get_position()
                mouse.move(*(current_position[0], current_position[1] - 15), absolute=True, duration=0)

            if str(key).upper() == "KEY.DOWN":
                current_position = mouse.get_position()
                mouse.move(*(current_position[0], current_position[1] + 15), absolute=True, duration=0)

            if str(key).upper() == "KEY.RIGHT":
                current_position = mouse.get_position()
                mouse.move(*(current_position[0] + 15, current_position[1]), absolute=True, duration=0)

            if str(key).upper() == "KEY.LEFT":
                current_position = mouse.get_position()
                mouse.move(*(current_position[0] - 15, current_position[1]), absolute=True, duration=0)

    def on_release(key):

        if str(key).upper() == str(left).upper():
            canvas.itemconfigure(leftmouse, state="hidden")
            mouse.release(button='left')

        if str(key).upper() == str(middle).upper():
            canvas.itemconfigure(middlemouse, state="hidden")

        if str(key).upper() == str(right).upper():
            canvas.itemconfigure(rightmouse, state="hidden")

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()


setup()
root.mainloop()