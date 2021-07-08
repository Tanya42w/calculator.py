from tkinter import *
root=Tk()
root.title("calculator")
root.configure(bg="grey80")
root.iconbitmap("C:/python/projects/accessories_calculator.ico")
expression=""
#creating entry widget  
val=StringVar()    
entry=Entry(root,textvariable=val,width=24,
            justify="right",bd=8,relief="sunken",font=("arial",25))
entry.grid(columnspan=4,row=0)
labelerror=Label(root,text="",fg="red",bg="grey80",font=("helvativa",15))
labelerror.grid(row=1,column=2,columnspan=2,sticky=E)
#fuction for buttons
def ans(num):
    global expression
    global labelerror
    labelerror.configure(text="")
    if num=="clear":
        val.set("")
    elif num=="Del":
        ex=entry.get()
        expression=expression[:-1]
        val.set(ex[:-1])        
    elif num=="=":
        try:            
            result=eval(entry.get())
            expression=str(result)
            val.set(expression)
        except:
            labelerror.configure(text="wrong entry")        
    else:
        expression=expression+num
        val.set(expression)
#creating buttons  
global lists
for i in range(5):
    lists=[["clear","Del","-","+"],
           ["7","8","9","*"],
           ["4","5","6","/"],
           ["1","2","3","="],
           [".","0","(",")"]]    
    for j in range(4):        
        seven=Button(root,text=lists[i][j],bg="grey80",height=3,width=7,
                     font=("arial",19),command=lambda x=lists[i][j] : ans(x))     
        seven.grid(row=i+2,column=j)
root.mainloop()
