class Mario():
    # -----------------------------
    # constructor
    # ----------------------------
    def __init__(self):
        self.x = 100
        self.y = 355
        self.vert_vel = -12.3
        self.prev_x = 0
        self.prev_y = 0
        self.width = 60
        self.hight = 95
        self.mario_pos = 0;

    #------------------------------
    #Update function for mario
    #-------------------------------
    def update(self):
        self.mario_pos = self.mario_pos + 1;
        self.vert_vel += 2.2
        self.y += self.vert_vel

        if self.y > 355:
            self.vert_vel = 0.0
            self.y = 355


    def move_front(self):
        self.x += 8

    def move_back(self):
        self.x -= 8

    #
    # def fire(self):
    #     print("Oops, I am supposed to fire ")

    def remember_state(self):
        self.prev_x = self.x
        self.prev_y = self.y

    def get_out_of_tube(self,tube):
        self.t = tube
        if self.x + self.width > self.t.x  and self.prev_x <= self.t.x:
            self.x = self.t.x - self.t.width

        elif self.x < self.t.x + self.t.width  and self.prev_x >= self.t.x + self.t.width:
            self.x = self.t.x + self.t.width

        elif self.y + self.hight > self.t.y and self.prev_y <= self.t.y:
            self.y = self.t.y - self.hight - 2

        elif self.y - self.hight < self.t.y + self.t.hight and self.prev_y - self.hight >= self.t.y + self.t.hight:
            self.y = self.t.y + self.t.hight + self.hight

        else:
            print ("How did I get into tube")
    # -----------------------------
    # function that makes a mario to jump
    # ----------------------------
    def mario_jump(self):
        self.y = self.y - 50

    def get_mario_pos(self):
        return self.mario_pos % 5

# mario1 = Mario()
# # mario1.move_front()
# # mario1.move_back()
# # mario1.mario_jump()
# # mario1.update()
# # mario1.does_collide()
# # mario1.get_out_of_tube()
