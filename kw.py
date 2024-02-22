from tkinter import Tk  # Python 3

def extract_keywords(input_text):
    keywords = input_text.split(',')
    return ', '.join(keywords[:20])

#input_text = input('Enter keywords: ')
r = Tk();
clipboard = r.clipboard_get(); 


keywords = extract_keywords(clipboard)

r.clipboard_clear()
r.clipboard_append(keywords)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()

print("\n\nThe first 20 keywords ")
print(keywords)
print("copied to the clipboard")
