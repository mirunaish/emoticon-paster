# emoticon paster

simple app for copy-pasting emoticons

## Instructions

1. Install dependencies

```
pip install pyperclip
```

2. Add your emoticons to the [emoticons.json](emoticons.json) file:

```
{
  "tab 1 title": ["emoticon 1", "emoticon 2"],
  "tab 2 title": ["emoticon 3", "emoticon 4"]
}
```

3. Run [program.py](program.py)
4. Switch tabs using the buttons at the top
5. Click on any emoticon to copy it to the clipboard
6. Paste it anywhere

## Implementation notes

### "Word" wrapping

A grid layout is not ideal in this case because the emoticons may be very different sizes and may not fit in their cells or may change the size of the entire column. In order to make sure all buttons fit nicely with minimal empty space, they are placed inside a `Text` widget which "wraps" buttons onto the next line if they don't fit.

## Tech Stack

- Python
- Tkinter
- JSON
- pyperclip

## Sources

- Documentation
  - https://docs.python.org/3.9/library/tkinter.ttk.html
- StackOverflow
  - https://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard
  - https://stackoverflow.com/questions/69846517/how-to-auto-wrap-widget-in-tkinter
  - https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
  - https://stackoverflow.com/a/47296482
  - others
