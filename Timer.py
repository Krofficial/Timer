import random
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BACKGROUND = (155, 155, 155)

class Bad():
  
    def __init__(self):
        self.direction = random.randrange(1,5)
        self.size_x = 50
        self.size_y = 50
        self.speed = random.randrange(1,6)
        self.x = 0
        self.y = 0
        self.drawn = False
        self.rand_r = random.randrange(256)
        self.rand_g = random.randrange(256)
        self.rand_b = random.randrange(256)
        self.colour = (self.rand_r, self.rand_g, self.rand_b)
        self.coin = random.randrange(21)
        self.am = "bad"

    def draw(self, screen):
     
        if self.drawn == False:
            if self.direction == 1:
                self.x = 375
                self.y = -50
            elif self.direction == 2:
                self.x = -50
                self.y = 375
            elif self.direction == 3:
                self.x = 375
                self.y = 850
            elif self.direction == 4:
                self.x = 850
                self.y = 375
            
            self.drawn = True
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.size_x, self.size_y], 0)
        pygame.draw.rect(screen, WHITE, [self.x, self.y, self.size_x, self.size_y], 5)

    def move(self):
        if self.direction == 1:
            self.y += self.speed
        elif self.direction == 2:
            self.x += self.speed
        elif self.direction == 3:
            self.y -= self.speed
        elif self.direction == 4:
            self.x -= self.speed

    def respawn(self):
        global no_bad

        self.drawn = False       
        self.direction = random.randrange(1,5)
        self.speed = random.randrange(1,6)
        new_bad = random.randrange(1,7)
        self.rand_r = random.randrange(256)
        self.rand_g = random.randrange(256)
        self.rand_b = random.randrange(256)
        self.colour = (self.rand_r, self.rand_g, self.rand_b)
        self.coin = random.randrange(21)
        if no_bad == False:
            if new_bad == 1:
                create_bad(1)

class Bomb(Bad):

    def __init__(self):
        self.direction = random.randrange(1,5)
        self.size_x = 50
        self.size_y = 50
        self.speed = random.randrange(1,6)
        self.x = 0
        self.y = 0
        self.drawn = False
        self.coin = random.randrange(21)
        self.am = "bomb"

    def draw(self, screen):
        if self.drawn == False:
            if self.direction == 1:
                self.x = 375
                self.y = -50
            elif self.direction == 2:
                self.x = -50
                self.y = 375
            elif self.direction == 3:
                self.x = 375
                self.y = 850
            elif self.direction == 4:
                self.x = 850
                self.y = 375
            
            self.drawn = True
        pygame.draw.circle(screen,BACKGROUND,[self.x + 25, self.y + 25],25)
        pygame.draw.circle(screen,YELLOW,[self.x + 25, self.y + 25],25, 5)



pygame.init()

triangle_direction = 1
point_x = 400
point_y = 360
player_health = 3
player_health_bar = 300
shockwave = 3

def draw_player(screen, side):
    global point_x
    global point_y
    global shield

    pygame.draw.rect(screen, YELLOW, [375, 375, 50, 50], 0)
    pygame.draw.rect(screen, WHITE, [375, 375, 50, 50], 3)
    if side == 1:
       point_x = 400
       point_y = 360

       pygame.draw.polygon(screen, RED, ((point_x, point_y),(425, 375), (375, 375)),0)
       pygame.draw.polygon(screen, WHITE, ((point_x, point_y),(425, 375), (375, 375)),3) 
    elif side == 2:
       point_x = 360
       point_y = 400
       
       pygame.draw.polygon(screen, RED, ((point_x, point_y),(375, 425), (375, 375)),0)
       pygame.draw.polygon(screen, WHITE, ((point_x, point_y),(375, 425), (375, 375)),3)
    elif side == 3:
       point_x = 400
       point_y = 440

       pygame.draw.polygon(screen, RED, ((point_x, point_y),(425, 425), (375, 425)),0)
       pygame.draw.polygon(screen, WHITE, ((point_x, point_y),(425, 425), (375, 425)),3)
    elif side == 4:
       point_x = 440
       point_y = 400

       pygame.draw.polygon(screen, RED, ((point_x, point_y),(425, 425), (425, 375)),0)
       pygame.draw.polygon(screen, WHITE, ((point_x, point_y),(425, 425), (425, 375)),3)

    if shield == True:
        pygame.draw.circle(screen,WHITE,[400, 400],50, 10)

def detect_hitbox(enemy_x, enemy_y, enemy_size, point_x, point_y, total_enemy, direction):

    for i in range(len(total_enemy)):
        if direction == 1:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True
        elif direction == 2:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True
        elif direction == 3:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True
        elif direction == 4:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True

