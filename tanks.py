from livewires import games
import math

games.init(screen_width = 1300, screen_height = 975, fps = 50)

class Tank(games.Sprite) :
    
    def __init__(self, image, x, y, player) :
        super(Tank,self).__init__(image = image, x = x, y = y)
        self.speed = 0
        self.controle = True
        self.time = 50
        self.player = player
        self.x_last = self.x
        self.y_last = self.y
        self.angle_last = self.angle
        
    def update(self) :        
        self.count_speed()
        self.bound()
        self.player_controle()
        self.colide()
    

    def count_speed(self) :
        direction = (self.angle+180) * math.pi/180
        self.dx = -1*self.speed * math.cos(direction)
        self.dy = -1*self.speed * math.sin(direction)
        
    def bound(self) :
        if self.left < 1 :
            self.speed = 0
            self.left = 2
        if self.right > 1299 :
            self.speed = 0
            self.right = 1298

        if self.top < 51 :
            self.speed = 0
            self.top = 52
        if self.bottom > 974 :
            self.speed = 0
            self.bottom = 973


    def player_controle(self) :


                
        if self.player == 0 :
            if games.keyboard.is_pressed(games.K_UP) :
                self.__speed_up()
            elif games.keyboard.is_pressed(games.K_DOWN) :
                self.__speed_back()
            else :
                self.__speed_break()
                        
            if games.keyboard.is_pressed(games.K_RIGHT) :
                self.__angle_r()            
            elif games.keyboard.is_pressed(games.K_LEFT) :
                self.__angle_l()

            if games.keyboard.is_pressed(games.K_RALT) :
                self.__shoot()
            else :
                self.__next_shoot()


        elif self.player == 1 :
            if games.keyboard.is_pressed(games.K_w) :
                self.__speed_up()
            elif games.keyboard.is_pressed(games.K_s) :
                self.__speed_back()
            else :
                self.__speed_break()
                        
            if games.keyboard.is_pressed(games.K_d) :
                self.__angle_r()            
            elif games.keyboard.is_pressed(games.K_a) :
                self.__angle_l()

            if games.keyboard.is_pressed(games.K_q) :
                self.__shoot()
            else :
                self.__next_shoot()
            
                


                
            
    def __speed_up(self) :
        if self.speed > 0 :
            self.speed -= 0.02
        else :
            self.speed -= 0.02


    def __speed_back(self) :
        if self.speed < 0 :
            self.speed += 0.02
        else :
            self.speed += 0.02


    def __speed_break(self) :
        if self.speed > 0.001 :
            self.speed -= 0.04
        elif self.speed < -0.001 :
            self.speed += 0.04
        else :
            self.speed = 0


        
    def __angle_r(self) :
        self.angle += 1


    def __angle_l(self) :
            self.angle -= 1

                    
                                
                                               
    def __shoot(self) :
        if self.controle == True :
            
            direction = (self.angle + 180) * math.pi/180
            amo_x = 75 * math.cos(direction) + self.x
            amo_y = 75 * math.sin(direction) + self.y

            
            amo_image = games.load_image('amo.xcf', transparent = True)           
            amo = Amo(image = amo_image, x = amo_x, y = amo_y, angle = (self.angle + 90))
            games.screen.add(amo)
            self.controle = False
            self.time = 50

    def __next_shoot(self) :
        self.time -= 1
        if self.time == 0 :
            self.controle = True



    def colide(self) :
        for i in self.overlapping_sprites :
            if type(i) is Tank or type(i) is Objects :
                self.speed = 0
                self.x = self.x_last
                self.y = self.y_last
                self.angle = self.angle_last
        if not self.overlapping_sprites :        
            self.remember_xy()
            self.remember_angle()

    def remember_xy(self) :
        self.x_last = self.x
        self.y_last = self.y

    def remember_angle(self) :
        self.angle_last = self.angle
                


                



class Amo(games.Sprite) :
    
    def __init__(self, image, x, y, angle) :
        super(Amo, self).__init__(image = image, x = x, y = y, angle = angle)
        self.speed = 15

    def update(self) :
        self.cnt_speed()
        self.exist()
        self.colide()
        
    def cnt_speed(self) :
        direction = (self.angle - 90) * math.pi/180
        self.dx = -1*self.speed * math.cos(direction)
        self.dy = -1*self.speed * math.sin(direction)

    def exist(self) :
        if self.x < 0 or self.x > 1300 or self.y < 50 or self.y > 975 :
            self.destroy()

    def colide(self) :
        for i in self.overlapping_sprites :
            if type(i) is Tank or type(i) is Objects:
                explosion_files = ['ex1.xcf', 'ex2.xcf',
                                   'ex3.xcf', 'ex4.xcf',
                                   'ex5.xcf', 'ex6.xcf',
                                   'ex7.xcf', 'ex8.xcf',
                                   'ex9.xcf', 'ex10.xcf',
                                   'ex11.xcf', 'ex12.xcf']

                explosion = games.Animation(images = explosion_files, x = self.x, y = self.y,
                                            n_repeats = 1, repeat_interval = 5, is_collideable = False)
                games.screen.add(explosion)
                self.destroy()
        





class Objects(games.Sprite) :
    def __init__(self, image, x, y) :
        super(Objects,self).__init__(image = image, x = x, y = y)
    
    


wall_image = games.load_image('field_image.xcf', transparent = False)
games.screen.background = wall_image

sherman_image = games.load_image('sherman.xcf', transparent = True)
sherman = Tank(image = sherman_image, x = 400, y = 300, player = 0)
games.screen.add(sherman)

tiger_image = games.load_image('tiger.xcf', transparent = True)
tiger = Tank(image = tiger_image, x = 600, y = 500, player = 1)
games.screen.add(tiger)

stone_image = games.load_image('stone.png', transparent = True)
stone = Objects(image = stone_image, x = 1000, y = 300)
games.screen.add(stone)

games.screen.mainloop()
