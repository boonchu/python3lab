# RiceRocks for Hall of Fame
# P. Dusoulier / July 9th 2015

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 500

time = 0
timex = 0

MAX_ROCKS = 12
k_rock = 1
radius_rock = 40
TIME_SCREEN = 10  # time for game over screen display
ROCK_POINTS = 10   # nb of points per asteroid distroyed
NOVA_CENTER = [50, 50]
NOVA_SIZE = [100, 100]
NOVA_DIM = [9, 9]
record = 0
time_record = 0
trc = "0s"
play_mode = "shoot"  # Shooting mode by default at launch

SPEED_INTERVAL = 30  # interval to speed up rocks in timing mode
K_REBOUND = 2.0  # elasticity factor

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

turret_info = ImageInfo([15,12], [30, 24],1)
turret_image = simplegui.load_image("https://dl.dropbox.com/s/j3zyc1lufntwzvp/tourelle_slim2.png")
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
miss_pos = [[0, 38],[-1.57,15],[1.57, 15]]

# ship debris
ship_debris_list = []
ship_debris1_info = ImageInfo([31.5,25], [63,50],0)
ship_debris1_image = simplegui.load_image("https://dl.dropbox.com/s/jlsxhjor5fxpp46/ship_debris1.png")
ship_debris_list.append([ship_debris1_image,ship_debris1_info])

ship_debris2_info = ImageInfo([28.5,22.5], [57,45],0)
ship_debris2_image = simplegui.load_image("https://dl.dropbox.com/s/1wlrqosmudegv9z/ship_debris2.png")
ship_debris_list.append([ship_debris2_image,ship_debris2_info])

ship_debris3_info = ImageInfo([30.5,19], [61,38],0)
ship_debris3_image = simplegui.load_image("https://dl.dropbox.com/s/th4km079bjvzlw2/ship_debris3.png")
ship_debris_list.append([ship_debris3_image,ship_debris3_info])

ship_debris4_info = ImageInfo([24,19], [48,38],0)
ship_debris4_image = simplegui.load_image("https://dl.dropbox.com/s/lbmoig09n3uuoo6/ship_debris4.png")
ship_debris_list.append([ship_debris4_image,ship_debris4_info])

# ast2roid images - aster28.5bl2.ue.pn57 45teroid_brown.png2 asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# special nova explosion for final hit
nova_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/explosion.hasgraphics.png")
nova_explosion1=simplegui.load_sound("https://dl.dropbox.com/s/n9rplxesdj5f9j4/explosion1.mp3")

sirene_sound = simplegui.load_sound("https://dl.dropbox.com/s/jdjtooj7yto4v5z/sirene_us.mp3")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(.5)
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
# ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound = simplegui.load_sound("https://dl.dropbox.com/s/1cqydtu2xxufybx/bernard_katz_glass_torch.mp3")
ship_thrust_sound.set_volume(.6)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# Various parameters 
# ANGLE_VEL = math.pi/90  # full circle in 3 seconds
ANGLE_VEL = .06
T_ANGLE_VEL = .08
turret = 0  # turret on manual by default

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:

    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
                              self.pos, self.image_size, self.angle)
       
    def get_pos(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        # update velocity
        if self.thrust:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * .1
            self.vel[1] += acc[1] * .1
            
        self.vel[0] *= .99
        self.vel[1] *= .99

    def set_thrust(self, on):
        self.thrust = on
        if on:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
        
    def modify_angle_vel(self,av):
        self.angle_vel = av
    
    def freeze(self, spin):
        global spin_on
        self.vel[0] = 0
        self.vel[1] = 0
        self.angle_vel = spin
        if lives > 0 :
            sirene_sound.play()
            spin_on = True
            
    def fly_away(self,spin):
        self.angle_vel = spin
        self.vel[0] = random.randint(1,3)*(2*random.randint(0,1) - 1)
        self.vel[1] = random.randint(1,3)*(2*random.randint(0,1) - 1)
        
    def shoot(self):
        global miss_fired
        miss_fired += 1
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 6 * forward[0], self.vel[1] + 6 * forward[1]]
        missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, 1, missile_sound)
        missile_group.add(missile)    

    def multi_shoot(self):
        global miss_fired
        miss_fired += 3
        for n in range (0,3):
            forward = angle_to_vector(self.angle + miss_pos[n][0])
            cossin_tir = angle_to_vector(self.angle)
            missile_pos = [self.pos[0] + miss_pos[n][1]*forward[0], self.pos[1] + miss_pos[n][1]*forward[1]]
            missile_vel = [self.vel[0] + 6*cossin_tir[0], self.vel[1] + 6*cossin_tir[1]] 
            missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, 1, missile_sound)
            missile_group.add(missile)  
                       
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, kr, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.kr = kr
        self.radius = info.get_radius()*self.kr
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        if self.animated == True:
            decale = self.age * self.image_size[0]
            canvas.draw_image(self.image, [self.image_center[0]+decale,self.image_center[1]],
            self.image_size,self.pos, [self.image_size[0]*self.kr, self.image_size[1]*self.kr], self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size,
            self.pos, [self.image_size[0]*self.kr, self.image_size[1]*self.kr], self.angle)
        
    def get_radius(self):
        return self.radius
    
    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def update(self):
        # update angle
        self.angle += self.angle_vel
        
        # update position
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age +=1
        old = False
        if self.age >= self.lifespan:
            old = True
        return old
            
    def collide(self, other_sprite):
        os_radius = other_sprite.get_radius()
        os_pos = other_sprite.get_pos()
        distance = dist(self.pos, os_pos)
        if distance <= (self.radius + os_radius) and distance >0:
            return True
        else:
            return False

