'''
Created on 28 sep. 2020

@author: Moretti
'''

from pygame import *
from tkinter import *

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('800x300'); window.title('Iris Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        FadeOut = Button(window, text = 'FadeOut', width = 10, font =('Times', 10), command = self.fadeout)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60);FadeOut.place(x=300,y=80)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()    
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
    def fadeout(self):
            mixer.music.fadeout(1500)
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
root = Tk()
app= MusicPlayer(root)
root.mainloop()

