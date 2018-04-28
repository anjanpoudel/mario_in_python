class Gumba():
    # print("Gumba class flag 1")

    # def __init__(self):
    def __init__(self):
        # print("Gumba class flag 2")
        # print("The constructor is running, gumba class")
        self.x = 500;
        self.y = 350;
        self.width = 60;
        self.hight = 95;
        # self.gumba_img = pygame.image.load("gumba_img")
        self.collide = False;
        self.gumba_speed = 3;

    def update(self):
        if self.collide == True:
            self.gumba_speed = self.gumba_speed * -1
            self.collide = False

        self.x+=self.gumba_speed

    # print("Gumba class flag 3")