def prepare_ship_debris():
    global ship_debris_group
    ship_debris_group = set([])
   
    for i in range(0,4):
        alpha = math.pi/4*(1 + 2*i) + (random.random() - 0.5)
        vel = 0.1*random.randint(8,12)
        velx = vel*math.cos(alpha)
        vely = vel*math.sin(alpha)
        ang_vel = (2*random.randint(0,1) - 1) * (0.05+0.09*random.random()) 
        image = ship_debris_list[i][0]
        info = ship_debris_list[i][1]
        a_ship_debris = Sprite([100,100],[velx,vely],0,ang_vel,image, info, 0.55)
        ship_debris_group.add(a_ship_debris)
    
def f_shoot():
    global play_mode
    if started == False:
        play_mode = "shoot"

def f_time():
    global play_mode, turret
    if started == False:
        play_mode = "time"
        turret = 0
        my_turret.modify_angle_vel(0)
        my_turret.angle = 0
        
                                          
# key handlers to control ship   
def keydown(key):
    global miss_fired, turret, spin_on, lives
    if key == simplegui.KEY_MAP['left']:
        my_ship.modify_angle_vel(- ANGLE_VEL)
        my_turret.modify_angle_vel(- ANGLE_VEL)
        spin_on = False
        sirene_sound.rewind()
    elif key == simplegui.KEY_MAP['right']:
        my_ship.modify_angle_vel(ANGLE_VEL)
        my_turret.modify_angle_vel(ANGLE_VEL)
        spin_on = False
        sirene_sound.rewind()
    elif chr(key) == "Q":
        my_turret.modify_angle_vel(- T_ANGLE_VEL)
    elif chr(key) == "S":
        my_turret.modify_angle_vel(T_ANGLE_VEL)

    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(True)
    if chr(key) == "I":  # cheat code
        lives = 9
    if play_mode == "shoot":
        if key == simplegui.KEY_MAP['space']:
            my_ship.shoot()
        elif chr(key) == "A":
            my_turret.shoot()
        elif chr(key) == "Z":
            my_ship.multi_shoot()
        elif chr(key) == "T":
            turret = (turret + 1) % 3
            if turret == 0:
                my_turret.modify_angle_vel(my_ship.angle_vel)
                          
        
def keyup(key):
    if key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['right'] :
        my_ship.modify_angle_vel(0)
        my_turret.modify_angle_vel(0)
    elif chr(key) == "Q" or chr(key) == "S":
        my_turret.modify_angle_vel(0)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.set_thrust(False)

def ask_radius(text_input):
    global k_rock
    rad= float(text_input)
    if rad >=15 and rad <= 60:
       k_rock = rad/40

def ask_number(text_input):
    global MAX_ROCKS
    n = float(text_input)
    if n > 0 and n <= 20:
        MAX_ROCKS = n
      
    

        
# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True

        # Helpers
def process_sprite_group(canvas, group):
    for object in list(group):
        object.draw(canvas)
        old = object.update()
        if old == True:
            group.remove(object)
        
def group_collide(group, other_sprite):
    # in the calls, the group is always the rocks
    #other_sprite can be the ship or the missiles
    collision = False
    for object in list(group):
        if object.collide(other_sprite) == True:
            if spawn_test == False:
                explosion = Sprite(object.get_pos(), [0,0], 0, 0, explosion_image, explosion_info, 1, explosion_sound)
                explosion_group.add(explosion)
                group.remove(object)
            collision = True
    return collision

