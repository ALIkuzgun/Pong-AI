import pygame

class Ball():
    def __init__(self,x,y,en,boy,speed):        
        self.image = pygame.image.load('ball.png') 
        self.x = x
        self.y = y
        self.en = en
        self.boy = boy
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.hit_direction = "left"
        self.direction = "left"

    def move(self):
        if self.hit_direction == "right":
            self.rect.x += self.speed
            self.rect.y += self.speed
            self.direction = "right"
        elif self.hit_direction == "left":
            self.rect.x -= self.speed
            self.rect.y += self.speed
            self.direction = "left"
        elif self.hit_direction == "up":
            self.rect.x += self.speed
            self.rect.y -= self.speed
            self.direction = "up"
        elif self.hit_direction == "down":
            self.rect.x -= self.speed
            self.rect.y -= self.speed
            self.direction = "down"

        if self.rect.y <= 0 :
            if self.direction == "down":
              self.hit_direction = "left"  
            if self.direction == "up":
              self.hit_direction = "right"  
        elif self.rect.y >= height - self.boy :
            if self.direction == "left":
              self.hit_direction = "down"  
            if self.direction == "right":
              self.hit_direction = "up"  

    def limit_hit(self):
        global p1_score, p2_score
        if self.rect.x <= 0:
            self.rect.x = width//2
            self.rect.y = height//2
            p2_score += 1
            self.direction = "right"
            self.hit_direction = "right"
        if self.rect.x >= width-self.en:
            self.rect.x = width//2
            self.rect.y = height//2
            p1_score += 1
            self.direction = "left"
            self.hit_direction = "left"

    def draw(self):
        ekran.blit(self.image,self.rect)

    def update(self):
        self.draw()
        self.move()
        self.limit_hit()

class Player_Computer():
    def __init__(self,x,y,en,boy,speed):        
        self.x = x
        self.y = y
        self.en = en
        self.boy = boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.speed = speed

    def move(self):
        if ball.rect.y < self.rect.y + self.boy:
            self.rect.y -= self.speed
        elif ball.rect.y > self.rect.y:
            self.rect.y += self.speed

        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + self.boy >= height:
            self.rect.y = height - self.boy

    def ball_hit(self):
        if self.rect.colliderect(ball.rect):
            if self.rect.x+16>=ball.rect.x+ball.en:
                if ball.direction == "up":
                    ball.hit_direction = "down"
                elif ball.direction == "down":
                    ball.hit_direction = "up"
            if sound_on == 1:
              ses.play()

    def draw(self):
        pygame.draw.rect(ekran,(0,0,0),self.rect)

    def update(self):
        self.draw()
        self.move()
        self.ball_hit()

class Player():
    def __init__(self,x,y,en,boy):        
        self.x = x
        self.y = y
        self.en = en
        self.boy = boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)

    def move(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_UP]:
            self.rect.y -= 5
        elif key[pygame.K_DOWN]:
            self.rect.y += 5

        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + self.boy >= height:
            self.rect.y = height - self.boy

    def ball_hit(self):
        if self.rect.colliderect(ball.rect):
            if self.rect.x+16<=ball.rect.x:
                if ball.direction == "left":
                    ball.hit_direction = "right"
                elif ball.direction == "down":
                    ball.hit_direction = "up"
            if sound_on == 1:
              ses.play()

    def draw(self):
        pygame.draw.rect(ekran,(0,0,0),self.rect)

    def update(self):
        self.draw()
        self.move()
        self.ball_hit()

pygame.init()

width = 900
height = 600 

ekran = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.Font(None,100)

player = Player(20,200,32,96)
player_computer = Player_Computer(width-52,100,32,96,5)

ball = Ball(200,100,32,32,5)

ses = pygame.mixer.Sound("pong_ses.wav")

p1_score = 0
p2_score = 0

play = 0
play_color = (0,0,0)
sound_color = (0,0,0)
df_color = (0,0,0)
exit_color = (0,0,0)
menu_color = (0,0,0)
on_color = (0,0,0)
off_color = (0,0,0)
dff_color = (0,0,0)
md_color = (0,0,0)

text_play_button = pygame.Rect(390, 240, 110, 36)
text_df_button = pygame.Rect(330, 340, 244, 36)
text_sound_button = pygame.Rect(370, 440, 150, 36)
text_exit_button = pygame.Rect(390, 540, 106, 36)
text_on_button = pygame.Rect(405, 260, 60, 36)
text_off_button = pygame.Rect(401, 340, 66, 36)
text_menu_button = pygame.Rect(380, 480, 116, 36)
text_dff_button = pygame.Rect(360, 340, 164, 36)
text_md_button = pygame.Rect(370, 260, 138, 36)

sound = 0
sound_on = 1
sound_off = 0

