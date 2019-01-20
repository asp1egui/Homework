import tkinter as gui

window=gui.Tk()
window.geometry("354x460")
window.resizable(False, False)
window.title("Calculator")
windowlabel = gui.Label(window,text="Calculator",bg='White')
windowlabel.pack(side=gui.TOP)

textinput=gui.StringVar()
operator=""
result=""

#here the numbers from the buttons are added to the operator
def clickbut(numbers):
     global operator
     operator=operator+str(numbers)
     textinput.set(operator)
#this evaluate the numbers and operators and give the result to textinput so windowtext can show the result
def equalbut():
     global operator
     global result
     result=str(eval(operator))
     textinput.set(result)
     operator=""

#this empty the variable textinput
def clrbut():
     textinput.set("")
#if result is empty set the variable textinput to 0 
#if not set textinput to the previous result
def ans():
    if result != '':
        clickbut(result)
    else:
        clickbut("0")

#the explanation is on this link 
#https://i.kym-cdn.com/photos/images/original/001/365/839/24d.png

windowtext=gui.Entry(window,textvar=textinput,width=25,bd=5,bg='powder blue')
windowtext.pack()

but1=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1")
but1.place(x=10,y=100)

but2=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2")
but2.place(x=10,y=170)

but3=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3")
but3.place(x=10,y=240)

but4=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4")
but4.place(x=75,y=100)

but5=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5")
but5.place(x=75,y=170)

but6=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6")
but6.place(x=75,y=240)

but7=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7")
but7.place(x=140,y=100)

but8=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8")
but8.place(x=140,y=170)

but9=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9")
but9.place(x=140,y=240)

but0=gui.Button(window,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0")
but0.place(x=10,y=310)

butdot=gui.Button(window,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".")
butdot.place(x=75,y=310)

butad=gui.Button(window,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"))
butad.place(x=205,y=100)

butsub=gui.Button(window,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"))
butsub.place(x=205,y=170)

butml=gui.Button(window,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"))
butml.place(x=205,y=240)

butdiv=gui.Button(window,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"))
butdiv.place(x=205,y=310)

butclear=gui.Button(window,padx=14,pady=70,bd=4,bg='white',text="CE",command=clrbut)
butclear.place(x=270,y=100)

butequal=gui.Button(window,padx=151,pady=14,bd=4,bg='white',command=equalbut,text="=")
butequal.place(x=10,y=380)

ansbut=gui.Button(window,padx=14,pady=20,bd=4,bg='white',command=ans,text="ans")
ansbut.place(x=265,y=300)

window.mainloop()