def detect_hitbox_end(enemy_x, enemy_y, enemy_size, point_x, point_y, total_enemy, direction):

    for i in range(len(total_enemy)):
        if direction != 1:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True
        elif direction != 2:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True
        elif direction != 3:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True
        elif direction != 4:
            if point_x >= enemy_x and point_x <= enemy_x + enemy_size and point_y >= enemy_y and point_y <= enemy_y + enemy_size:
                return True

slot = -1

def draw_slot(screen):
    global slot
    pygame.draw.rect(screen, WHITE,[25, 25, 200, 200],10)
    pygame.draw.rect(screen, RED,[50, 225, 150, 45],0)
    if slot == 0:
        pygame.draw.rect(screen, RED,[105, 75, 40, 100],0)
        pygame.draw.rect(screen, RED,[75, 105, 100, 40],0)
    elif slot == 1:
        pygame.draw.rect(screen, GREEN, [145, 75, 25, 100], 0)
        pygame.draw.rect(screen, WHITE, [145, 75, 25, 100], 5)
        pygame.draw.rect(screen, WHITE,[95, 105, 10, 50],0)
        pygame.draw.rect(screen, WHITE,[75, 125, 50, 10],0)
    elif slot == 2:
        pygame.draw.rect(screen, RED, [145, 105, 50, 50], 0)
        pygame.draw.rect(screen, WHITE, [145, 105, 50, 50], 5)
        pygame.draw.rect(screen, WHITE,[95, 105, 10, 50],0)
        pygame.draw.rect(screen, WHITE,[75, 125, 50, 10],0)  
    elif slot == 3:
        pygame.draw.rect(screen, RED, [145, 105, 50, 50], 0)
        pygame.draw.rect(screen, WHITE, [145, 105, 50, 50], 5)
        pygame.draw.rect(screen, WHITE,[75, 125, 50, 10],0)
    elif slot == 4:
        pygame.draw.circle(screen,WHITE,[125, 125],50, 10)
    elif slot == 5:
        pygame.draw.line(screen, RED, (35,35), (215,215),5)
        pygame.draw.line(screen, RED, (215,35), (35,215),5)    

def slot_spin():
    global coin_value
    global player_health
    global shockwave
    global bad_limit
    global slot
    global shield
    global bad_list
    global no_bad
    global cost_value

    if coin_value >= cost_value:
        coin_value -= cost_value
        cost_value = random.randrange(70, 131)
        slot = random.randrange(6)
        if slot == 0:
            player_health = 3
        elif slot == 1:
            if shockwave < 3:
                shockwave += 1
        elif slot == 2:
            bad_limit += 1
            create_bad(1)
        elif slot == 3:
            if bad_limit > 0:
                bad_limit -= 1
                no_bad = True
                bad_list[random.randrange(len(bad_list))].respawn()
        elif slot == 4:
            shield = True
        elif slot == 5:
            slot = 5

def draw_healthbar(screen, health, player_health):
    health = player_health * 100

    pygame.draw.rect(screen, RED,[475, 675, 300, 100],0)
    pygame.draw.rect(screen, GREEN,[475, 675, health, 100],0)
    pygame.draw.rect(screen, WHITE,[475, 675, 300, 100],10)

font = pygame.font.Font('freesansbold.ttf',50,)

text_x = 30
text_y = 700
score_value = 0
coin_x = 640
coin_y = 50
coin_value = 0
cost_x = 55
cost_y = 230
cost_value = random.randrange(70,131)

def show_score(x,y):
    score = font.render(str(score_value), True, WHITE)
    screen.blit(score, (x, y))

def show_coins(x,y):
    coins = font.render(str(coin_value), True, YELLOW)
    screen.blit(coins, (x, y))

def show_cost(x,y):
    cost = font2.render(str(cost_value), True, WHITE)
    screen.blit(cost, (x, y))

bad_list = []
baddy = 0
baddy2 = 0
bomb_limit = 1
bad_limit = 4

def create_bad(number):
    global bad_list
    global baddy
    global baddy2
    global bomb_limit

    if len(bad_list) <= bad_limit:
        for i in range(number):
            baddy = Bad()
            bad_list.append(baddy)
    elif len(bad_list) >= bad_limit and len(bad_list) <= bad_limit + bomb_limit:
        for i in range(number):
            baddy2 = Bomb()
            bad_list.append(baddy2)

def draw_charge_bar(screen, amount):
    if amount >= 3:
        pygame.draw.rect(screen, GREEN, [100, 675, 25, 100], 0)
        pygame.draw.rect(screen, WHITE, [100, 675, 25, 100], 5)
    if amount >= 2:
        pygame.draw.rect(screen, GREEN, [135, 675, 25, 100], 0)
        pygame.draw.rect(screen, WHITE, [135, 675, 25, 100], 5)
    if amount >= 1:
        pygame.draw.rect(screen, GREEN, [170, 675, 25, 100], 0)
        pygame.draw.rect(screen, WHITE, [170, 675, 25, 100], 5)

