import tkinter as tk 
text_1="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero"
win = tk.Tk()
photo_dog = tk.PhotoImage(file="dog.png") 
win.title("Example - task_4")
win.geometry("300x120") 
l0 = tk.Label(win, image=photo_dog, borderwidth=0)
l1 = tk.Label(win, text="Pochacco!", borderwidth=0)
l2 = tk.Label(win, text=text_1, bg='cyan', heigh=2, borderwidth=0)
l0.place(x=65, y=0)
l1.place(x=150, y=30)
l2.place(x=15, y=80)
win.mainloop()