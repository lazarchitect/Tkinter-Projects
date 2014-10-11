#calculator.py

#[pi, e, ANSWER BUTTON], [ln(x), sqrt(x), factorial()] 


from tkinter import *
import math

def tetrate(x,y):#repeated exponentiation. 2^^3 = 2^2^2. It's on wikipedia if you want to learn more(it goes deeper).
	if(y>0):
		total = x
		while y>1:
			total = total**x
			y-=1
		return total
	else:
		return x		

def fx(func):
	try:
		answer.set(round(func(float(textfield.get()), float(textfield2.get())),6 ) )
	except OverflowError:
		answer.set("Too big for your shitty processor")	
	except:
		answer.set("Bad Input")

def f(func):	
	try:
		answer.set(round(func(float(textfield.get())),6))
	except OverflowError:
		answer.set("Too big for your shitty processor")
	except:	
		answer.set("Bad Input")
			
def add():
	fx(lambda x,y: x+y)
def sub():
	fx(lambda x,y: x-y)
def mul():
	fx(lambda x,y: x*y)
def div():
	fx(lambda x,y: x/y)
def exp():
	fx(lambda x,y: x**y)
def tet():
	fx(lambda x,y: tetrate(x,y))

def sin():
	f(lambda x: math.sin(math.radians(x)))	
def cos():
		f(lambda x: math.cos(math.radians(x)))	
def tan():
		f(lambda x: math.tan(math.radians(x)))
def csc():
	f(lambda x: 1/(math.sin(math.radians(x))))
def sec():
		f(lambda x: 1/(math.cos(math.radians(x))))	
def cot():
		pass	
def asin():
	pass
def acos():
		pass	
def atan():
		pass					
def acsc():
	pass	
def asec():
		pass	
def atan():
		pass
def sinh():
	pass
def cosh():
		pass	
def tanh():
		pass					
def csch():
	pass	
def sech():
		pass	
def coth():
		pass		
		
#####		
		
def pi_set():
	s1.set(3.14159265359)
	textfield2.focus_set()
def e_set():
	s1.set(2.71828182846)
	textfield2.focus_set()
	
def redefine():
	s1.set(answer.get())
	answer.set("")

###############################################################################################


window = Tk()
window.title("Basic Calculator")
#window["bg"] = "gray"

Label(window, text="x=").grid(row=0,column=0)
s1 = StringVar()
textfield = Entry(window, width = 10, textvariable = s1)
textfield.focus_set()
textfield.grid(row=0,column=1,columnspan=2)

Label(window, text="y=").grid(row=1,column=0)
s2 = StringVar()
textfield2 = Entry(window, width = 10, textvariable = s2)
textfield2.grid(row=1,column=1,columnspan=2)

Button(window, text = "x+y", font = ("Helvetica",16), width = 5, height=2, command = add).grid(row=2,column=0)
Button(window, text = "x-y", font = ("Helvetica",16), width = 5, height=2, command = sub).grid(row=3,column=0)

Button(window, text = "x*y", font = ("Helvetica",16), width = 5, height=2, command = mul).grid(row=2,column=1)
Button(window, text = "x"+u"\u00F7"+"y", font = ("Helvetica",16), width = 5, height=2, command = div).grid(row=3,column=1)

Button(window, text = "x^y", font = ("Helvetica",16), width = 5, height=2, command = exp).grid(row=2,column=2)
Button(window, text = "x^^y", font = ("Helvetica",16), width = 5, height=2, command = tet).grid(row=3,column=2)

Button(window, text = "sin(x)\n(degrees)", font = ("Helvetica",16), width = 7, height=2, command = sin).grid(row=2,column=3)
Button(window, text = "cos(x)\n(degrees)", font = ("Helvetica",16), width = 7, height=2, command = cos).grid(row=3,column=3)

####
Button(window,text=u"\u03C0", font = ("Helvetica",16), width = 2, height = 1, command = pi_set).grid(row=0,column=3)
Button(window,text="e", font = ("Helvetica",16), width = 2, height = 1, command = e_set).grid(row=1,column=3)

answer = StringVar()

stuff = Button(window, textvariable=answer, font=("Helvetica",24), command=redefine)
stuff.grid(row=4,column=0,columnspan=10)


window.mainloop()