from tkinter import *
import statistics


def calculate_key_statistics():
    input_value = textBox.get('1.0', 'end-1c')
    user_list = input_value.split()
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])

    out_text.insert("end", f"{statistics.mean(user_list)}\n")
    out_text.insert("end", f"{statistics.median(user_list)}\n")
    out_text.insert("end", f"{statistics.mode(user_list)}\n")
    out_text.insert("end", f"{statistics.variance(user_list)}\n")
    out_text.insert("end", f"{statistics.stdev(user_list)}\n")
    out_text.insert("end", f"{statistics.pvariance(user_list)}\n")
    out_text.insert("end", f"{statistics.pstdev(user_list)}\n")


root = Tk()
root.geometry('750x400')
root.config(bg='#f5f5f5' )

Main_label=Label(root,text ="Enter your number list below, please leave spaces between your integers",font=("Lato","10"),bg='#008080',fg='white')
Main_label.grid(row=1,column=2)

textBox = Text(root, height=2, width=30)
textBox.grid(row=2,columnspan=5)

b2 = Button(root, height=1, width=7, text="Get stats", command=calculate_key_statistics)
b2.grid(row=3,column=2)

out_text = Text(root, height=7, width=30)
out_text.grid(row=5,column=2)

root.mainloop()