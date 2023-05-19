import tkinter
m=tkinter.Tk()
Lable1(master,text="first name").grid(row=0)
Lable1(master,text="last name").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
mainloop()