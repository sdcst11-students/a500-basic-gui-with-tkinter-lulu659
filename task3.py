import tkinter as tk 
text_1="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero"
win = tk.Tk()
photo_dog = tk.PhotoImage(file="dog.png")  
win.title("Example")
win.resizable(False,False)
l0 = tk.Label(win, image=photo_dog, borderwidth=0)
l1 = tk.Label(win, text="Pochacco!", borderwidth=0)
l2 = tk.Label(win, text=text_1, bg='cyan', heigh=2, borderwidth=0)
l0.grid(row=0, column=0, rowspan=3, padx=5, pady=5, sticky='e')
l1.grid(row=1, column=1, padx=5, sticky='w')
l2.grid(row=3, column=0,  ipadx=5, ipady=5, columnspan=2)
win.mainloop()
