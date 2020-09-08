from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

home = Tk() # Window of login page
home.geometry("400x400")
home.configure(bg="light blue",relief="sunken",bd=15)

L = Label(home,text="Login",font=("algerian",48,"bold"),bg="coral",relief="sunken",bd=15)
L.pack(side=TOP,fill="both")


L1 = Label(home,text="USERNAME*",font=("algerian",20,"bold"),bg="medium purple",padx=113,pady=10,relief="sunken",bd=7)

L1.place(x=200,y=130)


name=StringVar()

E1 = Entry(home,textvariable=name,font=("algerian",27,"italic"),bd=10,relief="groove",width=30)

E1.place(x=650,y=130)


L2 = Label(home,text="PASSWORD*",font=("algerian",20,"bold"),bg="medium purple",padx=11,bd=7,pady=10,relief="sunken",width=20)
L2.place(x=200,y=200)

code=StringVar()

E2 = Entry(home,textvariable=code,font=("algerian",27,"italic"),bd=10,relief="groove",show="*",width=30)
E2.place(x=650,y=200)
def qut():
	quit()
	

def check():
		
	if code.get()==regpass.get() and name.get()==regname.get():
		win = Toplevel() # Window of user detail
		win.geometry("580x940")
		win.title("Detail")
		win.configure(bg="darkslategray1")
		L1 = Label(win,text="Your account detail",font=("algerian",25,"bold"),bg="darkslategray3",relief="sunken",bd=15)
		L1.pack(side=TOP,fill="both")
		L2 = Label(win,text="Name : "+regname.get(),font=("algerian",15),bg="darkslategray1")
		L2.place(x=0,y=100)
		L3 = Label(win,text="Age : "+regage.get(),font=("algerian",15),bg="darkslategray1")
		L3.place(x=0,y=150)
		L4 = Label(win,text="Password : "+regpass.get(),font=("algerian",15),bg="darkslategray1")
		L4.place(x=0,y=200)
		L5 = Label(win,text="Phone Number : "+regnum.get(),font=("algerian",15),bg="darkslategray1")
		L5.place(x=0,y=250)
		L6 = Label(win,text="Gender : "+M.get(),font=("algerian",15),bg="darkslategray1")
		L6.place(x=0,y=300)
		L7 = Label(win,text="Location : "+city.get(),font=("algerian",15),bg="darkslategray1")
		L7.place(x=0,y=350)
		L8 = Label(win,text="Working Applications",font=("Elephant",20,"bold"),bg="thistle2",relief="sunken",bd=7,padx=125)
		L8.place(x=0,y=400)
		Bqut = Button(win,command=qut,text="quit",font=("algerian",25,"bold"),bg="red")
		Bqut.place(x=235,y=600) 
		
		Bcal=Button(win,command=opencal,text="Open Calculator",font=("Elephant",15,"bold"),bg="yellow",relief="solid",bd=10,pady=12)
		Bcal.place(x=180,y=500)
		

		
	
		
		L1.pack(side=TOP)
		if code.get()=="":
			win.destroy()
			messagebox.showerror("Not Valid","Please register before using the application\nif you are already registered so check your\npassword and username again !")
			win.mainloop()
		
	
	else:
		messagebox.showerror("Not found","Please check your password and try again !")
		
B1 = Button(home,command=check,text="CONFIRM",font=("algerian",25,"bold"),bd=15,relief="sunken",bg="light green",padx=100,pady=6)
B1.place(x=200,y=280)

def out():
	msg = messagebox.askquestion("Are you sure!","Do you want to quit ?")
	if msg=="yes":
		quit()
		
	else:
		messagebox.showinfo("Done","You are on the same program")
		
	
