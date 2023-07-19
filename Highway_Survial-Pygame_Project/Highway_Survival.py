#Highway_Survival-Pygame_project

#สมาชิก
#6306021610039 นางสาวยาดา สําระสมแสง
#6306021620085 นายเบญจพล เพชรเหลี่ยม
#6306021620093 นายรัฐกรณ์ พลแสน
#6306021620107 นายสหรัฐ พินยาหาญ
#6306021620115 นายกฤษกร สมากุล

#060243103 Problem Solving in IT (1/2563) IT 1RA
#King Mongkut's University of Technology North Bangkok Prachinburi Campus


import pgzrun
import pygame
import time
from random import randint

def draw():
    # draw screen intro
    if StatusGame == 0 :
        screen.fill('black')
        road_sg1.draw()
        len2_sg1.draw()
        len_sg1.draw()
        city_sg1.draw()
        screen.blit('head_sg1' , (0 , 0))
        car_sg1.draw()
        
    # draw screen play
    elif StatusGame == 1 :
        highway.draw()

        # draw car
        car.draw()

        # draw heart
        for heart in hearts :
            heart.draw()

        # draw coin
        for coin in coins :
            coin.draw()

        # draw enemies
        for enemy in enemies :
            enemy.draw()

        

        # draw smoke in front of car while hp = 0
        if not hp > 0:
            car_broken.draw()

        #draw information bar

        # draw time bar
        screen.blit('icon', (0,0))
        screen.draw.text("Time",topleft=(10,65),fontsize=30, owidth=1, ocolor=('black'),color=('skyblue'))
        screen.draw.text(str(Time) + " s",topleft=(12,95),fontsize=30, owidth=1, ocolor=('black'),color=('white'))

        # draw score bar
        screen.draw.text("Score",topright=(465,65),fontsize=30, owidth=1, ocolor=('black'),color=('Yellow'))
        screen.draw.text(str(round(Score)),topright=(465,95), fontsize=30, owidth=1, ocolor=('black'),color=('white'))

        # draw hp bar
        screen.draw.text("HP",topleft=(20,190),fontsize=30, owidth=1, ocolor=('black'),color=('red'))
        screen.draw.text(str(hp),topleft=(20,220),fontsize=30, owidth=1, ocolor=('black'),color=('white'))

        # draw speed bar
        screen.draw.text("Speed",topright=(470,190),fontsize=30, owidth=1, ocolor=('black'),color=('orange'))
        screen.draw.text(str(round((speed*5.5))),topright=(470,220),fontsize=30, owidth=1, ocolor=('black'),color=('white'))
        screen.draw.text(" km/h",topright=(470,245),fontsize=27, owidth=1, ocolor=('black'),color=('white'))
        
    # draw screen score
    elif StatusGame == 2 :
        screen.blit('bg_end',(0,0))
        smoke.draw()
        screen.draw.text("Your score : "+str(round(Score)), topleft=(105,100),fontsize=50,owidth=1.5, ocolor=('black'),color=('white'))
        screen.draw.text("High score : "+str(round(high_score)), topleft=(100,180),fontsize=48,owidth=1.5, ocolor=('black'),color=('skyblue'))
        
    # draw screen new high score
    elif StatusGame == 3 :
        screen.blit('bg_end',(0,0))
        smoke.draw()
        screen.draw.text("Your score : "+str(round(Score)), topleft=(105,100),fontsize=45,owidth=1.5, ocolor=('black'),color=('skyblue'))
        screen.draw.text("New Record!", topleft=(125,180),fontsize=50,owidth=1.5, ocolor=('black'),color=('yellow'))

def on_key_down(key) :
    global StatusGame, Score, high_score
    #prees enter to play
    if StatusGame == 0 :
        if key == keys.RETURN :
            sounds.ready.play()
            start_game()

    #prees enter to play again
    elif StatusGame == 2 :
        if key == keys.RETURN :
            sounds.ready.play()
            start_game()
    #prees enter to play again       
    elif StatusGame == 3 :
        if key == keys.RETURN :
            high_score = Score
            sounds.ready.play()
            start_game()

