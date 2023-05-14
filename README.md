# Virtual Mouse
Virtual mouse script for which you just need a keyboard

I wrote this basic program for a friend when his mouse stopped working, it is not very advanced or convenient, but if you need a quick replacement for your non-working mouse you will find everything you need here.
- Move the cursor using the arrows
- After running the program, bind each button of your virtual mouse with the keyboard keys you don't need

# Setup
Before running the program, make sure you have installed all the modules from the requirements.txt file

`pip install -r requirements.txt`

If everything was successful, you can run the program and hope that everything will work :)

# Demonstration
![Demo](https://github.com/iJakub/Virtual-Mouse/blob/main/demo/demo.gif)

# Compilation using PyInstaller
If you want to use the program on a computer that does not have the necessary software installed, use the PyInstaller module to compile it into an executable file

**Module installation**

`pip install pyinstaller`

**Compilation**

`pyinstaller --noconfirm --onedir --windowed --add-data "img;img/" "main.py"`
