from tkinter import *
import qrcode
import easygui
import cv2
import tkinter.messagebox as tmsg

Divyansh = Tk()

Divyansh.geometry("850x800")
Divyansh.minsize(675,750)
Divyansh.maxsize(1000,900)
Divyansh.title("QR Generator and decoder by Divyansh Yadav")
# icon = PhotoImage(file = "2.ico")
# Divyansh.iconbitmap(icon)

# bg=PhotoImage(file="image.png")
bg_label=Label(Divyansh)
bg_label.place(x=-100,y=100,relwidth=1,relheight=1)


def generate_QR():  
    t1=Name.get()

    t2=Registration_Number.get()
    t3=TexT.get()
    if((len(t1)==0 and len(t2)!=0) or (len(t1)!=0 and len(t2)==0)):
        if len(t1)==0:
            t4=f"Reg.No:{t2}_Text:{t3}"
        else:
            t4=f"Name:{t1}_Text:{t3}"
    elif(len(t1)==0 and len(t2)==0 and len(t3)==0):
        Label(text="Enter some information first!",font=("Fira Code","10","bold"),bg="red").grid(row=20,column=1,pady=10,sticky=W)
        return 
    elif(len(t1)==0 and len(t2)==0 and len(t3)!=0):
        t4=t3
    else:
        t4=f"Name:{t1}_Reg.No:{t2}_Text:{t3}"

    img = qrcode.make(t4)
    img.save("myQR.jpg")
    photo = PhotoImage(file="myQR.jpg")

    l2 = Label(image=photo)
    l2.image = photo
    l2.grid(row=17,column=1,sticky=W,pady=10)
    Label(text="QR code generated successfully!",font=("Fira Code","10","bold"),bg="yellow").grid(row=20,column=1,pady=10,sticky=W)

def getpath():
    t=easygui.fileopenbox()
    d = cv2.QRCodeDetector()
    val, _, _ = d.detectAndDecode(cv2.imread(t))
    tmsg.showinfo("Scanned Image contains",val)
    

l1 = Label(Divyansh,text="QR Code Generator and Decoder by Divyansh Yadav", bg="cyan", fg="brown", font=("Ubuntu", 18, "bold", "italic"), borderwidth=4, relief=RAISED)


browse=Button(text="browse",font=("Aerial" ,"15", "bold"),command=getpath,fg="blue")

generate_button = Button(fg="Red", text="GENERATE QR CODE",font="cursive 11 bold", bg="white",height=5,command=generate_QR)

name_label=Label(text="Name:",font=("Aerial" ,"15", "bold"))

text_label=Label(text="Text:",font=("Aerial" ,"15", "bold"))
Registration_number_label=Label(text="Registration Number:",font=("Aerial" ,"15", "bold"))
file_label=Label(text="Image path:",font=("Aerial" ,"15", "bold"))


Name=StringVar()
TexT=StringVar()
Registration_Number=StringVar()

Name=Entry(text="Enter name",textvariable=Name,width=35)

Text_entry=Entry(text="Enter name",textvariable=TexT,width=35)

Registration_Number=Entry(text="Enter registration number",textvariable=Registration_Number,width=35)


l1.grid(row=0,column=1,columnspan=3,pady=10)

name_label.grid(row=4,column=0)

text_label.grid(row=10,column=0)

Registration_number_label.grid(row=7,column=0)

Name.grid(row=4,column=1,sticky=W,pady=10)

Text_entry.grid(row=10,column=1,sticky=W,pady=10)

Registration_Number.grid(row=7,column=1,sticky=W,pady=10)

generate_button.grid(row=13,column=1,sticky=W,columnspan=2)

file_label.grid(row=4,column=2)

browse.grid(row=5,column=2,rowspan=4)

Divyansh.mainloop()