def update():
    global StatusGame, Score, high_score, hp, Time, speed, accel, random_speeds, crash, spin, side, smoke, car, car_broken, last, last_heart, hearts, coins

    # game_intro screen
    if StatusGame == 0 :
        sounds.highwaysound.play(-1)
        if side:
            city_sg1.x -= 2
            if city_sg1.x < -191:
                side = False
        else:
            city_sg1.x += 2
            if city_sg1.x > 671:
                side = True
        len_sg1.y -= 20
        if len_sg1.y < 700:
            len_sg1.y = 1000
            
        len2_sg1.y -= 20
        if len2_sg1.y < 500:
            len2_sg1.y = HEIGHT
        
        road_sg1.y -=10
        if road_sg1.y < 600:
            road_sg1.y = HEIGHT

        car_sg1.y += 0.25
        if car_sg1.y > 503:
            car_sg1.y = 500
            
    # game_play screen
    if StatusGame == 1 :
        sounds.highwaysound.stop()
        if hp > 0:
            sounds.carbreakdown.stop()
            sounds.car_flame.stop()
        
        #score collect system
        Score += speed*0.01

        #car sound with speed
        if speed < 8:
            sounds.audi_v8.play()
        sounds.audi_v8_highspeed.play()
            
        
        # move moving down in speed
        highway.y += speed
        if highway.y > 800 :
            highway.y = 0

        # if car finish spin then reset car angle to 0
        if not spin:
            car.angle = 0
            
        # moving left
        if keyboard.LEFT :
            if not spin:
                car.angle = 7
            if hp > 0:
                car.x-=5
            if car.left<99 :
                car.left=99
                
        # moving right
        elif keyboard.RIGHT :
            if not spin:
                car.angle = -7
            if hp > 0:
                car.x+=5
            if car.right>WIDTH-100 :
                car.right=WIDTH-100

        # control enemies car
        for n in range(last+1):
            # give enemies speed
            enemies[n].y += speed - random_speeds[n]
            if last > 0 :
                #remove overlapping car
                if enemies[n].colliderect(enemies[n-1]) :
                    last -= 1
                    
                    enemies.remove(enemies[n-1])
                    random_speeds.remove(random_speeds[n-1])
                    n = 0
                    break
                    
            # remove car that passed 1000 pixel
            if enemies[n].y > HEIGHT+200:
                last -= 1
                enemies.remove(enemies[n])
                random_speeds.remove(random_speeds[n])
                break
        
        for enemy in enemies :
            if hp > 0 :
                if not spin:
                    # damaged control
                    if enemy.colliderect(car) :
                        clock.unschedule(create_enemy)
                        sounds.audi_v8.stop()
                        sounds.audi_v8_highspeed.stop()
                        sounds.sse.play()
                        sounds.break_car.play()
                        
                        if speed > 20:
                            speed = speed - 15
                            hp -= 30
                        elif speed > 15:
                            speed = speed - 8
                            hp -= 15
                        elif speed > 10:
                            speed = speed - 4
                            hp -= 8
                        else:
                            speed = 0
                            hp -= 4
                        if hp < 0:
                            hp = 0
                        spin = True
                        clock.schedule_interval(spin_car,0.01)
                        crash = True
                        sounds.audi_v8.play()

            # if hp = 0
            else :
                # new high score
                if Score > high_score :
                    #decrease speed and stop engine sound when die
                    if speed > 0:
                        if speed > 18:
                            speed -= 0.05
                        elif speed > 14:
                            speed -= 0.043
                        elif speed > 8:
                            speed -= 0.033
                        else:
                            speed -= 0.025
                        sounds.audi_v8.stop()
                        sounds.audi_v8_highspeed.stop()
                        sounds.carbreakdown.play()
                        
                    # if not spin then end game
                    if not spin:
                        StatusGame = 3
                    
                # not new high score
                else :
                    #decrease speed and stop engine sound when die
                    if speed > 0:
                        if speed > 18:
                            speed -= 0.05
                        elif speed > 14:
                            speed -= 0.043
                        elif speed > 8:
                            speed -= 0.033
                        else:
                            speed -= 0.025
                        sounds.audi_v8.stop()
                        sounds.audi_v8_highspeed.stop()
                        sounds.carbreakdown.play()
                    # if not spin then end game
                    if not spin:
                        StatusGame = 2
                    
        
        # control spawn enemies when crash
        if crash :
            if speed > 8:
                clock.schedule_interval(create_enemy,2)
                crash = False
            else:
                clock.unschedule(create_enemy)
    

        # heart control speed and rate
        for heart in hearts:
            heart.y += speed-4
            if heart.y > 1000:
                hearts.remove(heart)
            
            if hp > 0 and hp < 100:
                # hp regen control
                if heart.colliderect(car) :
                    sounds.audi_v8.stop()
                    sounds.audi_v8_highspeed.stop()
                    sounds.re1.play()
                    hp += 15
                    hearts.remove(heart)
                    if hp > 100:
                        hp = 100
                    break

        # coin control speed and rate
        for coin in coins:
            coin.y += speed-4
            if coin.y > 1000:
                coins.remove(coin)
            
            # score increase control
            if coin.colliderect(car) :
                sounds.audi_v8.stop()
                sounds.audi_v8_highspeed.stop()
                sounds.ding.play()
                Score += 25
                coins.remove(coin)
                break

    # game_end screen 
    if StatusGame == 2 or StatusGame == 3 :

        # stop engine sound
        sounds.audi_v8.stop()
        sounds.audi_v8_highspeed.stop()

        #start flame car sound
        sounds.car_flame.play()
        
        #smoke on sceen
        smoke.y -= 5
        if smoke.y < -150:
            smoke.y = 426

