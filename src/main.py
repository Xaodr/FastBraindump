import tkinter as tk
from datetime import datetime

def append_to_braindump(text, file_path):
    today_date = datetime.now().strftime("%d.%m.%Y")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        existing_content = file.read()
    
    if today_date not in existing_content:
        existing_content += f"[ {today_date} ]\n"
    
    if text.startswith("TODO:"):
        formatted_text = f"- [ ] {text}\n"
    else:
        formatted_text = f"- {text}\n"
    
    existing_content += formatted_text

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(existing_content)

def on_submit(event=None):
    text = text_entry.get()
    if text:
        append_to_braindump(text, braindump_file_path)
        text_entry.delete(0, tk.END) 
    root.destroy() 

braindump_file_path = "C:\\tmp\\X\\Braindump.md"

root = tk.Tk()
root.title("Braindump")

root.overrideredirect(True)

root.attributes('-alpha', 0.95)

root.configure(bg="#0F0F0F")
entry_frame = tk.Frame(root, bg="#0F0F0F")
entry_frame.pack(pady=10, padx=20)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 500
window_height = 50
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

text_entry = tk.Entry(entry_frame, bg="#0F0F0F", fg="white", insertbackground="white", width=60, bd=0, font=('Roboto Mono', 20))
text_entry.pack()
text_entry.focus_set()

root.bind("<Return>", on_submit)

def on_motion(event):
    x, y = root.winfo_pointerxy()
    root.geometry(f"+{x - click_x}+{y - click_y}")

click_x, click_y = 0, 0
def on_click(event):
    global click_x, click_y
    click_x, click_y = event.x, event.y

root.bind('<Button-1>', on_click)
root.bind('<B1-Motion>', on_motion)

root.mainloop()
