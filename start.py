import Tkinter, tkFileDialog
from MusicPlusOne import doHarmonization, streamToMidi
import sys

root = Tkinter.Tk()
root.geometry("185x260+100+100")
filename=""
quality = Tkinter.IntVar(root)
quality.set(0)
key = Tkinter.StringVar(root)
key.set("C")
keyOptions = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]

def chooseFile():
    global filename
    filename = tkFileDialog.askopenfilename(title="Please Choose a MIDI File")
    fileDisplay.config(text = str(filename))

def harmonize():
    score1 = doHarmonization(filename, key.get(), quality.get())
    score1.show('musicxml')
    # root.destroy()

def export():
    doHarmonization(filename, key.get(), quality.get())
    index = len(filename) - filename[::-1].index('/')
    newfilename = filename[index:]
    streamToMidi(newfilename)

root.title("Music Plus One")
title = Tkinter.Label(root, text = "Harmonizer", font = "Avenir 20")
title.pack()

loadFile = Tkinter.Button(root, text = "Choose File", command = chooseFile)
loadFile.pack()

fileDisplay = Tkinter.Label(root, text = "No file chosen", font = "Avenir", wraplength="175")
fileDisplay.pack()

# maybe when file is selected, use music21 guess key fcn and auto set?
keyselection = Tkinter.OptionMenu(root, key, *keyOptions)
keyselection.pack()

button1 = Tkinter.Radiobutton(root, text="Major", padx = 20, variable=quality, value=0)
button1.pack()
button2 = Tkinter.Radiobutton(root, text="Minor", padx = 20, variable=quality, value=1)
button2.pack()

exportbutton = Tkinter.Button(root, text = "Export to MIDI", command = export)
exportbutton.pack()

if len(sys.argv) > 1 and sys.argv[1] == "debug":
    harmonizebutton = Tkinter.Button(root, text = "DEBUG: Hrmnize", command = harmonize)
    harmonizebutton.pack(ipady="3")

root.mainloop()
