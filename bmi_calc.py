from tkinter import *
from tkinter import messagebox

top = Tk()
top.title('BMI Calculator')
top.geometry('500x500')
top.config(bg='#207675')


def reset():
    age.delete(0,'end')
    height.delete(0,'end')
    weight.delete(0,'end')

def calc_bmi():
    kg = int(weight.get())
    m = int(height.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('BMI', f'Alert! BMI = {bmi} is Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI', f"That's Nice! BMI = {bmi} is Normal")
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI', f'Alert! BMI = {bmi} is Overweight')
    elif (bmi > 29.9):
        messagebox.showinfo('BMI', f'Alert! BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('BMI', 'Not Applicable!')   


var = IntVar()

frame = Frame( top, padx=30, pady=30, bd=30 )
frame.pack(expand=True)


age_lb = Label( frame, text="Enter Age (2 - 100)")
age_lb.grid(row=1, column=1)

age_tf = Entry(frame)
age_tf.grid(row=1, column=2, pady=5)

height_lb = Label( frame, text="Enter Height (cm)  ")
height_lb.grid(row=3, column=1)

height = Entry( frame)
height.grid(row=3, column=2, pady=5)

gen_lb = Label( frame, text='Select Gender')
gen_lb.grid(row=2, column=1)

frame2 = Frame( frame)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton( frame2, text = 'Male', variable = var,value = 1)
male_rb.pack(side=LEFT)

female_rb = Radiobutton( frame2, text = 'Female', variable = var, value = 2)
female_rb.pack(side=RIGHT)


weight_lb = Label( frame, text="Enter Weight (kg)  ")
weight_lb.grid(row=4, column=1)

weight = Entry( frame)
weight.grid(row=4, column=2, pady=5)

frame3 = Frame( frame)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3,text='Calculate', command=calc_bmi)
cal_btn.pack(side=LEFT)

reset_btn = Button( frame3, text='Reset', command=reset)
reset_btn.pack(side=LEFT)



top.mainloop()