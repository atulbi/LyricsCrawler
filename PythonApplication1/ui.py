import tkinter as tk
from tkinter import *
from application import main2



def helloCallBack(ttl_in,art_in,t):
    artist = art_in.get()
    track = ttl_in.get()
    print(track,artist)
    str = main2(track,artist)
    t.configure(state = "normal")
    t.delete(1.0,END)
    t.insert(INSERT,str)
    t.configure(state = "disabled")


def main():
    root = Tk()
    
    #window =Canvas(root,bg = "#03A9F4")
    ttl = Label(root,text="Enter Title Track ",bg = "#673AB7")
    ttl.grid(row = 0,column=0)
    ttl_in = Entry(root,bg="#ECEFF1",width = 40)
    ttl_in.grid(row = 0,column = 1,padx = 5 ,pady=5)
    art = Label(root,text = "Enter Artist Name ",bg = "#673AB7")
    art.grid(row = 1 ,column =0)
    art_in = Entry(root,bg ="#ECEFF1",width = 40)
    art_in.grid(row = 1,column=1,padx = 5 ,pady=5)
    t = Text(root,width = 50)
    t.grid(row =2,column = 0,columnspan=4,padx = 5,pady = 5,sticky = "WE")
    btn = Button(root,text="search",relief="flat",bg = "#B9F6CA",activebackground="#69F0AE",activeforeground="#000000",command = lambda: helloCallBack(ttl_in,art_in,t))
    btn.grid(row =0,column=3,rowspan=2,padx = 4,pady = 4)
    
    
    
    root.configure(background = "#673AB7")
    tk.mainloop()



if __name__=="__main__":
    main()