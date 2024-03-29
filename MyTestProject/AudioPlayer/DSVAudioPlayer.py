import os
import threading
import time
from tkinter import *
import tkinter.messagebox
from tkinter import  filedialog

from tkinter import ttk
from ttkthemes import themed_tk as tk

from mutagen.mp3 import MP3
from pygame import mixer



root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")

# Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
# MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
#
# Styles - normal, bold, roman, italic, underline, and overstrike.

stausbar = ttk.Label(root, text="Welocome To DSV Media Player", relief = SUNKEN, anchor = W, font='times 15 bold')
stausbar.pack(side=BOTTOM, fill = X)

# Create menu bar
menubar = Menu(root)
root.config(menu=menubar)

# Create submenu

playlist = []

# playlist - contains the full path + filename
# playlistbox - contains just the filename
# fullpath + filename is required to play the audio inside the play_music load function

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Open File", command = browse_file)
subMenu.add_command(label="EXIT", command=root.destroy)

def about_us():
    tkinter.messagebox.showinfo('About Us','This is the DSVH audio media player.\n Visit US AT: dsvarietyhub.com\n For More Info\n Created By: NOM ')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="HELP",menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)


mixer.init()  # Initializing The Mixer


root.title('DSVH Audio Player')
root.iconbitmap("images\dsvarietyhublogo1.ico")

# Root Window -- statusbar, leftframe, rightframe
# leftframe - the listbox (playlist)
# Rightframe - Topframe, middleframe and the Buttomframe

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30, pady=30)

playlistbox = Listbox(leftframe)
playlistbox.pack()

addbtn = ttk.Button(leftframe, text="+ ADD", command=browse_file)
addbtn.pack(side=LEFT)

def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)


delbtn = ttk.Button(leftframe, text="- Remove", command=del_song)
delbtn.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(pady=30)

topframe = Frame(rightframe)
topframe.pack()

lengthlabel = ttk.Label(topframe, text='Total Length Of Audio File : --:--', font='times 10 bold')
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text='Current Time Of Audio File : --:--', relief = GROOVE, font='times 10 bold')
currenttimelabel.pack()

def show_details(play_song):

    file_data = os.path.splitext(play_song)

    if file_data[1] == '.mp3':
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a = mixer.Sound(play_song)
        total_length = a.get_length()

    # div = total_length/60, and - total_length, 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length Of Audio File Is:" + timeformat

    t1 =threading.Thread(target=start_count, args=(total_length,))
    t1.start()

def start_count(t):
    global paused
    # mixer.music.get_ busy(): - Returns FALSE when we press the stop button (music stop playing)
    # Continue - Ignores all of the statement below it. we check if music is paused or not.
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current Time Of Audio File Is:" + timeformat
            time.sleep(1)
            current_time += 1

def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        stausbar['text'] = "Music Resumed"
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            stausbar['text'] = "Playing Audio File" + ' - ' + os.path.basename(play_it)
            show_details(play_it)
        except:
            tkinter.messagebox.showerror('File Not Fond','DSVH Media Player Did Not Find Any Audio File\nPlease Select An Audio File And Press Play')

def stop_music():
    mixer.music.stop()
    stausbar['text'] = "Stopped Playing Audio File"

paused = FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    stausbar['text'] = "Paused Playing Audio File"

def rewind_music():
    play_music()
    stausbar['text'] = "Rewind Audio File"

def set_vol(val):
    volume = float(val)/100
    mixer.music.set_volume(volume)
    # set volume of mixer only take value from 0-1 example 0, 0.1 0.55, 0.99, 1

muted = FALSE

def mute_music():
    global muted
    if muted: # UnMute the audio file that is playing
        mixer.music.set_volume(0.7)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = FALSE
    else:  # Mute the audio file that is playing
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = TRUE

middleframe = Frame(rightframe)
middleframe.pack(padx=100, pady=60)

playphoto = PhotoImage(file='images/play-button.png')
playBtn = ttk.Button(middleframe, image = playphoto, command=play_music)
playBtn.grid(row=0, column=0)

stopphoto = PhotoImage(file='images/stop.png')
stopBtn = ttk.Button(middleframe, image = stopphoto, command=stop_music)
stopBtn.grid(row=0, column=1)

pausephoto = PhotoImage(file='images/pause.png')
pauseBtn = ttk.Button(middleframe, image = pausephoto, command=pause_music)
pauseBtn.grid(row=0, column=2)

# Bottom frame volume, Mute, Rewind exct

bottomframe = Frame(rightframe)
bottomframe.pack()

rewindphoto = PhotoImage(file='images/rewind.png')
rewindBtn = ttk.Button(bottomframe, image = rewindphoto, command=play_music)
rewindBtn.grid(row=0, column=0)

mutePhoto = PhotoImage(file='images/mute.png')
volumePhoto = PhotoImage(file='images/volume.png')
volumeBtn = ttk.Button(bottomframe, image = volumePhoto, command=mute_music)
volumeBtn.grid(row=0, column=1)

scale = ttk.Scale(bottomframe,from_=0,to=100,orient_=HORIZONTAL, command=set_vol)
scale.set(70)  # implement the default value of scale when music player starts
mixer.music.set_volume(0.7)
scale.grid(row=0, column=2, pady=15, padx=30)


def on_closing():
    stop_music()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_closing)
root.mainloop()