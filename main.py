from cProfile import label
import tkinter as tk
from tkinter import filedialog , messagebox

#main window code
root = tk.Tk()
root.title("simple test editor")
root.geometry("800x600")

#creating text area
text = tk.Text(
    root,
    wrap = tk.WORD,
    font =("Helvetika" ,12)
)

text.pack(expand=True  ,fill=tk.BOTH)

#main logic 
#function to create a new file
def new_file():
   text.delete(1.0,tk.END)

 #function to open new file
def open_file():
   #open file dialogue
  file_path=filedialog.askopenfilename(
     defaultextension=".txt",
     filetypes=[("Text Files","*.txt")]
  )  

  if file_path:
     #open selected file
    with open(file_path,"r") as file:
        text.delete(1.0,tk.END)
        text.insert(tk.END,file.read())

  # save function
def save_file():
        file_path= filedialog.asksaveasfilename(
           defaultextension=".txt",
           filetypes=[("Text files","*.txt")]
        )

        if file_path:
           with open(file_path,"w") as file:
              file.write(text.get(1.0,tk.END))

        messagebox.showinfo("info","File saved successfully")

  #menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)

  # file , open , exit , save  , new 
  # add file menu bar 
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New",command=new_file)   
file_menu.add_command(label="Open",command=open_file)             
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit) 

                 
     

#start and keep the window open
root.mainloop()