# reset value when start a new game 
def start_game() :
    global StatusGame, Score, hp, Time, speed, accel, enemies, hearts, random_speeds, coins, random_color, spawn_pos, last_heart, last_coin, coin_spawn_y
    StatusGame = 1
    side = True
    hp = 100
    Time = 0
    TimeOut = False
    spawn_pos = 10
    coin_spawn_y = -150
    reset_coin_y = False
    Score = 0
    speed = 0
    spin = False
    accel = 0.35
    
    enemies = []
    random_speeds = []
    hearts = []
    coins = []
    
    random_color = randint(1,3)
    car.pos = (WIDTH/2,HEIGHT-140)
    car_broken.pos = car.pos
    
    create_enemy()
    
    
# creat enemies
def create_enemy() :
    global random_color, last, spawn_pos, speed
    if StatusGame == 1 :
        # random enemies cars
        random_color = randint(1,7)
        if random_color == 1 :
            enemies.append(Actor('purple_car'))
        elif random_color == 2 :
            enemies.append(Actor('green_car'))
        elif random_color == 3 :
            enemies.append(Actor('blue_car'))
        elif random_color == 4 :
            enemies.append(Actor('small_truck'))
        elif random_color == 5 :
            enemies.append(Actor('small_truck2'))
        elif random_color == 6 :
            enemies.append(Actor('truck'))
        elif random_color == 7 :
            enemies.append(Actor('bus'))

        #append enemies last
        last = len(enemies)-1
        enemies[last].pos = (randint(120,WIDTH-120),-300)

        # random enemies speed
        random_speeds.append(randint(9,10))

# spawn heart
def create_heart():
    global last_heart
    if StatusGame == 1 :
        hearts.append(Actor('heart'))
        last_heart = len(hearts)-1
        hearts[len(hearts)-1].pos = (randint(120,WIDTH-120),-150)

