from tkinter import *
root=Tk()
root.title("ASCII Names")
root.geometry("800x800")
root.config(bg="red")
label1=Label(root,text="Changes the name into ASCII Codes")
label2=Label(root)
textinput1=Entry(root)

def asciiconverter():
    word=textinput1.get()
    for letter in word:
                       label2["text"]+=str(ord(letter))+" "
                         
def reset():
            label2["text"]=""                       





btn1=Button(root,text="Change",command=asciiconverter)
btn2=Button(root,text="Reset",command=reset)
label1.pack()
label2.pack()
textinput1.pack()
btn1.pack()
btn2.pack()


root.mainloop()

