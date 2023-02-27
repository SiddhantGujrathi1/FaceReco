from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        
        #image 1
        img = Image.open(r"C:\Users\gujra\OneDrive\Desktop\Face_Recognition System\College Images\SNJB Logo.png")
        img = img.resize((500,150),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=150)

        #image 2
        img1 = Image.open(r"C:\Users\gujra\OneDrive\Desktop\Face_Recognition System\College Images\facial-scanning-AI_SH__1151270825.jpg")
        img1 = img1.resize((500,150),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=550,y=0,width=500,height=150)

        #image 3
        img2 = Image.open(r"C:\Users\gujra\OneDrive\Desktop\Face_Recognition System\College Images\Screenshot 2023-02-26 083309.jpg")
        img2 = img2.resize((500,150),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1050,y=0,width=500,height=150)

        #background image
        img3 = Image.open(r"C:\Users\gujra\OneDrive\Desktop\Face_Recognition System\College Images\BackgroundGradient.png")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=160,width=1530,height=710)

        #title
        title_lbl = Label(bg_img , text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4 = Image.open(r"C:\Users\gujra\OneDrive\Desktop\Face_Recognition System\College Images\R.jpg")
        img4 = img4.resize((200,200),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1_1 = Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=200,height=40)


        #face detector button
        img5 = Image.open(r"C:\Users\gujra\OneDrive\Desktop\Face_Recognition System\College Images\file.enc")
        img5 = img5.resize((200,200),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=200,height=200)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=200,height=40)

        #Attendance System


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()