def group_group_collide(group1, group2):
    global score, k_rock_vel
    discard1= set([])
    for object1 in list(group1):
        if group_collide(group2,object1) == True:
            score += ROCK_POINTS
            k_rock_vel = score/100
            if k_rock_vel < 1:
                k_rock_vel = 1
            discard1.add(object1)
    group1.difference_update(discard1)

def process_rock_bounce():
    rock_group_bounce = list(rock_group)
    for rock in rock_group:
        if rock in rock_group_bounce:
            group_bounce(rock_group_bounce, rock)
            rock_group_bounce.remove(rock)
        
def group_bounce(rock_group_bounce, rock1):
    for rock2 in rock_group_bounce:
        if rock2.collide(rock1) == True:
            calc_bounce(rock1, rock2)
            rock_group_bounce.remove(rock2)
            return

def calc_bounce(rock1,rock2):
    dx = rock2.pos[0] - rock1.pos[0]
    dy = rock2.pos[1] - rock1.pos[1]
    dist = math.sqrt(dx**2 + dy**2)
    diff = rock1.radius + rock2.radius - dist 
    if diff > 0 and dist > 0:
 
        ax = dx/dist
        ay = dy/dist
        vx1 = rock1.vel[0]
        vy1 = rock1.vel[1]
        vx2 = rock2.vel[0]
        vy2 = rock2.vel[1]
        
        va1 = vx1*ax + vy1 * ay
        vb1 = vy1*ax - vx1 * ay
        va2 = vx2*ax + vy2 * ay
        vb2 = vy2*ax - vx2 * ay
        
        vap1 = va1 + K_REBOUND*(va2-va1)/2
        vap2 = va2 + K_REBOUND*(va1-va2)/2
        
        vx1 = vap1*ax - vb1*ay
        vy1 = vap1*ay + vb1*ax
        vx2 = vap2*ax - vb2*ay
        vy2 = vap2*ay + vb2*ax
        
        rock1.vel[0] = vx1
        rock1.vel[1] = vy1 
        rock2.vel[0] = vx2
        rock2.vel[1] = vy2
        rock2.pos[0] += (diff+2)*ax
        rock2.pos[1] += (diff+2)*ay
  

def calc_hms(t):
    global h_d, m_d1, m_d2, s_d1, s_d2
    h = t // 3600
    ms = t % 3600
    m = ms // 60
    s = ms % 60
    h_d = str(h)
    m_d = str(m)
    if m < 10:
        m_d1='0'
        m_d2=m_d
    else:
        m_d1 = m_d[0]
        m_d2 = m_d[1]
    s_d = str(s)
    if s < 10:
        s_d1='0'
        s_d2=s_d
    else:
        s_d1 = s_d[0]
        s_d2 = s_d[1]
    return [h, m, s]

def rock_speed_up():
    global rock_group
    
    for rock in rock_group:
        rock.vel[0] = 1.03*rock.vel[0]
        rock.vel[1] = 1.03*rock.vel[1]
       
        
def draw_pol(canvas, x,y):
    canvas.draw_polygon([[x,y],[x+25, y],[x+25, y+35],[x, y+35]],2,'Red','White')

def new_game():
    global lives, score, started, time, game_over, count_go
    global msg, w_msg, g_msg, m_msg, p_msg 
    global my_ship, my_turret, rock_group, missile_group, explosion_group
    global ship_debris_group
    global k_rock_vel, miss_fired, speed_timer
    global ratio_msg, r_msg, ratio
    global turret_count, time_count, spin_on, fly
    soundtrack.rewind()
    soundtrack.play()
    my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
    my_turret = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, turret_image, turret_info)
    prepare_ship_debris()
    

    if turret > 0:
        my_turret.modify_angle_vel(T_ANGLE_VEL/4)  
    rock_group = set([])
    missile_group = set([])
    explosion_group = set([])
    nova_explosion1.rewind()
    turret_count = 0
    lives = 3
    score = 0
    miss_fired = 0
    game_over = False
    msg = ""
    miss_msg = ""
    prec_msg = ""
    ratio_msg = ""
    w_msg = 0
    g_msg = 0
    m_msg = 0
    p_msg = 0
    r_msg = 0
    count_go = 1
    k_rock_vel = 1 # used to increase rock vel with score
    spin_on = False
    fly = False
    time = 0
    time_count = 0
    speed_timer = 0
    started = False
    