# spawn coin
def create_coin():
    global last_coin, coin_spawn_y, rand_coin, reset_coin_y
    if StatusGame == 1 :
        coins.append(Actor('coin'))
        last_coin = len(coins)-1
        
        if reset_coin_y:
            coin_spawn_y = -150
            
        coins[len(coins)-1].pos = (randint(120,WIDTH-120),coin_spawn_y)
        coin_spawn_y -= 50
        reset_coin_y = False

# coin_spawn_rate
def coin_spawn_rate():
    global last_coin, coins, reset_coin_y
    rand_coin = randint(1,5)
    if rand_coin == 1:
        clock.schedule(create_coin,1)
        reset_coin_y = True
        
    elif rand_coin == 2:
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        reset_coin_y = True

    elif rand_coin == 3:
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        reset_coin_y = True

    elif rand_coin == 4:
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        reset_coin_y = True

    elif rand_coin == 5:
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        clock.schedule(create_coin,1)
        reset_coin_y = True

# acceleration control
def accel_control():
    global speed, accel
    if StatusGame == 1:
        speed += abs(accel)
        accel = (0.000389)*((speed-30)*(speed-30))

# enemies_spawn_rate_when_speed_is_8
def spawn_car_8():
    global speed
    if (speed > 10):
        clock.schedule(create_enemy,1)

# enemies_spawn_rate_when_speed_is_16
def spawn_car_16():
    global speed
    if (speed > 16):
        clock.schedule(create_enemy,1)
        
# car spin control
def spin_car():
    global spin, car, car_broken
    if spin:

        # normal spin
        if hp > 0:
            car.angle += 10
            if car.angle > 360:
                spin = False
                car.angle = 0
                clock.unschedule(spin_car)

        # spin when car is broken(hp = 0) control
        else:
            car_broken.pos = car.pos
            
            car.angle += speed*0.3
            car_broken.angle += speed*0.3
            
            car.y -= speed*0.4
            car_broken.y -= speed*0.4
            
            if car.angle > speed*200:
                spin = False
                car.angle = 0
                car_broken.angle = 0
                clock.unschedule(spin_car)
            
    

# time count system
def time_count() :
    global Time
    Time += 1
    
# time_out system       *not using*
#def time_out() :
    #global TimeOut
    #TimeOut = True

#size window
WIDTH = 480
HEIGHT = 800

# title of the game
TITLE = 'Highway Survival'


side = True
# Give actor
city_sg1 = Actor('city_sg1')

road_sg1 = Actor('road_sg1')
road_sg1.pos=(WIDTH/2,HEIGHT)

car_sg1=Actor('car_sg1')
car_sg1.pos=(WIDTH/2,500)

len_sg1 = Actor('len')
len_sg1.pos=(WIDTH/2,HEIGHT)

len2_sg1 = Actor('len2')
len2_sg1.pos=(WIDTH/2,HEIGHT)

smoke = Actor('smoke')
smoke.pos = (384,426)

# General value
hp = 100
crash = False
Num = 0
Score = 0
high_score = 0
spin = False
Time = 0
TimeOut = False
spawn_pos = 10
speed = 0
accel = 0.35
spawn_time = 3
coin_spawn_y = -150
reset_coin_y = False
StatusGame = 0

# car color random
random_color = randint(1,3)

# actor
car = Actor('car')
car.pos = (WIDTH/2,HEIGHT-140)
car_broken = Actor('car_broken')
car_broken.pos = car.pos

# array
enemies = []
random_speeds = []
hearts = []
coins = []

# road
highway = Actor('wallpaper')

# acceleration control
clock.schedule_interval(accel_control, 0.1)

# car_spawn control
clock.schedule_interval(create_enemy,2.1)
clock.schedule_interval(spawn_car_8,1.2)
clock.schedule_interval(spawn_car_16,0.7)

# heart spawn control
clock.schedule_interval(create_heart, 20.23)

# coin_spawn_rate control
clock.schedule_interval(coin_spawn_rate, 5.31)

# time control
#clock.schedule(time_out,60.0)
clock.schedule_interval(time_count,1.0)

pgzrun.go()
