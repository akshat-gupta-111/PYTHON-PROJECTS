import tkinter as tk
import time
import sys

def countdown_gui(seconds, time_up_flag):
    def update_timer():
        nonlocal seconds
        if seconds > 0:
            label.config(text=f"Time left: {seconds} sec")
            seconds -= 1
            root.after(1000, update_timer)
        else:
            time_up_flag.value = 1
            root.destroy()

    root = tk.Tk()
    root.title("KBC Timer")
    root.geometry("250x100")
    label = tk.Label(root, text="", font=("Helvetica", 16))
    label.pack(expand=True)
    update_timer()
    root.mainloop()

if __name__ == '__main__':
    import multiprocessing
    seconds = int(sys.argv[1])
    flag = multiprocessing.Value('i', 0)
    countdown_gui(seconds, flag)