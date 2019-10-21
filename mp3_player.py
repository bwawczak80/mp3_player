from tkinter import *


def previous():
    print("Previous")


def pause():
    print("Pause")


def play():
    print("Play")


def next_track():
    print("next")


def stop():
    print("stop")


def load():
    print("load")


def back():
    print("back")


def add():
    print("add")


def subtract():
    print("subtract")


main = Tk()
main.geometry("435x600+400+100")
frame = Frame(main)

title_label = Label(main, text="Title:").place(x=20, y=10)
artist_label = Label(main, text="Artist:").place(x=20, y=30)
display_artist = Label(main, text="Artist Placeholder").place(x=100, y=30)
display_title = Label(main, text="Song Placeholder").place(x=100, y=10)
btn_previous = Button(main, text="Prev", command=previous, width=5).place(x=20, y=70)
btn_pause = Button(main, text="Pause", command=pause, width=5, ).place(x=100, y=70)
btn_play = Button(main, text="Play", command=play, width=5, ).place(x=180, y=70)
btn_next = Button(main, text="Next", command=next_track, width=5, ).place(x=260, y=70)
btn_stop = Button(main, text="Stop", command=stop, width=5, ).place(x=340, y=70)
play_list = Listbox(main, width=45, height=20).place(x=10, y=120)
btn_load = Button(main, text="Load", command=load).place(x=20, y=470)
btn_back = Button(main, text="Back", command=back).place(x=80, y=470)
btn_add = Button(main, text="+", command=add).place(x=345, y=470)
btn_subtract = Button(main, text="-", command=subtract).place(x=380, y=470)


main.mainloop()