def draw(canvas):
    global time, started, lives, score, timex
    global game_over, record, msg, w_msg, g_msg, m_msg, p_msg, miss_msg, prec_msg
    global ratio_msg, r_msg, ratio, fly, trc, time_record
    global turret_count
    global ship_debris_group
    # animate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    
    
    my_turret.draw(canvas)
    if game_over == False:
        my_ship.draw(canvas)
        my_turret.draw(canvas)
        if len(rock_group)>1:
            process_rock_bounce()
        process_sprite_group(canvas, rock_group)
        rock_ship = group_collide(rock_group, my_ship)
        
        if rock_ship == True:
            pos = my_ship.get_pos()
            lives -= 1
            spin = 2*ANGLE_VEL*(2*random.randint(0,1) - 1)
            my_ship.freeze(spin)
            my_turret.freeze(spin)
              
            if lives <= 0:
                game_over = True
                fly = True
                for ship_debris in ship_debris_group:
                    ship_debris.pos[0]=my_ship.pos[0]
                    ship_debris.pos[1]=my_ship.pos[1]
                    
                if play_mode == "shoot":
                    if score > record:
                        msg = "New Shooting Record : "+str(score)
                        record = score
                    else:
                        msg = "Shooting Record stands at "+ str(record)
                else:
                    if time_count > time_record:
                        hms = calc_hms(time_count)
                        if hms[0] > 0:
                            trc = str(hms[0]) + "h " + str(hms[1]) + "m "+str(hms[2]) + "s"
                        elif hms[1] > 0:
                            trc = str(hms[1]) + "m "+str(hms[2]) + "s"
                        else:
                            trc = str(hms[2]) + "s"
                        msg = "New Timing Record :" + trc
                        time_record = time_count
                    else:
                        msg = "Timing Record stands at " + trc
                        
                if play_mode == "shoot":
                    miss_msg = "Missiles fired : "+str(miss_fired)
                else:
                    miss_msg = ""
                if score >0:
                    precision = float(miss_fired)/score*ROCK_POINTS
                    ratio = int(1/precision*1000 + 0.5)/10.0
                    precision = int(precision*10 +0.5)/10.0
                    prec_msg = str(precision) + " missiles/rock"
                    ratio_msg = "Accuracy : "+str(ratio)+" %"
                else:
                    precision = 0
                    prec_msg = ""
                    ratio_msg = ""    
                                
                w_msg = frame.get_canvas_textwidth(msg, 25)
                g_msg = frame.get_canvas_textwidth("GAME OVER",40)
                m_msg = frame.get_canvas_textwidth(miss_msg,25)
                p_msg = frame.get_canvas_textwidth(prec_msg,25)
                r_msg = frame.get_canvas_textwidth(ratio_msg,25)
                nova_explosion1.play()
    else:
        if fly == True:
            my_turret.fly_away(2*ANGLE_VEL)
            fly = False
        my_turret.update()
        process_sprite_group(canvas, ship_debris_group)
        nova_index = [timex % NOVA_DIM[0]//1, (timex // NOVA_DIM[0]) % NOVA_DIM[1]//1]
        canvas.draw_image(nova_image, 
                    [NOVA_CENTER[0] + nova_index[0] * NOVA_SIZE[0], 
                     NOVA_CENTER[1] + nova_index[1] * NOVA_SIZE[1]], 
                     NOVA_SIZE, my_ship.get_pos(), NOVA_SIZE)
        timex += 0.8
        if timex > 63:
            timex = 0
        canvas.draw_text("GAME OVER", [(WIDTH - g_msg)/2,HEIGHT/2], 40, 'Red')
        canvas.draw_text(miss_msg, [(WIDTH- m_msg)/2, 90], 25, 'White')
        canvas.draw_text(prec_msg, [(WIDTH- p_msg)/2, 120], 25, 'White')
        canvas.draw_text(ratio_msg, [(WIDTH - r_msg)/2, 150], 25, 'White')
            
        canvas.draw_text(msg, [(WIDTH- w_msg)/2, 180], 25, 'White')
        if count_go >= TIME_SCREEN:
            new_game()
        
     # draw UI
    canvas.draw_text("Lives:", [10,35], 25, "White")
    draw_pol(canvas,80,10)
    canvas.draw_text(str(lives), [86,35], 25, "Black")
    canvas.draw_text("Score:", [WIDTH- 178, 35], 25, "White")
    draw_pol(canvas, WIDTH-110, 10)
    draw_pol(canvas, WIDTH-85, 10)
    draw_pol(canvas, WIDTH-60, 10)
    draw_pol(canvas, WIDTH-35, 10)
    if score > 9999: 
        score = 9999
    score_str = str(score)
    if score <10:
        score_str = "000"+score_str
    elif score <100 :
        score_str = "00" + score_str
    elif score <1000:
        score_str = "0" + score_str
        
        
    for i in range(0,4):
        canvas.draw_text(score_str[i], [WIDTH-110 + 6 + 25*i,35], 25, "Black")
    if play_mode == "shoot":
        msg1 = "Best so far: "+ str(record)
        l = frame.get_canvas_textwidth(msg1,20)
        canvas.draw_text(msg1, [WIDTH -84 - l/2,65], 20, "White")
    else:
        msg1 = "Best so far: "+ trc
        l = frame.get_canvas_textwidth(msg1,20)
        canvas.draw_text(msg1, [(WIDTH - l)/2,65], 20, "White")
        
    calc_hms(time_count)
    draw_pol(canvas,300,10)
    draw_pol(canvas,350,10)
    draw_pol(canvas,375,10)
    draw_pol(canvas,425,10)
    draw_pol(canvas,450,10)
    canvas.draw_text(h_d,[306,35],25, "Black")
    canvas.draw_text('h',[331,35],25,'White')
    canvas.draw_text(m_d1,[356,35],25, "Black")
    canvas.draw_text(m_d2,[381,35],25, "Black")
    canvas.draw_text('m',[404,35],25,'White')
    canvas.draw_text(s_d1,[431,35],25, "Black")
    canvas.draw_text(s_d2,[456,35],25, "Black")
    canvas.draw_text('s',[481,35],25,'White')
    
    # update ship and sprites
    if game_over == False:
        process_sprite_group(canvas, missile_group)
    
        process_sprite_group(canvas, explosion_group)
    
    # check missiles hitting rocks
        group_group_collide(missile_group, rock_group)
    
        my_ship.update()
        if turret > 0:
            my_turret.modify_angle_vel(T_ANGLE_VEL/4)
        my_turret.update()
        my_turret.pos[0] = my_ship.pos[0]
        my_turret.pos[1] = my_ship.pos[1]
        my_turret.vel[0] = my_ship.vel[0]
        my_turret.vel[1] = my_ship.vel[1]
        if turret == 2 and started == True and spin_on == False and play_mode == "shoot":
            turret_count +=1
            if turret_count >=30:
                my_turret.shoot()
                turret_count =0

    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())

