from tkinter import * 
from tkinter import messagebox

wd = Tk()
wd.title("BMI-Calculator")
wd.config(padx=20,pady=20)

def click_button():
    weight = my_entry_1.get()
    height = my_entry_2.get()  

    if weight == "" or height == "":
        snc_label.config(text="Enter both weight and height! ")
    else:
        try:
            bmi = float(weight) / (float(height) /100) ** 2
            snc_label.config(text="BMI: {:.2f}".format(bmi))
            BMI_index(round(bmi,2))
        except:
            snc_label.config(text="Enter a valid number")
    

def BMI_index(bmi):
    if bmi < 18.5:
        index_label.config(text=f'BMI = {bmi} - Zayıf')
    elif 18.5 <= bmi < 24.9:
        index_label.config(text=f'BMI = {bmi} - Normal')
    elif 24.9 <= bmi < 29.9:
        index_label.config(text=f'BMI = {bmi} - Fazla Kilolu')
    else:
        index_label.config(text=f'BMI = {bmi} - Obez')

label_1 = Label(text="Kilonuzu giriniz (kg):")
label_1.pack()

my_entry_1 = Entry(width=30)
my_entry_1.pack()

label_2 = Label(text="Boyunuzu giriniz (cm):")
label_2.pack()

my_entry_2 = Entry(width=30)
my_entry_2.pack()

btn = Button(text="Hesapla", command=click_button)
btn.pack()

snc_label = Label(text="BMI:")
snc_label.pack()

index_label = Label(text="")
index_label.pack()

wd.mainloop()
