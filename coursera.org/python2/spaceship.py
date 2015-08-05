# SpaceShip Project 
# Boonchu Ngampairoijpibul
# July 28th, 2015
# https://class.coursera.org/interactivepython2-003/
# Note that this program works best at Chrome Browser Only
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0

# When thrusting, the ship should accelerate in the direction of its forward vector. 
# This vector can be computed from the orientation/angle of the ship using the provided
# helper function angle_to_vector.
def angle_to_vector(angle):
    return [math.cos(angle), math.sin(angle)]

def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

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
    
class Ship:
    
    def __init__(self, position, velocity, angle, image, info):
        self.position 		= [position[0], position[1]]
        self.velocity 		= [velocity[0], velocity[1]]
        self.thrust 		= False
        self.angle 			= angle
        self.angle_velocity = 0
        self.image 			= image
        self.image_center 	= info.get_center()
        self.image_size 	= info.get_size()
        self.radius 		= info.get_radius()
        
    # draw the thrust image when it is on. (The ship image is tiled and contains 
    # both images of the ship.)
    def draw(self, canvas):
        center = list(self.image_center)
        if self.thrust:
            center[0] = self.image_center[0] + self.image_size[0]
        canvas.draw_image(self.image, center, self.image_size,
                          self.position, self.image_size, self.angle)
        
    def update(self):
        # update angle by angle velocity from keyup or keydown handler
        self.angle += self.angle_velocity

        # update position
        # modify the ship's update method such that the ship's position wraps around the 
        # screen when it goes off the edge (use modular arithmetic!).
        self.position[0] = (self.position[0] + self.velocity[0]) % WIDTH
        self.position[1] = (self.position[1] + self.velocity[1]) % HEIGHT

        # accelerate the ship in the direction of this forward vector when the ship is
        # thrusting. You will need to update the velocity vector by a small fraction 
        # of the forward acceleration vector so that the ship does not accelerate too fast.
        
        # == velocity ==
        # Remember that while the ship accelerates in its forward direction, 
        # but the ship always moves in the direction of its velocity vector. 
        if self.thrust:
            accelerate = angle_to_vector(self.angle)
            self.velocity[0] += accelerate[0] * .1
            self.velocity[1] += accelerate[1] * .1

        # == friction ==
        # Your ship should always experience some amount of friction. 
        # (Yeah, we know, "Why is there friction in the vacuum of space?". 
        # Just trust us there is in this game.) This choice means that the 
        # velocity should always be multiplied by a constant factor less than 
        # one to slow the ship down. It will then come to a stop eventually 
        # after you stop the thrusters.
        
        # add friction to the ship's update method as shown in the 
        # "Acceleration and Friction" video by multiplying each component of 
        # the velocity by a number slightly less than 1 during each update.
        self.velocity[0] *= .95
        self.velocity[1] *= .95
    
    # While the left arrow is held down, your spaceship should turn counter-clockwise. 
    # While the right arrow is down, your spaceship should turn clockwise. When neither 
    # key is down, your ship should maintain its orientation.
    def turn(self, direction):
        if direction == 'Left': 
            print 'turn spaceship counter-clockwise direction'
            self.angle_velocity -= .025
        elif direction == 'Right': 
            print 'turn spaceship clockwise direction'
            self.angle_velocity += .025
        elif direction == 'Stop': 
            print 'Slow rotation'
            self.angle_velocity = 0
        else: 
            print 'Unknown'
    
    # The up arrow should control the thrusters of your spaceship. 
    # The thrusters should be on when the up arrow is down and off 
    # when it is up. When the thrusters are on, you should draw the 
    # ship with thrust flames. When the thrusters are off, you 
    # should draw the ship without thrust flames.
    # 
    # play the thrust sound when the thrust is on. Rewind the sound 
    # when the thrust turns off.
    def set_thrust(self, bool=True):
        self.thrust = bool
        if bool: 
            print 'up and away!'
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else: 
            print 'slowing down'
            ship_thrust_sound.pause()
    
    # use the same sprite class as for rocks. Missiles will always have 
    # a zero angular velocity. 
    # 
    # spawn a new missile (for now just replace the old missile in 
    # a_missile). The missile's initial position should be the tip of 
    # your ship's "cannon". Its velocity should be the sum of the ship's 
    # velocity and a multiple of the ship's forward vector.
    #
    #  missile sound is passed to the sprite initializer so that the 
    # shooting sound is played whenever you shoot a missile.
    def shoot(self):
        global missile_image, missile_info, missile_sound
            
        print 'Bang Bang'    
        forward = angle_to_vector(self.angle)
        missile_pos = [self.position[i] + self.radius * forward[i] for i in range(2)]
        missile_vel = [self.velocity[i] + 4 * forward[i] for i in range(2)]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, 
                           missile_image, missile_info, missile_sound)
        missiles.append(a_missile)
        
# key handler that controls the spaceship
# 
# keydown handler to call this shoot method when the spacebar is pressed
KEY_DOWN_DICT = {
        'left' : lambda: Ship.turn(my_ship, 'Left'), 
        'right' : lambda: Ship.turn(my_ship, 'Right'), 
        'up' : lambda: Ship.set_thrust(my_ship), 
        'space' : lambda: Ship.shoot(my_ship)
}