B2 = Button(home,command=out,text="Quit",font=("algerian",30,"bold"),bg="red",bd=5)
B2.place(x=610,y=560)
regname = StringVar()
regage = StringVar()
regpass = StringVar()
regcon = StringVar()
regnum = StringVar()
M = StringVar()
city =StringVar()
def reg():
	top = Toplevel()     #window of registration 
	top.geometry("500x800")
	top.configure(bg="Light blue",relief="groove",bd=4)
	L1 = Label(top,text="Registration Form",font=("algerian",20,"bold"),bg="goldenrod1",bd=12)
	L1.pack(side=TOP,fill="both")
	L2 = Label(top,text="Enter your age",font=("algerian",13),bg="light blue")
	L2.place(x=0,y=150)
	
	L4 = Label(top,text="Create password",font=("algerian",13),bg="light blue")
	L4.place(x=0,y=200)
	
	L5 = Label(top,text="Confirm password",font=("algerian",12),bg="Light blue")
	L5.place(x=0,y=250)
	
	L6 = Label(top,text="Phone Number",font=("algerian",13),bg="light blue")
	L6.place(x=0,y=300)
	
	L7 = Label(top,text="Gender",font=("algerian",  13),bg="light blue")
	L7.place(x=0,y=350)
	
	L8 = Label(top,text="Where you live",font=("algerian",13),bg = "Light blue")
	L8.place(x=0,y=400)
	
	
	E5 = Entry(top,textvariable=regnum,bd=5)
	E5.place(x=250,y=300)
	
	E4 = Entry(top,textvariable=regcon,bd=5)
	E4.place(x=250,y=250)
	
	E3 = Entry(top,textvariable=regpass,bd=5)
	E3.place(x=250,y=200)
	
	E2 = Entry(top,textvariable=regage,bd=5)
	E2.place(x=250,y=150)

	E7 = Entry(top,textvariable=regname,bd=5,bg="white")
	E7.place(x=250,y=100)

				
	
	L1 = Label(top,text="Enter your name",font=("algerian",13),bg="light blue")
	L1.place(x=0,y=100)
	
	CB1 = Checkbutton(top,text="Male",variable=M,font=("algerian",10),onvalue="Male",offvalue="Female",bg="light blue")
	CB1.place(x=250,y=350)
	CB2 = Checkbutton(top,text="Female",variable=M,font=("algerian",10),bg="light blue",onvalue="Female",offvalue="Male")
	CB2.place(x=350,y=350)
	V=["UP","MP","South India","West Bengal","Gujrat","Jammu and Kashmir","Punjab","Other"]
	CMB1 = Combobox(top,values=V,textvariable=city)
	CMB1.set("Select your state")
	CMB1.place(x=240,y=403)
	
	def ok():
		if regname.get()=="" or regpass.get()=="" or regcon.get()=="" or regage.get()=="" or regnum.get()=="" or city.get()=="" or M.get()=="" or regpass.get() != regcon.get():
			messagebox.showerror("Error","Fill the form properly and check \nyour entries and password carefull\nTry again ! ")
			
			
		else:
			messagebox.showinfo("Submitted","You have submitted the form successfully\nNow you can login")
			print("Registered Name : "+regname.get())
			print("Registered password : "+regpass.get())
			print("Registered age : "+regage.get())
			print("Registered number : "+regnum.get())
			print("Registered city : "+city.get())
			print("Registered Gender : "+M.get())
			
			top.destroy()
		
	B5 = Button(top,text="Submit",command=ok,font=("algerian",22,"bold"),bg="light green",bd=7)
	B5.place(x=175,y=500)
	
	top.mainloop()
	
B3 = Button(home,command=reg,text="Click here for Register",bg="light blue",relief="flat",font=("algerian",27))
B3.place(x=720,y=300)

def con():
	messagebox.showinfo("Thank you from Garvit Sharma and Saksham Yadav","No terms and conditions are applicable here\nthis is only a example and for making the\nprogram more interactive\nNOTE : This program is made by Garvit Sharma and \nSaksham Yadav it is not copied from any\nprogram or website.")
	
