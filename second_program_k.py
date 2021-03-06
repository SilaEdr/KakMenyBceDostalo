# coding: utf8
import pygame

# размер окна
size = [400, 440]
window = pygame.display.set_mode(size)
# задайте имя
pygame.display.set_caption("Strelok Egor")
screen = pygame.Surface([400, 440])
score = pygame.Surface([400,40])




   




class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))



def IntersectR(s1, s2):
    s1_x = s1.x
    s1_y = s1.y
    s2_x = s2.x
    s2_y = s2.y
    if ((s1_x>s2_x-40) and (s1_x<s2_x+40) and (s1_y>s2_y-40) and (s1_y<s2_y+40)):
        return 1
    else:
        return 0



def destroyed(s1, s2):
    w = 20
    s1_x = s1.x
    s1_y = s1.y
    s2_x = s2.x
    s2_y = s2.y
    if ((s1_x>s2_x-w) and (s1_x<s2_x+w) and (s1_y>s2_y-w) and (s1_y<s2_y+w)):
        

        return 1
    else:
        return 0




# создание персонажей
# герой 
hero = Sprite(50, 200, 'archer.png')
hero.right = True
hero.up = True

# стрела
strela = Sprite(500, 500, 'strela.png')
strela.push = False

# враги
enemy = Sprite(150, 100, 'enemy.png')
enemy.right  = False
enemy.up = True

enemy2 = Sprite(350, 0, 'enemy2.png')
enemy2.right = False
enemy2.up = False

ball = Sprite(500, 500, 'Ball.png')
ball.push = False

ball2 = Sprite(500, 500, 'ball2.png')
ball2.push = False

counter = 0
strel = 5
#создаём шрифт , объявляем об использование шрифтов
pygame.font.init()
myFont = pygame.font.Font('vga866.ttf', 30)
#залипание клавиш
running = True
pygame.key.set_repeat(1, 1)
chetchikstrel = 5
taxt = myFont.render("Game over!", 1, [255, 0, 0])



while running:
    # обработка событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running  = False
        if e.type == pygame.KEYDOWN:
            
            if e.key == pygame.K_UP:
                if hero.y > 0:
                    hero.y -= 2
                
            if e.key == pygame.K_DOWN:
                if hero.y < 360:
                    hero.y += 2
                    
            if e.key == pygame.K_LEFT:
                if hero.x > 0:
                    hero.x -= 2
                    
            if e.key == pygame.K_RIGHT:
                if hero.x < 360:
                    hero.x += 2



            if e.key == pygame.K_SPACE:
                if strela.push == False:
                    strela.push = True
                    strela.x = hero.x +15
                    strela.y = hero.y +15
                    if  chetchikstrel > 0:
                        chetchikstrel -= 1
                        print (chetchikstrel)
                    
                





            if e.key == pygame.K_w:
                ball.push = True
                ball.x = enemy.x +15
                ball.y = enemy.y +15
                ball.push == True

                ball2.push = True
                ball2.x = enemy2.x +15
                ball2.y = enemy2.y +15
                ball2.push == True



                
    if strela.push == True:
        strela.y -= 3
    else:
        strela.y = -300
        strela.x = -300

    if strela.y < 0:
        strela.push = False




    if ball.push == True:
        x_ball=ball.x
        ball.x=x_ball

        ball.y += 3
    else:
        ball.y = -300
        ball.x = -300


    if ball.y > 360:
        ball.push = False



    if ball2.push == True:
        x_ball2=ball2.x
        ball2.x=x_ball2

        ball2.x -= 3
    else:
        ball2.y = -300
        ball2.x = -300


    if ball2.y > 360:
        ball2.push = False



        
            
    # задайте фоновый цвет
    screen.fill([255, 255, 255])
    score.fill([0, 255 , 255])
    # движение персонажей
  
    if enemy.up == True:
       enemy.x -= 1
       if enemy.x < 0:
            enemy.up = False
    else:
        enemy.x += 1
        if enemy.x > 360:
            enemy.up = True



            
    '''if hero.up == True:
        hero.y -= 1
        if hero.y < 0:
            hero.up = False
    else:
        hero.y += 1
        if hero.y > 360:
            hero.up = True'''

            
    if enemy2.up == True:
       enemy2.y -= 1
       if enemy2.y < 0:
            enemy2.up = False
    else:
        enemy2.y += 1
        if enemy2.y > 360:
            enemy2.up = True

    if IntersectR(hero, enemy):
        hero.up = True
        enemy.up = True
 

        

        
    if destroyed(strela, enemy):
        strela.y = -300
        strela.x = -300
        enemy.y = 1000
        enemy.x = 1000
        counter += 1

    if destroyed(ball, hero):
        ball.y = -300
        ball.x = -300
        hero.y = -300
        hero.x = -300

    if destroyed(ball2, hero):
        ball2.y = -300
        ball2.x = -300
        hero.y = -300
        hero.x = -300

    if destroyed(ball2, enemy):
        ball2.y = -300
        ball2.x = -300
        enemy.y = -300
        enemy.x = -300

    if destroyed(strela, enemy2):
        strela.y = -300
        strela.x = -300
        enemy2.y = 1000
        enemy2.x = 1000
        counter += 1



    # отображение персонажей
    hero.render()
    enemy.render()
    enemy2.render()
    strela.render()
    ball.render()
    ball2.render()

    
    text = myFont.render("Score: ", 1, [255, 0, 0])

    n = myFont.render(str(counter), 1, [255, 0, 0])
    score.blit(text, [10, 10])

    score.blit(n, [60, 10])



    

    toxt = myFont.render("Strel: ", 1, [255, 0, 0])
    

    n = myFont.render(str(chetchikstrel), 1, [255, 0, 0])
    score.blit(toxt, [100, 10])

    score.blit(n, [155, 10])










    
    if chetchikstrel <= 0:
        screen.blit(taxt, [200, 200])




    # отображение окна
    window.blit(screen, [0, 40])
    window.blit(score, [0, 0])
    pygame.display.flip()
    pygame.time.delay(5)
pygame.quit()
