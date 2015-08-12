# Rice Rock Project 
# Boonchu Ngampairoijpibul
# August 8th, 2015
# https://class.coursera.org/interactivepython2-003/
# Note that this program works best at Chrome Browser Only
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
SPAWN_ROCKS = 7 # a number of spawn rocks
SHIP_ROCK_DISTANCE = 150 # a minimum of ship and rock distance
scores = 0 # zero score when game start
lives = 3 # offer 3 lives from start
time = 0
started = False
# only these object tuples allows in this class
RICE_ROCKS = ('Ship', 'Rock', 'Explosion', 'Missile')

best_scores = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=888
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
    
# When thrusting, the ship should accelerate in the direction of its forward vector. 
# This vector can be computed from the orientation/angle of the ship using the provided
# helper function angle_to_vector.
def angle_to_vector(angle):
    return [math.cos(angle), math.sin(angle)]

def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)    

class Ship:
    
    def __init__(self, position, velocity, angle, image, info):
        self.name           = 'Ship'
        self.position       = [position[0], position[1]]
        self.velocity       = [velocity[0], velocity[1]]
        self.thrust         = False
        self.angle          = angle
        self.angle_velocity = 0
        self.image          = image
        self.image_center   = info.get_center()
        self.image_size     = info.get_size()
        self.radius         = info.get_radius()
        
    def get_name(self):
        return self.name
        
    def get_position(self):
        return self.position
    
    def get_radius(self):
        return self.radius    
        
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
        #
        # writing new style of coding
        # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=760
        #self.velocity[0] *= .98
        #self.velocity[1] *= .98   
        self.velocity[:] = [ x*.98 for x in self.velocity]
        
        # == velocity ==
        # Remember that while the ship accelerates in its forward direction, 
        # but the ship always moves in the direction of its velocity vector. 
        if self.thrust:
            accelerate = angle_to_vector(self.angle)
            #self.velocity[0] += accelerate[0] * .1
            #self.velocity[1] += accelerate[1] * .1
            #wrap code - # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=760
            self.velocity = [ x + y*0.1 for x,y in zip(self.velocity, accelerate)]
    
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
    # missile sound is passed to the sprite initializer so that the 
    # shooting sound is played whenever you shoot a missile.
    def shoot(self):
        global missile_group, missile_image, missile_info, missile_sound
            
        print 'Bang Bang'    
        forward = angle_to_vector(self.angle)
        missile_pos = [self.position[i] + self.radius * forward[i] for i in range(2)]
        missile_vel = [self.velocity[i] + 6 * forward[i] for i in range(2)]
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, 
                           missile_image, missile_info, missile_sound)
        a_missile.name_it('Missile')
        missile_group.add(a_missile)
        
    # reset ship to center and drop all ship attributes to zero    
    def reset(self):
        self.position = [WIDTH / 2, HEIGHT / 2]
        self.velocity = [0, 0]
        self.thrust = False
        self.angle = 0
        self.angle_velocity = 0

        
