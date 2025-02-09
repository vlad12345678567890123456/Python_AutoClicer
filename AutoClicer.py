import tkinter as tk
import pyautogui
import keyboard
import time

def start_autoclicker():
    x = int(entry_x.get())
    y = int(entry_y.get()) 

    pyautogui.moveTo(x, y)

    while True:
        pyautogui.press('f5')  
        time.sleep(1)  

        if keyboard.is_pressed('f6'):
            print("Автокликер остановлен!")
            break

root = tk.Tk()
root.title("Автокликер")

label_x = tk.Label(root, text="Координата X:")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()

label_y = tk.Label(root, text="Координата Y:")
label_y.pack()
entry_y = tk.Entry(root)
entry_y.pack()

start_button = tk.Button(root, text="Запустить автокликер", command=start_autoclicker)
start_button.pack()

root.mainloop()
