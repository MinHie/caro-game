from tkinter import *
root = Tk()

root.title('App Tài Xỉu')
root.geometry('650x500')

dice_face = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
dice_label = Label(root, font=("Helvetica", 150))
result_label = Label(root, font=("Helvetica", 40))
result_label1 = Label(root, font=("Helvetica", 40))

radio_button = StringVar()

rb1 = Radiobutton(root, text='con cặc', value = 'Tài', variable = radio_button,  font=("Helvetica", 15))

rb2 = Radiobutton(root, text='cái lồn', value = 'Xỉu', variable = radio_button,  font=("Helvetica", 15))

rb1.pack()
rb2.pack()
def roll():
    import random
    xucXac1 = random.randint(1, 6)
    xucXac2 = random.randint(1, 6)
    xucXac3 = random.randint(1, 6)
    
    dice_label.config(
        text=f'{dice_face[xucXac1 - 1]}{dice_face[xucXac2 - 1]}{dice_face[xucXac3 - 1]}'
    )
    dice_label.pack()
    
    sum = xucXac1 + xucXac2 + xucXac3
    result_label.config(text = 'Tài' if sum > 10 else 'Xỉu',
                        foreground='red' if sum > 10 else 'green')
    result_label.pack()
    
def check():
    global coin
    if radio_button.get() == result_label["text"]:
        coin += 50
        result_text = 'Bạn đã được +50K VNĐ'
        result_fg = 'green'
    else:
        coin -= 50
        result_text = 'Bạn vừa bị -50K VNĐ'
        result_fg = 'red'
    result_label1.config(text=result_text+" \n"+"Tổng tiền hiện có: "+str(coin)+"K VNĐ", foreground=result_fg)
    result_label1.pack()
    
coin = 0
myButton1 = Button(root, text='Quay xúc xắc!', command=lambda : [roll(), check()], foreground="blue")
myButton1.pack()
  
root.mainloop()