B4 = Button(home,command=con,text="terms and conditions *",bg="light blue",relief="flat",font=("algerian",15))
B4.place(x=560,y=650)
data = StringVar()
x = ""
y = 0
sign=""
def opencal():
	win2 = Toplevel()   #Calculator application
	win2.geometry("580x900")
	win2.title("CALCULATOR")
	win2.configure(bg="black",relief="groove",bd=7)
	F1 = Frame(win2)
	F1.pack(expand=True,fill="both")
	F2 = Frame(win2)
	F2.pack(expand=True,fill="both")
	F3 = Frame(win2)
	F3.pack(expand=True,fill="both")
	F4 = Frame(win2)
	F4.pack(expand=True,fill="both")
	F5 = Frame(win2)
	F5.pack(expand=True,fill="both")
	F6 = Frame(win2)
	F6.pack(expand =True,fill="both")

	E1 = Entry(F1,textvariable=data,font=("Elephant",30),bg="black",fg="lawn green")
	E1.pack(expand=True,fill="both")
	
	def back():
		win2.destroy()
		
	def qt():
		quit()
	
	def bt1():
		global x
		x = x + "1"
		data.set(x)
		
	def bt2():
		global x
		x = x + "2"
		data.set(x)
		
	def bt3():
		global x 
		x = x + "3"
		data.set(x)
		
	def bt4():
		global x 
		x = x + "4"
		data.set(x)
		
	def bt5():
		global x
		x = x + "5"
		data.set(x)
		
	def bt6():
		global x 
		x = x + "6"
		data.set(x)
		
	def bt7():
		global x 
		x = x + "7"
		data.set(x)
		
	def bt8():
		global x 
		x = x + "8"
		data.set(x)
		
	def bt9():
		global x 
		x = x + "9"
		data.set(x)
		
	def bt0():
		global x 
		x = x + "0"
		data.set(x)
		
	def btpl():
		global y
		global sign
		global x
		y = int(x)
		sign="+"
		x = x + "+"
		data.set(x)
	def btmi():
		global y 
		global sign
		global x 
		y = int(x)
		sign="-"
		x = x + "-"
		data.set(x)
		
	def btmu():
		global y
		global sign
		global x
		y = int(x)
		sign ="*"
		x=x+ "*"
		data.set(x)
		
	def btdi():
		global y 
		global sign 
		global x
		y = int(x)
		sign = "/"
		x = x + "/"
		data.set(x)
		
	def btcl():
		global y
		global sign
		global x
		x =""
		y=0
		sign = ""
		data.set(x)
		
	def result():
		global y
		global sign
		global x
		x2 = x
		if sign=="+":
			z = int((x2.split("+")[1]))
			c = y+z
			data.set(c)
			x = str(c)
		elif sign=="-":
			z = int((x2.split("-")[1]))
			c =y-z
			data.set(c)
			x = str(c)
		elif sign=="*":
			z = int((x2.split("*")[1]))
			c = y*z
			data.set(c)
			x = str(c)
		elif sign=="/":
			z = int((x2.split("/")[1]))
			if z ==0:
				messagebox.showerror("Error","Division by zero not supported")
				x =""
				y=""
				data.set(x)
				
			else:
				c = y/z
				data.set(c)
				x = str(c)
				
			
		
	
	B1= Button(F2,command=bt1,text="1",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	B1.pack(side=LEFT,expand=True,fill="both")
	B2 = Button(F2,command=bt2,text="2",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	B2.pack(side=LEFT,expand=True,fill="both")
	B3 = Button(F2,command=bt3,text="3",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	B3.pack(side=LEFT,expand=True,fill="both")
	B4= Button(F2,command=bt4,text="4",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	B4.pack(side=LEFT,expand=True,fill="both")
	B5 = Button(F2,command=bt5,text="5",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	B5.pack(side=LEFT,expand=True,fill="both")
	B6 = Button(F3,command=bt6,text="6",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	B6.pack(side=LEFT,expand=True,fill="both")
	B7 = Button(F3,command=bt7,text="7",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	B7.pack(side=LEFT,expand=True,fill="both")
	B8= Button(F3,command=bt8,text="8",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	B8.pack(side=LEFT,expand=True,fill="both")
	B9 = Button(F3,command=bt9,text="9",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	B9.pack(side=LEFT,expand=True,fill="both")
	B0 = Button(F3,command=bt0,text="0",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	B0.pack(side=LEFT,expand=True,fill="both")
	Bpl= Button(F4,command=btpl,text="+",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	Bpl.pack(side=LEFT,expand=True,fill="both")
	Bmi = Button(F4,command=btmi,text="-",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	Bmi.pack(side=LEFT,expand=True,fill="both")
	Bmu = Button(F4,command=btmu,text="x",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	Bmu.pack(side=LEFT,expand=True,fill="both")
	Bdi= Button(F4,command=btdi,text="/",font=("Elephant",20,"bold"),bd=5,bg="Khaki1")
	Bdi.pack(side=LEFT,expand=True,fill="both")
	Bcl = Button(F4,command=btcl,text="C",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	Bcl.pack(side=LEFT,expand=True,fill="both")
	Bequal = Button(F5,command=result,text="=",font=("Elephant",20,"bold"),bd=5,bg="khaki1")
	Bequal.pack(side=LEFT,expand=True,fill="both")
	
	Bback = Button(F6,command=back,text="Back",font=("Elephant",20,"bold"),bd=5,bg="purple2")
	Bback.pack(side=LEFT)
	
	Bqt = Button(F6,command=qt,text="Quit",font=("Elephant",20,"bold"),bd=5,bg="purple2")
	Bqt.pack(side=RIGHT)
	
	win2.mainloop()
	

	
	

home.mainloop()