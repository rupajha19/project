from tkinter import*
r=Tk()
r.configure(background="sky blue")
def send():
    send = "you->"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=='hii' or e.get()=='hello' or e.get()=="hi"):
        txt.insert(END,'\n'+'\t'+"Bot-> Hello!, How can we help you?")
    elif (e.get()=='i want to know about navgurukul'):
        txt.insert(END,"\n"+'\t'+"Bot-> sure! Navgurukul is a free software development cours")
    elif (e.get()=='how many year is cours'):
        txt.insert(END,"\n"+'\t'+"Bot-> one year cours")
    elif (e.get()=='what are the language you are teaching'):
        txt.insert(END,"\n"+'\t'+"PYTHON, JAVASCRIPT,HTML CSS")
    elif (e.get()=='Thank you'):
        txt.insert(END,"\n"+'\t'+"Bot-> do visit again")
    else:
        txt.insert(END,"\n"+'\t'"Bot-> sorry i didn'n get you?")
    e.delete(0,END)
txt = Text(r)
txt.grid(row=0,column=0)
e=Entry(r,width=80,bg="pink",fg="red")
send=Button(r,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
r.title("CHATBOT")
r.mainloop()

