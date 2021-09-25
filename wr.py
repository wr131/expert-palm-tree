import tkinter as tk #导入thinter
import random
#import tkMessageBox
import tkinter.messagebox #导入messagebox类
from secrets import token_bytes
from typing import Tuple
win=tk.Tk() #生成窗口
win.geometry("256x200")
win.title("Sigh")
#start
#desigh 2 tips
labname=tk.Label(win,text='User name',width=10000,
                 #justify == RIGHT
                 )
labname.pack(
    #side = LEFT
    )
entname=tk.Entry(win,width=10000,
                 #textvariable=var_name
                 )
entname.pack(#"Please input your user name"
    #side = RIGHT
    )
#labname=tk.Label(win.text=='User name:',width=80)
labpassword=tk.Label(win,text='Password',width=80)
labpassword.pack()
entpassword=tk.Entry(win,show="*",width=10000,
                     #textvariable=var_password
                     )
entpassword.pack(#"Please input your password"
    )
def loging():
    var_name=tk.StringVar()
    var_name.set('');
    var_password=tk.StringVar()
    var_password.set('');
    p=random.randint(1,1024)
    p2=random.randint(1024, 2048)
    p3=random.randint(1,5)
    p4=random.randint(1,5)
    name=var_name.get()
    passwordy='131'
    passwordo=var_password.get()
    password=encrypt (passwordo)
    #passwordu=password*p**p4+password*p2**p4
    #passwordt=passwordy*p**p4+password*p2**p4
    passwordt=encrypt (passwordy)
    #name=input("Please enter your name;");
    if name in "petty" and passwordu == passwordt:
        print(passwordt)
        r=tk.messagebox.askokcancel( title="Sigh successfully", message="Sigh successfully")
        r.pack()
        #open(C\Windows\explorer.exe, mode='b')
        #right=tk.Tk()
        #right.titel("Right")
        #labright=tk.Label(right,text='Sigh succesefully.')
        #labright.pack()
    else:
        b=tk.messagebox.askokcancel( title="s", message="s")
        b.pack()
        text.delete(0, END)
but_Ok=tk.Button(win,text="Sigh",width=10000,command=loging
                 #,relief=GROOVE
                 )
but_Ok.pack()
but_Cancel=tk.Button(win,text="Reset",width=10000
                     #,relief=GROOVE
            #,command=cancel
            )
but_Cancel.pack(#side = RIGHT
                )
but_quit=tk.Button(win,text="Quit",width=10000,command=quit
                   #,relief=GROOVE
                   )
but_quit.pack()
win.mainloop()
'''elif name in "mike" and passwordu == passwordt:
        print(passwordt)
        r=tk.messagebox.askokcancel( title="Sigh successfully", message="Sigh successfully")
        r.pack()
        #open(C\Windows\explorer.exe, mode='b')
        #right=tk.Tk()
        #right.titel("Right")
        #labright=tk.Label(right,text='Sigh succesefully.')
        #labright.pack()'''
