import tkinter as tk
from tkinter import messagebox




class Text_Write:
    def __init__(self):



        self.window = tk.Tk()
        self.window.title("Never Stop Writing")
        self.window.minsize(width=500, height=600)

        self.after_id = None
        self.text = tk.Text(width=50, height=30)
        self.text.pack(ipady=20, expand=True)
        self.text.bind('<Key>', self.wait)


        self.window.mainloop()


    def wait(self, event):

        if self.after_id is not None:
            tk.Frame().after_cancel(self.after_id)

        self.after_id = tk.Frame().after(5000, self.delete)

    def delete(self):
        self.text.delete(1.0, tk.END)
        messagebox.showinfo(title='You lost everything', message="You just lost everything you wrote. Next time do not stop writing")


















text = Text_Write()










