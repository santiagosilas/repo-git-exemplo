class Formulario:
    def __init__(self):
        self.StopButton = Button()
	self.PauseButton = Button()
    def next_music(self):
        self.play_song = True
    def play_music(self):
	self.play = True
    def pause_music(self):
	self.pause = True
    def stop_music(self):
        self.stop = True
    def turn_off(self):
	pass
