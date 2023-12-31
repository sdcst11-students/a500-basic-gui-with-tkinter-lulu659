import tkinter as tk 
win = tk.Tk()
photo_dog = tk.PhotoImage(file="dog.png") 
win.title("T-Town Veterinary Clinic Database")
win.resizable(False,False)
l0 = tk.Label(win, image=photo_dog, borderwidth=0)  
l1 = tk.Label(win, text="Name", borderwidth=0)
l2 = tk.Label(win, text="Type", borderwidth=0)
l3 = tk.Label(win, text="Breed", borderwidth=0)
l4 = tk.Label(win, text="Owner", borderwidth=0)
l5 = tk.Label(win, text="Birthdate", borderwidth=0)
l6 = tk.Label(win, text="Search by Name", borderwidth=2, relief='groove')
l7 = tk.Label(win, text="Client Database", borderwidth=0)
e1 = tk.Entry(win, borderwidth=1)
e2 = tk.Entry(win, borderwidth=1)
e3 = tk.Entry(win, borderwidth=1)
e4 = tk.Entry(win, borderwidth=1)
e5 = tk.Entry(win, borderwidth=1)
e6 = tk.Entry(win, borderwidth=1)
b0 = tk.Button(win, text="Save Entry")
b1 = tk.Button(win, text="< Previos", background='white')
b2 = tk.Button(win, text="Next >", background='white')
l0.grid(row=0, column=0, rowspan=3, padx=5, pady=5)
l1.grid(row=3, column=0)
l2.grid(row=3, column=1)
l3.grid(row=3, column=2)
l4.grid(row=3, column=3)
l5.grid(row=3, column=4)
e1.grid(row=4, column=0, padx=5, pady=5)
e2.grid(row=4, column=1, padx=5, pady=5)
e3.grid(row=4, column=2, padx=5, pady=5)
e4.grid(row=4, column=3, padx=5, pady=5)
e5.grid(row=4, column=4, padx=5, pady=5)
l6.grid(row=0, column=3, sticky='e')
e6.grid(row=0, column=4)
l7.grid(row=1, column=2)
b0.grid(row=5, column=2, ipadx=5, ipady=5)
b1.grid(row=5, column=0, sticky='w')
b2.grid(row=5, column=4, sticky='e')
win.mainloop()