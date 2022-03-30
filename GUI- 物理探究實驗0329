import tkinter as tk
import math

def update4(v1):
    label.configure(text=f"實際距離為 {scale.get()}公分.")
    label1.configure(text=f"入射度為 {(float(scale1.get())*0.05)}度.")
    label2.configure(text=f"鏡子厚度為{float(scale2.get())*0.2}公分.")
    label3.configure(text=f"折射率為 {float(scale3.get())*0.05-2}.")
    dis =scale.get()
    arg=scale1.get()*0.05
    thick =scale2.get()*0.2
    rate=scale3.get()*0.05-2
    parta = math.tan(math.degrees(arg)) * (dis - thick)
    partb = rate * math.sin(math.degrees(arg)) * thick
    partc = parta + partb
    partd = 1 / (math.tan(math.degrees(arg)))
    label4.configure(text=f" 視距離{float(partc*partd)}公分.")
root = tk.Tk()
root.wm_title("Scale Demo")
font = ('Courier New', 20, 'bold')

select = tk.IntVar()
scale = tk.Scale(label='距離', font=font, orient=tk.HORIZONTAL, showvalue=False,bg='blue', fg='white', tickinterval=20, length=800, width=30,troughcolor='yellow', variable=select, command=update4)
scale.grid(row=0, column=0)

select1 = tk.IntVar()
scale1 = tk.Scale(label='折射角', font=font, orient=tk.HORIZONTAL, showvalue=False,bg='blue', fg='white', tickinterval=0.1, length=800, width=30,troughcolor='yellow', variable=select1, command=update4)
scale1.grid(row=2, column=0)

select2 = tk.IntVar()
scale2 = tk.Scale(label='厚度', font=font, orient=tk.HORIZONTAL, showvalue=False,bg='blue', fg='white', tickinterval=0.1, length=800, width=30,troughcolor='yellow', variable=select2, command=update4)
scale2.grid(row=4, column=0)

select3 = tk.IntVar()
scale3 = tk.Scale(label='折射率', font=font, orient=tk.HORIZONTAL, showvalue=False,bg='blue', fg='white', tickinterval=0.1, length=800, width=30,troughcolor='yellow', variable=select3, command=update4)
scale3.grid(row=6, column=0)

label = tk.Label(text='', width=40, font=font)
label.grid(row=1, column=0)
label1 = tk.Label(text='', width=40, font=font)
label1.grid(row=3, column=0)
label2 = tk.Label(text='', width=40, font=font)
label2.grid(row=5, column=0)
label3 = tk.Label(text='', width=40, font=font)
label3.grid(row=7, column=0)
label4 = tk.Label(text='', width=40, font=font)
label4.grid(row=9, column=0)
root.mainloop()
