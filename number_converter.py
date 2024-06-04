import tkinter as tk
from threading import Thread
from time import sleep
root=tk.Tk()
t=[]
lb_t=["Int","Bin","Hex","Oct"]
for j,i in enumerate(["Int","Bin","Hex","Oct"]):
    tk.Label(root,text=f"{i}",font=("times new roman",15)).grid(row=j,column=0,pady=5)
    ent=tk.Entry(root)
    ent.grid(row=j,column=1,pady=10,padx=10,sticky="nsew")
    t.append(ent)
for i in range(4):
    root.grid_rowconfigure(i,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=50)
ts={}
print(t)
def ent_vls(v,tt):
    if v==0:
        ts={'Int':tt,'Bin':bin(int(tt))[2:],'hex':hex(int(tt))[2:],'Oct':oct(int(tt))[2:]}
    elif v==1:
        ts={'Int':int(tt,2),'Bin':tt,'hex':hex(int(tt,2))[2:],'Oct':oct(int(tt,2))[2:]}
    elif v==2:
        ts={'Int':int(tt,16),'Bin':bin(int(tt,16))[2:],'hex':tt,'Oct':oct(int(tt,16))[2:]}
    elif v==3:
        ts={'Int':int(tt,8),'Bin':bin(int(tt,8))[2:],'hex':hex(int(tt,8))[2:],'Oct':tt}
    return ts


def ksv(x,i):
    kt=t.index(i)
    if kt==0:
        if x.char not in [str(i) for i in range(10)]:
            i.delete(len(i.get())-1, 'end')
    elif kt == 1:
        if x.char not in ['0','1']:
            i.delete(len(i.get())-1, 'end')
    elif kt == 2:
        if x.char not in [str(i) for i in range(10)]+['a','b','c','d','e','f','A', 'B', 'C', 'D', 'E', 'F']:
            i.delete(len(i.get())-1, 'end')
    else:
        if x.char not in [str(i) for i in range(10)][:8]:
            i.delete(len(i.get())-1, 'end')
    ct = ent_vls(kt,i.get())
    for i in zip(t,ct.values()):
        i[0].delete(0,'end')
        i[0].insert('end',i[1])
        
for i in t:
    i.bind("<KeyRelease>",lambda x,v=i:ksv(x,v))

root.mainloop()


