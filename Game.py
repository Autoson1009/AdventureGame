class Game():
    def __init__(self):
        self.player = Player()
        self.area = Area("initialArea")


    def play(self):
        self.area.start()
        return


###############################################################################################
# Main Method
###############################################################################################
if __name__ == "__main__":
    g = Game()
    g.play()
