# Example: Explosion from Sprite class
# 

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600


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

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
ship_thrust_sound.rewind()
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound.rewind()

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
#        print "Init: [%d, %d]" % (self.image_center[0], self.image_center[1])
   
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def draw(self, canvas):
        # canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        
        if self.animated:
            index = ( self.age % self.lifespan ) // 2
            image_center=[self.image_center[0]+ index*self.image_size[0],
                            self.image_center[1]]
            canvas.draw_image(self.image, image_center, self.image_size,
                               self.pos, self.image_size, self.angle)
        
        else: 
            canvas.draw_image(self.image, 
                          self.image_center,
                          self.image_size, 
                          self.pos, 
                          self.image_size,
                          0)
    def update(self):
        
        
        self.age += 0.5
        if self.age > self.lifespan:
            return True
        else:
            return False

def process_sprite_group(canvas, sprite_group):
    end_of_life_group = set([])
    
    for a_sprite in sprite_group:
        a_sprite.draw(canvas)
        if a_sprite.update():
            end_of_life_group.add(a_sprite)
    
    sprite_group.difference_update(end_of_life_group)
 

def draw(canvas):
    
    global explosion_group
    
    process_sprite_group(canvas, explosion_group)
    

# timer handler that spawns a rock    
def rock_spawner():
    global explosion_group
    global explosion_image, explosion_info
    global explosion_sound
    
    posx = random.randint(0, WIDTH)
    posy = random.randint(0, HEIGHT)
    
    if len(explosion_group) >= 3:
        return
    
    explosion_group.add(
                    Sprite([posx, posy], [0, 0], 0, 0, 
                    explosion_image, explosion_info,
                    explosion_sound))
    explosion_sound.rewind()
    explosion_sound.play()
    
    print "Len: %d" % (len(explosion_group))
    thecenter = explosion_info.get_center()
    print "explosion_info.get_center: [%d, %d]" % (thecenter[0], thecenter[1])
    
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

explosion_group = set([])
    
timer = simplegui.create_timer(1000.0, rock_spawner)

frame.start()
timer.start()

