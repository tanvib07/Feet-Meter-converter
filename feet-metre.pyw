from tkinter import Tk,Button,Label,DoubleVar,Entry

window = Tk()
window.title("Length Converter App")
window.configure(background="orange")
window.geometry("400x300")
window.resizable(width=False,height=False)

ft_l = Label(window,text="Feet",bg="black",fg="white",width=20,height=2)
ft_l.grid(column=0,row=0,padx=30,pady=30)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=20)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')

mt_l = Label(window,text="Meter",bg="black",fg="white",width=20,height=2)
mt_l.grid(column=0,row=1,padx=30,pady=30)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=20)
mt_entry.grid(column=1,row=1,pady=10)
mt_entry.delete(0,'end')

def convert():
    if ft_entry.get():
        value = float(ft_entry.get())
        meter = value * 0.3048
        mt_value.set("% .4f" %meter)
    else:
        value = float(mt_entry.get())
        feet = value / 0.3048
        ft_value.set("% .4f" %feet)


def clear():
    ft_value.set("")
    mt_value.set("")

convert_b = Button(window,text="Convert",bg='grey',fg='black',width=15,command=convert)
convert_b.grid(column=0,row=3,padx=40,pady=30)

clear_b = Button(window,text="Clear",bg='grey',fg='black',width=15,command=clear)
clear_b.grid(column=1,row=3,padx=20,pady=30)

window.mainloop()

#To remove the console save the python file as .pyw
#To create .exe file to run the app on any computer install->pyinstaller 
#Then in cmd >>> pyinstaller --onefile filename.pyw