# timer handler that spawns a rock    
def rock_spawner():
    global count_go, spawn_test, time_count, speed_timer
    if started == True and game_over == False:
        time_count +=1
        if play_mode == "time":
            speed_timer += 1
            if speed_timer >= SPEED_INTERVAL:
                speed_timer = 0
                rock_speed_up()
    if len(rock_group) < MAX_ROCKS and started == True and game_over == False:
        
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        s1 = 2*random.randint(0,1) - 1
        s2 = 2*random.randint(0,1) - 1
        k_rock_vel = (score - 100)//50
        rx = 0.1*s1*random.randint(2 + k_rock_vel//2, 10+k_rock_vel)
        ry = 0.1*s2*random.randint(2 + k_rock_vel//2, 10+k_rock_vel)
     
        rock_vel = [rx,ry]
        rock_avel = random.random() * .2 - .1
        a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info,k_rock)
        spawn_test = True
        if a_rock.collide(my_ship) == False and group_collide(rock_group, a_rock)== False:
            rock_group.add(a_rock)
            
        spawn_test = False
    elif game_over == True:
        count_go += 1
        
# initialize stuff
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)



new_game()
# register handlers
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

frame.add_button("Shooting Mode", f_shoot, 120)
frame.add_button("Timing Mode", f_time, 120)
inp = frame.add_input("Rock Radius (15 - 60)", ask_radius,130)
inp2 = frame.add_input("Nb of Rocks (1 - 20)", ask_number,130) 
label00 = frame.add_label('')
label0 = frame.add_label('Space bar => shoots 1 missile')
label1 = frame.add_label('Z => shoots 3 missiles')
label2 = frame.add_label('T => Turret toggle through :')
label3 = frame.add_label('** Manual : Q/S to rotate, A to shoot')
label4 = frame.add_label('** Semi-Auto : self_rotates, A to shoot')
label5 = frame.add_label('** Automatic : self_rotates, shoots 3 missiles/sec')
                         



timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

