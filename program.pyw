import json
import pyperclip
import tkinter as tk

## load emoticons
emoticons = ""
with open("emoticons.json", 'r', encoding="utf8") as fp:
  emoticons = json.load(fp)

## create tkinter window
window = tk.Tk()
# set title and icon
window.wm_title("emoticon paster")
window.iconbitmap("caticon.ico")
# set size and prevent resizing
window.geometry("350x350")
window.resizable(width=False, height=False)
# make it stay on top
window.attributes('-topmost', 'true')

# define font
bigfont = ("Arial", 14)

## create frames
tab_frame = tk.Frame(master=window)
tab_frame.pack(side="top", fill="x", expand=False)

emoticons_frame = tk.Frame(master=window)
emoticons_frame.pack(side="top", fill="both", expand=True)

# the text widget enables automatic "word wrapping" of buttons
# https://stackoverflow.com/questions/69846517/how-to-auto-wrap-widget-in-tkinter
text = tk.Text(master=emoticons_frame, wrap="word")
text.configure(state="disabled", cursor='')
text.pack(fill="both", expand=True)

## load emoticons on selected tab
def select_tab(tab):
  # remove old emoticons
  # https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
  for widget in text.winfo_children():
    widget.destroy()

  # add new emoticons
  for i, emoticon in enumerate(emoticons[list(emoticons)[tab]]):
    button = tk.Button(
        text=emoticon,
        font=bigfont,
        bg="white",
        fg="black",
        # https://stackoverflow.com/a/47296482
        command=lambda e=emoticon: pyperclip.copy(e),
        master=text
    )
    text.window_create("end", window=button)
  
## add tab buttons
for i, title in enumerate(emoticons.keys()):
  tk.Button(
      text=title,
      bg="white",
      fg="black",
      command=lambda tab=i: select_tab(tab),
      master=tab_frame
  ).pack(side="left", fill="both", expand=True)

## initial load
select_tab(0)

window.mainloop()