difficulty = 0

def sound_menu():
    font2 = pygame.font.Font(None, 62)
    font3 = pygame.font.Font(None, 200)

    text_menu = font3.render('MENU', True, (0,0,0))
    ekran.blit(text_menu, (250, 30))

    text_on = font2.render('On', True, on_color)
    ekran.blit(text_on, (405, 260))
    text_off = font2.render('Off', True, off_color)
    ekran.blit(text_off, (401, 340))
    text_menu = font2.render('Menu', True, menu_color)
    ekran.blit(text_menu, (380, 480))

def df_menu():
    font2 = pygame.font.Font(None, 62)
    font3 = pygame.font.Font(None, 200)

    text_menu = font3.render('MENU', True, (0,0,0))
    ekran.blit(text_menu, (250, 30))

    text_md = font2.render('Middle', True, md_color)
    ekran.blit(text_md, (370, 260))
    text_df = font2.render('Difficult', True, dff_color)
    ekran.blit(text_df, (360, 340))
    text_menu = font2.render('Menu', True, menu_color)
    ekran.blit(text_menu, (380, 480))

def menu():
    font2 = pygame.font.Font(None, 62)
    font3 = pygame.font.Font(None, 200)

    text_menu = font3.render('MENU', True, (0,0,0))
    ekran.blit(text_menu, (250, 30))

    text_play = font2.render('PLAY', True, play_color)
    ekran.blit(text_play, (390, 240))
    text_df = font2.render('DIFFICULTY', True, df_color)
    ekran.blit(text_df, (330, 340))
    text_sound = font2.render('SOUND', True, sound_color)
    ekran.blit(text_sound, (370, 440))
    text_exit = font2.render('EXIT', True, exit_color)
    ekran.blit(text_exit, (390, 540))
    
run = True
while run:
    mouse_pos = pygame.mouse.get_pos()
    if text_play_button.collidepoint(mouse_pos):
        play_color = (255,255,255)
    else:
        play_color = (0,0,0)
    if text_sound_button.collidepoint(mouse_pos):
        sound_color = (255,255,255)
    else:
        sound_color = (0,0,0)
    if text_df_button.collidepoint(mouse_pos):
        df_color = (255,255,255)
    else:
        df_color = (0,0,0)
    if text_exit_button.collidepoint(mouse_pos):
        exit_color = (255,255,255)
    else:
        exit_color = (0,0,0)
    if text_on_button.collidepoint(mouse_pos):
        on_color = (255,255,255)
    else:
        on_color = (0,0,0)
    if text_off_button.collidepoint(mouse_pos):
        off_color = (255,255,255)
    else:
        off_color = (0,0,0)
    if text_menu_button.collidepoint(mouse_pos):
        menu_color = (255,255,255)
    else:
        menu_color = (0,0,0)
    if text_dff_button.collidepoint(mouse_pos):
        dff_color = (255,255,255)
    else:
        dff_color = (0,0,0)
    if text_md_button.collidepoint(mouse_pos):
        md_color = (255,255,255)
    else:
        md_color = (0,0,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if sound == 0 and difficulty == 0:
                if text_play_button.collidepoint(event.pos):
                  play = 1
                  sound = 0

                if text_sound_button.collidepoint(event.pos):
                   sound = 1

                if text_df_button.collidepoint(event.pos):
                   difficulty = 1

                if text_exit_button.collidepoint(event.pos):
                   run = False

            if sound == 1 and difficulty == 0:
                if text_on_button.collidepoint(event.pos):
                  sound_on = 1
                  sound_off = 0
                if text_off_button.collidepoint(event.pos):
                  sound_on = 0
                  sound_off = 1
                if text_menu_button.collidepoint(event.pos):
                  play = 0
                  sound = 0
                   
            if sound == 0 and difficulty == 1:
                if text_menu_button.collidepoint(event.pos):
                  play = 0
                  difficulty = 0
                if text_md_button.collidepoint(event.pos):
                  player_computer.speed = 5
                  ball.speed = 5
                if text_dff_button.collidepoint(event.pos):
                  player_computer.speed = 7
                  ball.speed = 7

    ekran.fill((120,120,200))
    if play == 0 and sound == 0 and difficulty == 0:
      menu()
    if sound == 1:
        sound_menu()
    if difficulty == 1:
        df_menu()
    if play == 1:
        text_p1_score = font.render(f'{p1_score}',True,(0,0,0))
        text_p2_score = font.render(f'{p2_score}',True,(0,0,0))
        ekran.blit(text_p1_score,(390,20))
        ekran.blit(text_p2_score,(510,20))
        pygame.draw.rect(ekran,(0,0,0),(width//2,0,32,height))
        player.update()
        player_computer.update()
        ball.update()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()