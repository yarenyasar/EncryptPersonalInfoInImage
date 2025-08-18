from tkinter import Tk, filedialog, Button, Entry, StringVar
from encryption import fonk
from decryption import fonk1
import tkinter

def character_limit(entry_text, limit):
    if len(entry_text.get()) > limit:
        entry_text.set(entry_text.get()[:limit])

root = tkinter.Tk()
root.title("Encryption & Decryption")

frame1 = tkinter.Frame(root)
frame1_title_label = tkinter.Label(frame1, text="Encryption", font=("Helvetica", 16, "bold","underline"))
frame1_title_label.grid(row=0, column=1, pady=5)
frame1.pack(side=tkinter.LEFT, padx=10, pady=10)

input1_var = StringVar()
input2_var = StringVar()
input3_var = StringVar()

def upload_image():
    file_path = filedialog.askopenfilename()
    input3_var.set(file_path)
    print(file_path)

def process():

    if(len(str(input1_var.get())) == 0):
        tkinter.messagebox.showerror("Error!", "Please input a name.")
        return
    
    if len(str(input2_var.get())) != 11:
        tkinter.messagebox.showerror("Error!", "TC number has to be 11 characters.")
        return
    
    if len(str(input3_var.get())) == 0:
        tkinter.messagebox.showerror("Error!", "Please upload an image.")
        return
    
    save_image(fonk(str(input3_var.get()), str(input1_var.get()), str(input2_var.get())))


input1 = Entry(frame1, textvariable=input1_var)
input1.grid(row=1, column=1, pady=5)
input1_title_label = tkinter.Label(frame1, text="Name&Surname: ", font=("Helvetica", 8), anchor="e", justify="right", width=14)
input1_title_label.grid(row=1, column=0, pady=0)
input1_var.trace("w", lambda *args: character_limit(input1_var, 30))

input2 = Entry(frame1, textvariable=input2_var)
input2_title_label = tkinter.Label(frame1, text="TC Number: ", font=("Helvetica", 8), anchor="e", justify="right", width=14)
input2_title_label.grid(row=2, column=0, pady=0)
input2.grid(row=2, column=1, pady=5)
input2_var.trace("w", lambda *args: character_limit(input2_var, 11))

upload_button = Button(frame1, text="Upload", command=upload_image)
upload_button.grid(row=3, column=1, pady=5)

send_button = Button(frame1, text="Encrypt", command=process)
send_button.grid(row=4, column=1, pady=5)

def save_image(encoded_image):
    input1.delete(0, "end")
    input2.delete(0, "end")
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        encoded_image.save(save_path)

# ------------------------------- frame 2 -------------------------------

def frame_2upload_image():
    file_path = filedialog.askopenfilename()
    output3_var.set(file_path)

output1_var = StringVar()
output2_var = StringVar()
output3_var = StringVar()

def process2():
    if len(str(output3_var.get())) == 0:
        tkinter.messagebox.showerror("Error!", "Please upload an image for decryption.")
        return
        
    save_data(fonk1(str(output3_var.get())))

frame2 = tkinter.Frame(root)
frame2_title_label = tkinter.Label(frame2, text="Decryption", font=("Helvetica", 16, "bold", "underline"))
frame2_title_label.grid(row=0, column=0, pady=5)
frame2.pack(side=tkinter.RIGHT, padx=10, pady=10)

frame2_upload_button = Button(frame2, text="Upload", command=frame_2upload_image)
frame2_upload_button.grid(row=3, column=0, pady=5)

frame2_send_button = Button(frame2, text="Decrypt", command=process2)
frame2_send_button.grid(row=4, column=0, pady=5)

def save_data(data):
    if data:
        output1_var.set(data[0])
        output2_var.set(data[1])

frame2_output = Entry(frame2, textvariable=output1_var)
frame2_output.grid(row=1, column=0, pady=5)

frame2_output2 = Entry(frame2, textvariable=output2_var)
frame2_output2.grid(row=2, column=0, pady=5)


root.resizable(False, False)
root.mainloop()



