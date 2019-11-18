from tkinter import *
import pygame
from mutagen.mp3 import MP3
import PIL.Image as coverArt
from PIL import Image, ImageTk
import os
from io import BytesIO
import tkinter.messagebox
import requests as req

main = Tk()
main.geometry("450x550+500+20")
frame = Frame(main)
pygame.mixer.init()
pygame.display.init()

title_label = Label(main, text="Title:").place(x=20, y=10)
artist_label = Label(main, text="Artist:").place(x=20, y=30)

display_artist = Label(main, text="")
display_artist.place(x=100, y=30)
display_title = Label(main, text="")
display_title.place(x=100, y=10)
play_list_box = Listbox(main, width=45, height=20)
play_list_box.place(x=10, y=120)


def get_song_list(song_location):
    
    song_list = os.listdir(song_location)
    allFiles = list()
    for song in song_list:
        fullPath = os.path.join(song_location, song)
        allFiles.append(fullPath)
                
    return allFiles
directory = ('/home/pi/Music')
playlist = get_song_list(directory)

def get_details(current_song):
    
    file_data = os.path.splitext(current_song)
    if file_data[1] == '.mp3':
        audio = MP3(current_song)
        artist = audio['TPE1']
        title = audio['TIT2']
        display_artist.config(text=artist)
        display_title.config(text=title)
    else:
        a = pygame.mixer.Sound(current_song)


def previous():
    songs = len(playlist)
    selected_song = play_list_box.curselection()
    selected_song_int = int(selected_song[0])
    
    if selected_song_int > 0:
        pygame.mixer.music.stop()
        next_track = play_list_box.selection_set(selected_song_int - 1,)
        play_list_box.selection_clear(selected_song)
        play()
    
    else:
        pygame.mixer.music.stop()
        next_track = play_list_box.selection_set(len(playlist),)
        play_list_box.selection_clear(selected_song)
        play()

count = 1

def pause():
    
    global count
    if (count % 2) != 0:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    count += 1
    
def play():
    
    try:
        selected_song = play_list_box.curselection()
        selected_song = int(selected_song[0])
        play_selected = playlist[selected_song]
        pygame.mixer.music.load(play_selected)
        pygame.mixer.music.play()
        get_details(play_selected)
        
    except:
        tkinter.messagebox.showerror("Error", "Please select a track")
        

def next_track():
    
    songs = len(playlist)
    selected_song = play_list_box.curselection()
    selected_song_int = int(selected_song[0])
    
    if selected_song_int < songs:
        pygame.mixer.music.stop()
        next_track = play_list_box.selection_set(selected_song_int + 1,)
        play_list_box.selection_clear(selected_song)
        play()
    
    else:
        pygame.mixer.music.stop()
        next_track = play_list_box.selection_set(0,)
        play_list_box.selection_clear(selected_song)
        play()

    
def stop():
    pygame.mixer.music.stop()
    
    
def load():
    
    for x in range(len(playlist)):
        play_list_box.insert(END, playlist[x])
        pygame.mixer.music.queue(playlist[x])
    
    pygame.mixer.music.load( playlist.pop())

        
def subtract():
    try:
        selected_song = play_list_box.curselection()
        selected_song = int(selected_song[0])
        play_list_box.delete(selected_song)
        playlist.pop(selected_song)
    except:
        tkinter.messagebox.showerror("Error", "No song is selected")
    
    
btn_previous = Button(main, text="Prev", command=previous, width=5).place(x=20, y=70)
btn_pause = Button(main, text="Pause", command=pause, width=5, ).place(x=100, y=70)
btn_play = Button(main, text="Play", command=play, width=5, ).place(x=180, y=70)
btn_next = Button(main, text="Next", command=next_track, width=5, ).place(x=260, y=70)
btn_stop = Button(main, text="Stop", command=stop, width=5, ).place(x=340, y=70)
btn_load = Button(main, text="Load", command=load).place(x=20, y=470)
btn_subtract = Button(main, text="-", command=subtract).place(x=380, y=470)

main.mainloop()