create_bad(1)

# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Timer")
 
# Loop until the user clicks the close button.
done = False
pressed = False
pressed2 = False
pressed3 = False
pressed4 = False
pressed5 = False
pressed6 = False
mouse_clicked = False
shield = False

font2 = pygame.font.SysFont('Calibri', 40, True, False)
text = font2.render("$",True,WHITE)
text2 = font.render("$",True,YELLOW)

 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    keys = pygame.key.get_pressed()
    no_bad = False

    if keys[pygame.K_UP]:
        if pressed == True:
            triangle_direction = 1
        pressed = False

    if not keys[pygame.K_UP]:
        if pressed == False:
            pressed = True

    if keys[pygame.K_LEFT]:
        if pressed2 == True:
            triangle_direction = 2
        pressed2 = False

    if not keys[pygame.K_LEFT]:
        if pressed2 == False:
            pressed2 = True

    if keys[pygame.K_DOWN]:
        if pressed3 == True:
            triangle_direction = 3
        pressed3 = False

    if not keys[pygame.K_DOWN]:
        if pressed3 == False:
            pressed3 = True

    if keys[pygame.K_RIGHT]:
        if pressed4 == True:
            triangle_direction = 4
        pressed4 = False

    if not keys[pygame.K_RIGHT]:
        if pressed4 == False:
            pressed4 = True

    if keys[pygame.K_w]:
        if pressed == True:
            triangle_direction = 1
        pressed = False

    if not keys[pygame.K_w]:
        if pressed == False:
            pressed = True

    if keys[pygame.K_a]:
        if pressed2 == True:
            triangle_direction = 2
        pressed2 = False

    if not keys[pygame.K_a]:
        if pressed2 == False:
            pressed2 = True

    if keys[pygame.K_s]:
        if pressed3 == True:
            triangle_direction = 3
        pressed3 = False

    if not keys[pygame.K_s]:
        if pressed3 == False:
            pressed3 = True

    if keys[pygame.K_d]:
        if pressed4 == True:
            triangle_direction = 4
        pressed4 = False

    if not keys[pygame.K_d]:
        if pressed4 == False:
            pressed4 = True

    if keys[pygame.K_SPACE]:
        if pressed5 == True:
            if shockwave > 0:
                for i in range(len(bad_list)):
                    bad_list[i].respawn()
                shockwave -= 1
                
                if len(bad_list) >= 2:
                    bad_list = []
                    create_bad(2)
                else:
                    bad_list = []
                    create_bad(1)
        pressed5 = False

    if not keys[pygame.K_SPACE]:
        if pressed5 == False:
            pressed5 = True

    if keys[pygame.K_e]:
        if pressed6 == True:
            slot_spin()
        pressed6 = False

    if not keys[pygame.K_e]:
        if pressed6 == False:
            pressed6 = True

    screen.fill(BLACK)
 
    # --- Drawing code should go here
    draw_player(screen, triangle_direction)
    draw_healthbar(screen, player_health_bar, player_health)
    draw_charge_bar(screen, shockwave)
    draw_slot(screen)
    screen.blit(text2, [coin_x + 90, coin_y])
    screen.blit(text, [175, cost_y])

    for i in range (len(bad_list)):
        bad_list[i].draw(screen)
        bad_list[i].move()

        if detect_hitbox(bad_list[i].x, bad_list[i].y, bad_list[i].size_x, point_x, point_y, bad_list, triangle_direction):
            if bad_list[i].am == "bomb":
                if shield == False:
                    bad_list[i].respawn()
                    player_health -= 1
                    if player_health <= 0:
                        done = True
                        print("Your final score was:", score_value)
                else:
                    shield = False
                    bad_list[i].respawn()
            else:              
                bad_list[i].respawn()
                score_value += 1 
                coin_value += bad_list[i].coin      

        if detect_hitbox_end(bad_list[i].x, bad_list[i].y, bad_list[i].size_x, 400, 400, bad_list, triangle_direction):
            if bad_list[i].am == "bomb":
                bad_list[i].respawn()
                score_value += 1 
                coin_value += bad_list[i].coin                
            else:
                if shield == False:
                    bad_list[i].respawn()
                    player_health -= 1
                    if player_health <= 0:
                        done = True
                        print("Your final score was:", score_value)
                else:
                    shield = False
                    bad_list[i].respawn()

    
    show_score(text_x, text_y)
    show_coins(coin_x, coin_y)
    show_cost(cost_x, cost_y)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()