# key handler that controls the spaceship
# 
# keydown handler to call this shoot method when the spacebar is pressed
# 
# To do: rapid fire, oposite direction with "DOWN" key
# https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=789
# holds space key and start timer
KEY_DOWN_DICT = {
        'left' : lambda: Ship.turn(my_ship, 'Left'), 
        'right' : lambda: Ship.turn(my_ship, 'Right'), 
        'up' : lambda: Ship.set_thrust(my_ship), 
        #'up' : lambda: Ship.set_thrust(my_ship, 'up'), 
        'space' : lambda: Ship.shoot(my_ship)
        #'down' : lambda: Ship.set_thrust(my_ship, 'down')
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

# Implement a group_collide helper function. This function should take a set group and 
# a sprite other_object and check for collisions between other_object and elements of the 
# group. If there is a collision, the colliding object should be removed from the group. 
#
# To avoid removing an object from a set that you are iterating over (which can cause you 
# a serious debugging headache), iterate over a copy of the set created via set(group). 
#
# This function should return True or False depending on whether there was a collision. 
# Be sure to use the collide method from part 1 on the sprites in the group to accomplish 
# this task. 
#
# In the draw handler, use the group_collide helper to determine if the ship hit any of the 
# rocks. If so, decrease the number of lives by one. Note that you could have negative lives 
# at this point. 
#
# collision discussion
# https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=847
def group_collide(sprites, other_object):
    global explosion_image, explosion_info, explosion_sound, explosion_group, ship_explosion
    if not other_object.get_name() in RICE_ROCKS:
        return False
                                       
    objs = set()
    for obj in list(sprites):
        if obj.collide(other_object):
            objs.add(obj)
            print 'Boom!!!'
            # adding explosion sprites for draw handler
            if not other_object.get_name() in 'Ship':
                explosion = Sprite(obj.get_position(), 
                               obj.get_velocity(), 
                               0, 0, 
                               explosion_image, 
                               explosion_info, 
                               explosion_sound)
            else:
                explosion = Sprite(other_object.get_position(), 
                               obj.get_velocity(), 
                               0, 0, 
                               ship_explosion, 
                               explosion_info, 
                               explosion_sound)
            explosion.name_it('Explosion')
            explosion_group.add(explosion)   
    if objs:
        sprites.difference_update(objs)
    # return True if value greater than 0
    return len(objs) > 0

# To destroy rocks when they are hit by a missile. We can't quite use group_collide, because we 
# want to check for collisions between two groups. 
# 
# Implement a final helper function group_group_collide that takes two groups of objects as input.
# group_group_collide should iterate through the elements of a copy of the first group using a 
# for-loop and then call group_collide with each of these elements on the second group. 
# 
# group_group_collide should return the number of elements in the first group that collide 
# with the second group as well as delete these elements in the first group. You may find 
# the discard method for sets to be helpful here.
# 
# Call group_group_collide in the draw handler to detect missile/rock collisions. Increment 
# the scores by the number of missile collisions.
def group_group_collide(sprites_a, sprites_b):
    objs = set()
    for obj_a in list(sprites_a):
        if group_collide(sprites_b, obj_a):
            print 'it hits!!!!'
            objs.add(obj_a)
    
    if objs: sprites_a.difference_update(objs)
    
    return len(objs)
        
# Sprite class
class Sprite:
    def __init__(self, position, velocity, angle, angle_velocity, image, info, sound = None):
        self.name = 'Unknown'
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
            
    def get_name(self):
        return self.name
            
    def name_it(self, name):
        self.name = name
   
    def draw(self, canvas):
        # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=881
        # How age works?
        image_center = self.image_center
        if self.animated:            
            if self.name in 'Rock' or self.name in 'Explosion':
                index = ( self.age % self.lifespan ) // 1
                image_center = [self.image_center[0] + index * self.image_size[0], self.image_center[1]]
            elif self.name in 'Missile':
                image_center = [self.image_center[0] + (self.age * self.image_size[0]), self.image_center[1]]    
                
        canvas.draw_image(self.image, image_center, self.image_size, 
            self.position, self.image_size, self.angle)

    # modifying the draw handler to draw the actual image and the update handler to make 
    # the sprite move and rotate. Rocks do not accelerate or experience friction, so 
    # the sprite update method should be simpler than the ship update method.
    #
    # increment the age of the sprite every time update is called. If the age is greater
    # than or equal to the lifespan of the sprite, then we want to remove it. So, return 
    # False (meaning we want to keep it) if the age is less than the lifespan and True 
    # (meaning we want to remove it) otherwise. 
    #
    def update(self):

        # update angle
        self.angle += self.angle_velocity
        
        # update position
        self.position[0] = (self.position[0] + self.velocity[0]) % WIDTH
        self.position[1] = (self.position[1] + self.velocity[1]) % HEIGHT

        # increment the age of the sprite
        if self.lifespan:
            #print 'life span ', self.lifespan, ' age ', self.age
            if self.age > self.lifespan:
                return True
            else:
                if self.get_name() in 'Rock':
                    self.age += 0.0
                elif self.get_name() in 'Explosion':
                    self.age += 0.8
                elif self.get_name() in 'Missile':
                    self.age += 1.2
                else:
                    self.age += 0.0
        return False        
    
    # detect collisions between the ship and a rock. Upon a collision, the 
    # rock should be destroyed and the player should lose a life.
    # 
    # Add a collide method to the Sprite class. This should take an other_object as an argument
    # and return True if there is a collision or False otherwise. For now, this other object 
    # will always be your ship, but we want to be able to use this collide method to detect 
    # collisions with missiles later, as well. 
    # 
    # Collisions can be detected using the radius of the two objects. This requires you to 
    # implement methods get_position and get_radius on both the Sprite and Ship classes.
    # (dist < r1 + r2) ? True : False
    #
    # Rock Collision Calculation
    # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=885
    
    def get_position(self):
        return self.position
    
    def get_velocity(self):
        return self.velocity
    
    def get_radius(self):
        return self.radius
    
    def collide(self, other_object):
        if distance(self.position, other_object.get_position()) <= (self.radius + other_object.get_radius()):
            return True
        return False
       
# Create a helper function process_sprite_group. This function should take a set and a canvas 
# and call the update and draw methods for each sprite in the group.
# 
# Modify process_sprite_group to check the return value of update for sprites. If it 
# returns True, remove the sprite from the group. Again, you will want to iterate 
# over a copy of the sprite group in process_sprite_group to avoid deleting from the 
# same set over which you are iterating.
def process_sprite_group(canvas, sprite_group):
    # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=852
    # order set in list before remove it
    objs = set()
    for sprite in list(sprite_group): 
        sprite.draw(canvas)
        if sprite.update():
           #print 'object was removed'
           objs.add(sprite)
    if objs:
        sprite_group.difference_update(objs)         
    
# timer handler that spawns a rock    
# ship's velocity and rotation are controlled by keys, whereas sprites have these set randomly 
# when they are created
#
# Choose a velocity, position, and angular velocity randomly for the rock.  
def rock_spawner():
    global my_ship, rock_groupl, started, scores
    
    # Method 1 (velocity, angle_velocity, position)
    position = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    velocity = [random.random() * random.choice([-250,250]) / 100 for x in [0,0]]
    angle_velocity = random.random() * random.choice([-0.5, 0.5]) * 0.05
    
    # Method 2 (velocity, angle_velocity, position)
    #if random.random() < 0.5:
    #    negative_h = -1
    #else:
    #    negative_h = 1
    #if random.random() < 0.5:
    #    negative_v = -1
    #else:
    #    negative_v = 1
    #velocity = [random.random() * .6 - .3 + scores / 40 * negative_h, random.random() * .6 - .3 + scores / 40 * negative_v]
    #angle_velocity = random.random() * .2 - .1
    #position = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    
    # do not sparwn rock on top of the ship position
    # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=887
    if started and len(rock_group) < SPAWN_ROCKS and distance(position, my_ship.position) > SHIP_ROCK_DISTANCE:
        a_rock = Sprite(position, velocity, 0, 
                    angle_velocity, asteroid_image, asteroid_info)
        a_rock.name_it('Rock')
        rock_group.add(a_rock) 

def draw(canvas):
    global missile_group, explosion_group, rock_group
    global time, lives, scores, best_scores, started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
                
            
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

    # draw a group of 5 rocks randomly
    # - The program draws a rock as an image.
    # - The rock travels in a straight line at a constant velocity.
    # - The rock is respawned once every second by a timer.
    # - The rock has a random spawn position, spin direction and velocity.
    process_sprite_group(canvas, rock_group)
    
    # check collided?
    is_crash = group_collide(rock_group, my_ship)
    if is_crash == True:
        lives -= 1
        # if ship got hit, clear rock and move ship to screen center position.
        rock_group = set([])
        my_ship.reset()
        
    # draw a group of explosion    
    process_sprite_group(canvas, explosion_group)
    
    # draw a group of missiles   
    # - The program spawns a missile when the space bar is pressed.
    # - The missile spawns at the tip of the ship's cannon.
    # - The missile's velocity is the sum of the ship's velocity and a multiple of its forward vector.
    # - The program plays the missile firing sound when the missile is spawned. 
    #   **** Use Chromse Browser for this test case (Not compatible with Firefox) ****
    process_sprite_group(canvas, missile_group)

    # To do - increase a difficulty
    # https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=922
    
    # reset the game if lives == 0
    if lives < 1:
        lives = 3
        started = False
        # clear the rock 
        rock_group = set([])
        explosion_group = set([])
        missile_group = set([])
        if best_scores < scores:
            best_scores = scores
        my_ship.reset()
        soundtrack.pause()
    
    # update group a group b collision
    scores += group_group_collide(rock_group, missile_group)
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
    
    # draw live scores
    # - The program draws appropriate text for lives on the upper left portion of the canvas.
    # - The program draws appropriate text for scores on the upper right portion of the canvas.
    canvas.draw_text('lives '+ str(lives), ( 60, 40 ), 30, 'Yellow', 'monospace')
    canvas.draw_text('scores '+ str(scores), ( WIDTH - 200, 40), 30, 'Yellow', 'monospace')
    
    if not started:
        canvas.draw_text('Higest scores '+ str(best_scores), ( WIDTH /2 -140, HEIGHT /2 + 100), 30, 'Yellow', 'monospace')

# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, lives, scores
    
    scores = 0
    lives = 3
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.rewind()
        soundtrack.play()
        missile_sound.rewind()
        ship_thrust_sound.rewind()
        explosion_sound.rewind()

#create a Frame unload_handler routine
def unload_timer_check():
    try:
        t = frame.get_canvas_textwidth("t",12)
    except:
        t = 0
    if t==0:
        unload();
        unload_timer.stop()

def unload():
    global soundtrack
    
    print "The frame has been closed."
    soundtrack.pause()
                
" === main() === "        
        
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
# asteroid_info = ImageInfo([64, 64], [128, 128], 17, 64, True)
# asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid1.opengameart.warspawn.png")
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")
ship_explosion = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_blue.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# .ogg versions of sounds are also available, just replace .mp3 by .ogg
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# Initialize the rock group to an empty set. 
rock_group = set()
missile_group = set()
explosion_group = set()

# the number of lives remaining and the scores
lives = 3
scores = 0

frame = simplegui.create_frame("Spaceship", WIDTH, HEIGHT)
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# a_rock is created at the start with zero velocity. Instead, we want to create version 
# of a_rock once every second in the timer handler.
timer = simplegui.create_timer(1000.0, rock_spawner)
# get things rollin
timer.start()

# https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=834
# stop background music when frame closes
unload_timer = simplegui.create_timer(1000, unload_timer_check)
unload_timer.start()


frame.start()
