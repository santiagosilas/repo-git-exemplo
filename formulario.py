class Formulario:
    def __init__(self):
        self.StopButton = Button()
	self.PauseButton = Button()
    def pause_music(self):
	self.pause = True
    def stop_music(self):
        self.stop = True
