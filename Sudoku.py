import tkinter as tk
import random
root=tk.Tk()
root.title("Sudoku")
root.geometry("400x410")
mnf1=[]
for i in range(3):
    f=tk.Frame(root,bd=1,relief="sunken")
    f.pack(expand=True,fill='both')
    mnf1.append(f)
mnf2={i:[] for i in mnf1}
for i in mnf1:
    for j in range(3):
        f=tk.Frame(i,bd=1,relief="sunken")
        f.pack(expand=True,fill='both',side="left")
        mnf2[i].append(f)
gbl=None
def mk_bt(bt):
    global gbl
    gbl=bt
lbs=[]

def fnd_dupl(lst):
    indx={}
    for j,i in enumerate(lst):
        if i in indx:
            indx[i].append(j)
        else:
            indx[i]=[]
    indx={j:i for j,i in indx.items() if i!=[]}
    return indx
for i in mnf2.values():
    for m in i:
        for j in range(3):
            m.grid_rowconfigure(j,weight=1)
            m.grid_columnconfigure(j,weight=1)
            for k in range(3):
                f=tk.Label(m,text=f"{random.randint(1,9)}",relief="groove")
                f.grid(row=j,column=k,sticky='nsew')
                f.bind("<Button-1>",lambda x,y=f:mk_bt(y))
                lbs.append(f)
def ct(e):
    global gbl
    v =e.keysym
    #print(v,gbl.config(text=v))
    if v in [str(i) for i in range(10)]:
        gbl.config(text=v)
clr_v=0

def chk_horz(gp=0):
    global clr_v
    nlst = [[[k for k in j.winfo_children()] for j in i.winfo_children()] for i in mnf1]
    n1lst=[[[j[(k-1)*3:k*3] for k in range(1,4)] for j in i] for i in nlst]
    cct = [[[j[k] for j in i] for k in range(3)] for i in n1lst]
    kt2=[[j[0]+j[1]+j[2] for j in i] for i in cct]
    for i in kt2:
        for j in i:
            et=[int(i.cget("text")) for i in j]
            lmn = fnd_dupl(et)
            for lm,l in enumerate(j):
                if clr_v==0:
                    l.config(bg="#DDFDFF",relief="ridge")
                else:
                    l.config(bg="#eeeeee",relief="groove")
                if lm in [i[0] for i in lmn.values()]:
                    l.config(fg="red")
                root.update()
                root.after(gp)
    clr_v^=1
def chk_vert(gp=0):
    global clr_v
    nlst=[[i.winfo_children()[k] for i in mnf1] for k in range(3)]
    cnt=[]
    for i in nlst:
        for j in i:
            ct = [k for k in j.winfo_children()]
            kt=[ct[(i-1)*3:i*3] for i in range(1,4)]
            kkt=[[j[i] for j in kt] for i in range(3)]
            cnt.append(kkt)
    ct=[[j[i] for j in cnt] for i in range(3)]
    kt=[[k[(i-1)*3:i*3] for i in range(1,4)] for k in ct]
    kt1=[[kt[j][i] for j in range(3)] for i in range(3)]
    kt2=[[j[0]+j[1]+j[2] for j in i] for i in kt1]
    for i in kt2:
        for j in i:
            et=[int(i.cget("text")) for i in j]
            lmn = fnd_dupl(et)
            
            for lm,l in enumerate(j):
                if clr_v==0:
                    l.config(bg="#DDFDFF",relief="ridge")
                else:
                    l.config(bg="#eeeeee",relief="groove")
                if lm in [i[0] for i in lmn.values()]:
                    l.config(fg="red")
                root.update()
                root.after(gp)
    clr_v^=1

def chk_v():
    vts=[]
    for i in lbs:
        cm = [i.grid_info()[j] for j in ['in','column','row']]
        tm=cm[0]
        m_ind=[(mnf1.index(i),j.index(tm)) for i,j in mnf2.items() if tm in j][0] if [i for i,j in mnf2.items() if tm in j]!=[] else -1
        vts.append((m_ind[0],m_ind[1],cm[1],cm[2],int(i.cget('text'))))
    cells=[[[int(i.cget('text')) for i in j.winfo_children()] for j in k] for k in mnf2.values()]
    cnt=1
    [i.config(fg='black') for i in lbs]
    for i in enumerate(cells):
        for j in enumerate(i[1]):
            cnt+=1
            for k in fnd_dupl(j[1]).values():
                root.winfo_children()[i[0]].winfo_children()[j[0]].winfo_children()[k[0]].config(fg='red')
                root.update()
    chk_vert()
    root.after(100)
    chk_vert()
    root.after(100)
    chk_horz()
    root.after(100)
    chk_horz()
root.bind("<KeyPress>",ct)
bt=tk.Button(root,text="Check",command=chk_v)
bt.pack(fill="x")

root.mainloop()