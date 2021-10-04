import pygame
import random
import math
import time

# Initialize pygame
pygame.init()

clock = pygame.time.Clock()

# Create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
PURPLE = (160, 0, 200)
PINK = (255, 0, 255)
WHITE = (255, 255, 255)

# Frame Per Second
FPS = 25

# Sounds
BULLET_CRASH_SOUND = pygame.mixer.Sound('sounds/explosion.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('sounds/shoot.mp3')

# Title
pygame.display.set_caption("Lazy Eye Game")

# Game Icon
game_icon = pygame.image.load('images/eye.png')
pygame.display.set_icon(game_icon)

# Background Image
backgroundmenu = pygame.image.load('images/backgroundx.png').convert()

# Fonts
menu_font = pygame.font.Font("fonts/ka1.ttf", 50)
menu_font2 = pygame.font.Font("fonts/ka1.ttf", 34)
instructions_font = pygame.font.Font("fonts/barcade-brawl.ttf", 13)

# Background
background = pygame.image.load('images/spacemoving2.png').convert()
backgroundY = 0
backgroundY2 = background.get_height() * -1

# Level

level = 1
previous_level = 0

# Player
player_image = pygame.image.load('images/spaceship1.png')
player_X = 370
player_Y = 480
player_X_change = 0

spaceship_sprite = [pygame.image.load('images/spaceship1.png'), pygame.image.load('images/spaceship2.png'),
                    pygame.image.load('images/spaceship3.png'), pygame.image.load('images/spaceship4.png'),
                    pygame.image.load('images/spaceship5.png'), pygame.image.load('images/spaceship6.png'),
                    pygame.image.load('images/spaceship7.png'), pygame.image.load('images/spaceship8.png'),
                    pygame.image.load('images/spaceship9.png')]

# Score
score_value = 0
game_font = pygame.font.Font('fonts/barcade-brawl.ttf', 20)
text_X = 10
text_Y = 10

# Health
health_value = 10
health_text_X = 580
health_text_Y = 10

# Top Score File
topscores_file = "topscores.txt"


def show_score(x,y):
    score = game_font.render("Score : " + str(score_value), True, WHITE)
    game_screen.blit(score, (x,y))

def show_health(x,y):
    health = game_font.render("Health : " + str(health_value), True, WHITE)
    game_screen.blit(health, (x,y))

seconds = 0


def player(x,y):
    game_screen.blit(spaceship_sprite[seconds // 3], (x, y))

# Enemy list
enemy_image = []
enemy_X = []
enemy_Y = []
enemy_Y_change = 0.5
enemy_num = 10

enemyXran = random.randint(0, 736)
enemyYran = random.randint(-600, 50)

enemy_img_content = pygame.image.load('images/invader.png')

blue_enemy = pygame.image.load('images/invader2.png')
red_enemy = pygame.image.load('images/invader.png')

def red_en():
    global enemy_img_content
    # make enemy image red
    enemy_img_content = pygame.image.load('images/invader.png')


def blue_en():
    global enemy_img_content
    # make enemy image blue
    enemy_img_content = pygame.image.load('images/invader2.png')


for i in range(enemy_num):

    enemy_image.append(enemy_img_content)
    enemy_X.append(enemyXran)
    enemy_Y.append(enemyYran)

def enemy(x, y, i):
    game_screen.blit(enemy_image[i], (x, y))

# Bullet
bullet_X = 0
bullet_Y = 480
bullet_Y_change = 10
MAX_BULLETS = 3
bullets =[]


def handle_bullet(bullets):
    for bullet in bullets:
        bullet.y -= 10
        bullet.x
        #print('bullet is ', bullet, 'x is ',bullet.x, 'y is ', bullet.y)
        if bullet.y < 0:
            bullets.remove(bullet)


def collision(enemy_X, enemy_Y, player_X, player_Y):
    distance = math.sqrt(math.pow(enemy_X - player_X, 2) + (math.pow(enemy_Y - (player_Y - 20), 2)))

    if distance < 35:
        return True
    else:
        return False


def isShot(enemy_X, enemy_Y, bullet_X, bullet_Y):
    distance = math.sqrt(math.pow(enemy_X - (bullet_X-28), 2) + (math.pow(enemy_Y-(bullet_Y-20),2)))
    if distance < 35:
        BULLET_CRASH_SOUND.play()
        return True
    else:
        return False

def collidedImg():
    global player_image
    player_image = pygame.image.load('images/spaceshipshot.png')

def backToOriginal():
    global spaceship_sprite
    spaceship_sprite = [pygame.image.load('images/spaceship1.png'), pygame.image.load('images/spaceship2.png'), pygame.image.load('images/spaceship3.png'), pygame.image.load('images/spaceship4.png'), pygame.image.load('images/spaceship5.png'), pygame.image.load('images/spaceship6.png'), pygame.image.load('images/spaceship7.png'), pygame.image.load('images/spaceship8.png'), pygame.image.load('images/spaceship9.png')]


def button(txt, x, y, wid, hei, color_nothover, color_hover, event_call):
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()
    if x + wid > mouse[0] > x and y + hei > mouse[1] > y:
        pygame.draw.rect(game_screen, color_hover, (x, y, wid, hei))
        if pressed[0] == 1 and event_call != None:
            event_call()
    else:
        pygame.draw.rect(game_screen, color_nothover, (x, y, wid, hei))
    button_text = pygame.font.Font("fonts/barcade-brawl.ttf", 20)
    text_style = button_text.render(txt, True, (0,0,0))
    text_box = text_style.get_rect()
    text_box.center = ((x + (wid/2)),(y + (hei/2)))
    game_screen.blit(text_style, text_box)


def refill():
    global enemy_image
    global enemy_X
    global enemy_Y
    global enemy_Y_change
    global enemy_num

    enemy_image = []
    enemy_X = []
    enemy_Y = []
    enemy_Y_change = 0.5
    enemy_num = 10

    for i in range(enemy_num):
        enemy_image.append(enemy_img_content)
        enemy_X.append(random.randint(0, 736))
        enemy_Y.append(random.randint(-600, 50))

def game_intro():
    global health_value, score_value, enemy_num, level, previous_level

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
        game_screen.blit(backgroundmenu, (0,0))
        menutext = menu_font.render('LAZYEYE SHOOTER', 1 ,PINK)
        game_screen.blit(menutext, (SCREEN_WIDTH / 2 - menutext.get_width() / 2, 100))
        refill()


        button("PLAY", 250, 200, 320, 65, PURPLE, PINK, game_loop)
        button("HOW TO PLAY", 250, 275, 320, 65, PURPLE, PINK, instructions)
        button("OPTIONS", 250, 350, 320, 65, PURPLE, PINK, game_selection)
        button("HIGHEST SCORES", 250, 425, 320, 65, PURPLE, PINK, top10_scores)
        button("QUIT", 250, 500, 320, 65, PURPLE, PINK, quit_game)
        pygame.display.update()
        clock.tick(FPS)

        # Restart the game with default values
        health_value = 10
        score_value = 0
        level = 1
        previous_level = 0
        refill()
        # enemy_num = 10

def game_selection():

    gameselection = True
    while gameselection:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameselection = False
                pygame.quit()


        game_screen.blit(backgroundmenu, (0,0))
        selectiontext = menu_font2.render('WHICH SIDE OF YOUR EYES IS LAZY?', 1, PINK)
        game_screen.blit(selectiontext, (SCREEN_WIDTH / 2 - selectiontext.get_width() / 2, 255))
        button("LEFT", 250, 350, 300, 65, PURPLE, PINK, red_en)
        button("RIGHT", 250, 425, 300, 65, PURPLE, PINK, blue_en)
        button("<< BACK", 10, 520, 250, 65, PURPLE, PINK, game_intro)
        pygame.display.update()
        clock.tick(FPS)


def quit_game():
    pygame.quit()
    quit()


# Game Loop
def game_loop():
    global level, previous_level, level_notification, dusman_rect, seconds, spaceship_sprite, player_image, bullets, bullet, bullet_Y_change, player_X, player_X_change, player_Y, background, backgroundY, backgroundY2, bullet_X, bullet_Y, enemy_Y_change, bullet_state, score_value, health_value

    ammunition = []
    #dusman_rect = pygame.rect(enemyXran, enemyYran, 64, 64)
    background = pygame.image.load('images/spacemoving2.png').convert()
    backgroundY = 0
    backgroundY2 = - background.get_height()

    #print(level)

    running_state = True
    # print(enemy_img_content)

    while running_state:

        # Game color
        game_screen.fill((0, 0, 0))

        # Background
        game_screen.blit(background, (0, backgroundY))
        game_screen.blit(background, (0, backgroundY2))

        backgroundY += 1.5
        backgroundY2 += 1.5
        if backgroundY > background.get_height():
            backgroundY = background.get_height() * -1
        if backgroundY2 > background.get_height():
            backgroundY2 = background.get_height() * -1

        # Levels
        level = 1 + score_value // 3
        #enemy's speed adjustment according to levels
        enemy_Y_change = level / 2


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_state = False
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_X_change = -3.5
                if event.key == pygame.K_RIGHT:
                    player_X_change = 3.5
                if event.key == pygame.K_SPACE and len(ammunition) < MAX_BULLETS:
                    ammo = pygame.Rect(player_X + 30, 480 + 10, 5, 12)
                    ammunition.append(ammo)
                    BULLET_FIRE_SOUND.play()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_X_change = 0

        # Player Movement
        player_X += player_X_change

        if player_X <= 0:
            player_X = 0
        if player_X >= SCREEN_WIDTH - 64:
            player_X = SCREEN_WIDTH - 64

        # Enemy Movement
        backToOriginal()
        for i in range(enemy_num):
            enemy_Y[i] += enemy_Y_change
            collided = collision(enemy_X[i], enemy_Y[i], player_X, player_Y)

            if collided is True or enemy_Y[i] > 600:
                print('SHOT')
                enemy_X[i] = random.randint(0, 736)
                enemy_Y[i] = -64
                spaceship_sprite = [pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png'), pygame.image.load('images/spaceshipshot.png')]

                time.sleep(0.3)
                health_value -= 1
                collidedImg()

            for ammo in ammunition:
                #is it shot
                shot = isShot(enemy_X[i], enemy_Y[i], ammo.x, ammo.y)

                if shot is True:
                    bullet_Y = 480
                    score_value += 1
                    #print(score_value)
                    enemy_X[i] = random.randint(0, 736)
                    enemy_Y[i] = -64
                    ammunition.remove(ammo)

            enemy(enemy_X[i], enemy_Y[i], i)

        # Bullet movement
        if bullet_Y > -64:
            bullet_Y -= bullet_Y_change

        handle_bullet(ammunition)

        if health_value < 9:
            game_over()

        for ammo in ammunition:
            pygame.draw.rect(game_screen, WHITE, ammo)

        if previous_level < level:
            level_up()

        seconds += 1
        #print(seconds)
        if seconds > 25:
            seconds = 0
        clock.tick(FPS)
        player(player_X, player_Y)
        show_score(text_X,text_Y)
        show_health(health_text_X, health_text_Y)
        pygame.display.update()
        #blitscreenfunc()

def level_up():
    global level, previous_level, level_notification
    level_up_state = True
    while level_up_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level_up_state = False
                pygame.quit()
        level_notification = menu_font.render('LEVEL ' + str(level), 1, PINK)
        game_screen.blit(level_notification, (SCREEN_WIDTH / 2 - level_notification.get_width() / 2, 200))

        pygame.display.update()
        print('Level is ', level, 'previous level is ', previous_level)
        previous_level = level
        print('Level is ', level, 'previous level is ', previous_level)
        pygame.time.delay(1000)
        game_loop()


def instructions():
    how_to = True
    while how_to:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                how_to = False
                pygame.quit()
        game_screen.blit(background, (0, 0))
        how_to_headline = menu_font.render('HOW TO PLAY', 1, PINK)
        game_screen.blit(how_to_headline, (SCREEN_WIDTH / 2 - how_to_headline.get_width() / 2, 40))

        instructions = instructions_font.render('THIS GAME IS DESIGNED FOR PEOPLE WITH LAZY EYE CONDITION', 1, PINK)
        instructions2 = instructions_font.render('(AMBLYOPIA). THE AIM OF THIS GAME IS TO STIMULATE THE LAZY', 1, PINK)
        instructions3 = instructions_font.render('EYE BY PROVIDING IT WITH DYNAMIC IMAGES, WHILE STRONGER EYE', 1, PINK)
        instructions4 = instructions_font.render('IS MOSTLY EXPOSED TO STILL IMAGES. TO ACHIEVE THIS', 1, PINK)
        instructions5 = instructions_font.render('DISCREPANCY BETWEEN VISUALS, YOU NEED TO GO TO OPTIONS,', 1, PINK)
        instructions6 = instructions_font.render('TO SELECT WHICH ONE OF YOUR EYES HAS AMBYLOPIA. AFTER', 1, PINK)
        instructions7 = instructions_font.render('SELECTING THAT, YOU WILL JUST BUCKLE UP AND ENJOY YOUR', 1, PINK)
        instructions8 = instructions_font.render('SPACE RIDE...IN YOUR SPACE JOURNEY YOU WILL TRY TO SHOOT ALL', 1, PINK)
        instructions9 = instructions_font.render('THE MONSTER COMING IN YOUR WAY AND AVOID CLASHING WITH ', 1, PINK)
        instructions10 = instructions_font.render('THEM, BECAUSE IT WILL DECREASE YOUR HEALTH POINTS. ALSO YOU', 1, PINK)
        instructions11 = instructions_font.render('SHOULD SHOOT THEM BEFORE IT PASSES YOU, OTHERWISE IT WILL', 1, PINK)
        instructions12 = instructions_font.render('ALSO DECREASE YOUR HEALTH. SO BEWARE OF YOUR HEALTH POINTS', 1, PINK)

        credits = game_font.render('© Melis Game Inc.', 1, PURPLE)
        game_screen.blit(instructions, (SCREEN_WIDTH / 2 - instructions.get_width() / 2, 130))
        game_screen.blit(instructions2, (SCREEN_WIDTH / 2 - instructions2.get_width() / 2, 160))
        game_screen.blit(instructions3, (SCREEN_WIDTH / 2 - instructions3.get_width() / 2, 190))
        game_screen.blit(instructions4, (SCREEN_WIDTH / 2 - instructions4.get_width() / 2, 220))
        game_screen.blit(instructions5, (SCREEN_WIDTH / 2 - instructions5.get_width() / 2, 250))
        game_screen.blit(instructions6, (SCREEN_WIDTH / 2 - instructions6.get_width() / 2, 280))
        game_screen.blit(instructions7, (SCREEN_WIDTH / 2 - instructions7.get_width() / 2, 310))
        game_screen.blit(instructions8, (SCREEN_WIDTH / 2 - instructions8.get_width() / 2, 340))
        game_screen.blit(instructions9, (SCREEN_WIDTH / 2 - instructions9.get_width() / 2, 370))
        game_screen.blit(instructions10, (SCREEN_WIDTH / 2 - instructions10.get_width() / 2, 400))
        game_screen.blit(instructions11, (SCREEN_WIDTH / 2 - instructions11.get_width() / 2, 430))
        game_screen.blit(instructions12, (SCREEN_WIDTH / 2 - instructions12.get_width() / 2, 460))
        game_screen.blit(credits, (430, 540))


        button("<<MAIN MENU", 10, 500, 250, 65, PURPLE, PINK, game_intro)
        pygame.display.update()
        clock.tick(50)

def top10_scores():
    global top_headline, f, line, record
    top10scores = True
    while top10scores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                top10scores = False
                pygame.quit()
        game_screen.blit(background, (0, 0))
        top_headline = menu_font.render('TOP SCORES', 1, PINK)

        game_screen.blit(top_headline, (SCREEN_WIDTH / 2 - top_headline.get_width() / 2, 30))

        button("<<MAIN MENU", 10, 520, 240, 65, PURPLE, PINK, game_intro)
        button("<<RESET", 560, 520, 220, 65, PURPLE, PINK, reset_values)

        # Read the Scores
        f = open(topscores_file, 'r')
        f_contents = f.readlines()
        sortedData = sorted(f_contents, reverse = True)

        nums = list()
        try:
            for variabled in sortedData:
                temp = variabled.rsplit(' ', 1)[0]
                #print(temp)
                num = int(temp)
                nums.append(num)

            lastSort = sorted(nums, reverse = True)
            height = 80
            i=0
            while i < 10:
                record = game_font.render(str(i + 1) + '. ' + str(lastSort[i]), 1, WHITE)
                height +=40
                game_screen.blit(record, (SCREEN_WIDTH / 2 - record.get_width() / 2, height))
                i += 1
        except Exception:
            blank_top = game_font.render('', 1, WHITE)
            game_screen.blit(blank_top, (SCREEN_WIDTH / 2 - blank_top.get_width() / 2, 400))
            #print(Exception)

        f.close()
        pygame.display.update()

def reset_values():
    with open(topscores_file, 'w') as f:
        f.write('')

def game_over():
    global score_value

    with open(topscores_file, 'a') as f:
        f.write(str(score_value) + '\n')

    credits_end = True
    while credits_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                credits_end = False
                pygame.quit()

        game_screen.blit(background, (0, 0))
        notification = menu_font.render('GAME OVER', 1, PINK)
        total_score = menu_font.render('Your Score is ' + str(score_value), 1, PINK)
        game_screen.blit(notification, (SCREEN_WIDTH / 2 - notification.get_width() / 2, 200))
        game_screen.blit(total_score, (SCREEN_WIDTH / 2 - total_score.get_width() / 2, 300))
        button("MAIN MENU", 10, 520, 300, 65, PURPLE, PINK, game_intro)

        pygame.display.update()

game_intro()