KEY_UP_DICT = {
        'left' : lambda: Ship.turn(my_ship, 'Stop'),
        'right' : lambda: Ship.turn(my_ship, 'Stop'),
        'up' : lambda: Ship.set_thrust(my_ship, False),
        #'down' : lambda: Ship.set_thrust(my_ship, False)
}
        
def keyup(key):
    for (i, operation) in KEY_UP_DICT.items():
        #print 'i:',i, simplegui.KEY_MAP[i]
        if key == simplegui.KEY_MAP[i]:
            operation()
            
def keydown(key):
    for (i, operation) in KEY_DOWN_DICT.items():
        #print 'i:',i, simplegui.KEY_MAP[i]
        if key == simplegui.KEY_MAP[i]:
            operation()
    
# Sprite class
class Sprite:
    def __init__(self, position, velocity, angle, angle_velocity, image, info, sound = None):
        self.position = [position[0],position[1]]
        self.velocity = [velocity[0],velocity[1]]
        self.angle = angle
        self.angle_velocity = angle_velocity
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
   
    def draw(self, canvas):
        if self.animated:
            canvas.draw_image(self.image, 
            [self.image_center[0] + (self.age * self.image_size[0]), self.image_center[1]],
                            self.image_size,
                            self.position, 
                            self.image_size,
                            self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, 
                              self.position, self.image_size, self.angle)

    #  modifying the draw handler to draw the actual image and the update handler to make 
    # the sprite move and rotate. Rocks do not accelerate or experience friction, so 
    # the sprite update method should be simpler than the ship update method.
    def update(self):
        remove = False
        # update angle
        self.angle += self.angle_velocity
        
        # update position
        self.position[0] = (self.position[0] + self.velocity[0]) % WIDTH
        self.position[1] = (self.position[1] + self.velocity[1]) % HEIGHT
        self.age += 1
        if self.age == self.lifespan:
            remove = True
        return remove
    
# timer handler that spawns a rock    
# ship's velocity and rotation are controlled by keys, whereas sprites have these set randomly 
# when they are created
#
# Choose a velocity, position, and angular velocity randomly for the rock.  
def rock_spawner():    
    
    position = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    #velocity = [random.random(), random.random()]
    velocity = [random.random() * random.choice([-250,250]) / 100 for x in [0,0]]
    #angle_velocity = random.random() * .05
    angle_velocity = random.random() * random.choice([-0.5, 0.5]) * 0.05
    
    a_rock = Sprite(position, velocity, 0, 
                    angle_velocity, asteroid_image, asteroid_info)
    if len(rocks) < 10:
        rocks.append(a_rock) 

def draw(canvas):
    global rocks, time, live_remaining, score
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
                
    # draw a group of ten rocks randomly
    # - The program draws a rock as an image.
    # - The rock travels in a straight line at a constant velocity.
    # - The rock is respawned once every second by a timer.
    # - The rock has a random spawn position, spin direction and velocity.
    for sprite in rocks: 
        sprite.draw(canvas)
        if sprite.update():
            rocks.remove(sprite)            
            
    # draw ship and sprites
    # - The ship flies in a straight line when not under thrust.
    # - The ship rotates at a constant angular velocity in a counter clockwise direction when the left 
    #   arrow key is held down.
    # - The ship rotates at a constant angular velocity in the clockwise direction when the right arrow 
    #   key is held down.
    # - The ship's orientation is independent of its velocity.
    # - The program draws the ship with thrusters on when the up arrow is held down.
    # - The program plays the thrust sound only when the up arrow key is held down.
    # - The ship accelerates in its forward direction when the thrust key is held down.
    # - The ship's position wraps to the other side of the screen when it crosses the edge of the screen.
    # - The ship's velocity slows to zero while the thrust is not being applied. 
    my_ship.draw(canvas)
    my_ship.update() 
    
    # draw a group of missiles   
    # - The program spawns a missile when the space bar is pressed.
    # - The missile spawns at the tip of the ship's cannon.
    # - The missile's velocity is the sum of the ship's velocity and a multiple of its forward vector.
    # - The program plays the missile firing sound when the missile is spawned. 
    #   **** Use Chromse Browser for this test case (Not compatible with Firefox) ****
    for sprite in missiles: 
        sprite.draw(canvas)
        if sprite.update():
              missiles.remove(sprite)
                
    # draw live scores
    # - The program draws appropriate text for lives on the upper left portion of the canvas.
    # - The program draws appropriate text for score on the upper right portion of the canvas.
    canvas.draw_text('lives '+ str(live_remaining), ( 10, 40 ), 30, 'Yellow', 'monospace')
    canvas.draw_text('scores '+ str(scores), ( WIDTH - 150, 40), 30, 'Yellow', 'monospace')

" === main() === "        
        
# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
# ship sound assets 
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
# missile sound assets
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)

rocks = list()
missiles = list()

# the number of lives remaining and the score
live_remaining = 3
scores = 0

frame = simplegui.create_frame("Spaceship", WIDTH, HEIGHT)
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)

frame.set_draw_handler(draw)

# a_rock is created at the start with zero velocity. Instead, we want to create version 
# of a_rock once every second in the timer handler.
timer = simplegui.create_timer(1000.0, rock_spawner)
# get things rollin
timer.start()

frame.start()
