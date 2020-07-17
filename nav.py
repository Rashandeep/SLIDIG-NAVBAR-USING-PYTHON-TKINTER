from tkinter import PhotoImage
import tkinter as tk

# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

# setting root window:
root = tk.Tk()
root.title("Tkinter Navbar")
root.geometry("500x640")

# setting switch state:
btnState = False

# loading Navbar icon image:
# navIcon = PhotoImage(file="menu.png")
# closeIcon = PhotoImage(file="close.png")

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        # brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg="green")
        topFrame.config(bg="green")
        # root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        # brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg="green")
        topFrame.config(bg="green")
        # root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(root, bg="green")
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="title", font="Bahnschrift 15", bg="green", fg="black", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
# brandLabel = tk.Label(root, text="Pythonista\nEmpire", font="System 30", bg="gray17", fg="green")
# brandLabel.place(x=100, y=250)

# Navbar button:
navbarBtn = tk.Button(topFrame, text="MENU", bg="green", activebackground="green", bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=15)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="lightgrey", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg="green", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Mail", "About", "Exit"]
# Navbar Option Buttons:
for i in range(3):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="lightgrey", fg="black", activebackground="lightgrey", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot,text="CLOSE", bg="green", activebackground="green", bd=0, command=switch)
closeBtn.place(x=250, y=15)

# window in mainloop:
root.mainloop()
