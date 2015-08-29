# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
add_lives = [200, 500, 1000]
time = 0
end_time = 0

#globals
started = False
rock_group = set([])
missile_group = set([])
explosion_group = set([])
angular_velocity = 0.05
SHIP_IMG_CTR = [45, 45]
SHIP_IMG_CTR_THRUST = [135, 45]
LIVES_POS = (100, 50)
SCORE_POS = (WIDTH - 200, 50)
game_over_pos = [0, 125]
GAME_OVER_POS = (200, 125)
GAME_OVER_TEXT = 'Game Over'
GAME_OVER_FONTSIZE = 75
FONT = 'monospace'
FONT_COLOR = '#D6ADEB'

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

    def set_center(self, center):
        #print 'center is now:', center
        self.center = center
    
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
#ship_info = ImageInfo([135, 45], [90, 90], 35)
ship_info = ImageInfo(SHIP_IMG_CTR, [90, 90], 35)
ship_info.set_center(SHIP_IMG_CTR_THRUST)
ship_info.set_center(SHIP_IMG_CTR)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 80)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def new_game():
    global time, started, score, lives, rock_group, missile_group, my_ship
    
    started = True
    score = 0
    lives = 3
    time = 0
    rock_group = set([])
    missile_group = set([])
    my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
    soundtrack.rewind()
    soundtrack.play()
    timer.start()
    
# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.forward_vector = angle_to_vector(self.angle)
        self.scaled_image_size = list(self.image_size)
        self.scaled_radius = self.radius
        self.in_play = True
        scale = 0.75
        self.scaled_image_size[0] = self.image_size[0] * scale
        self.scaled_image_size[1] = self.image_size[1] * scale
        self.scaled_radius = self.radius * scale

    def is_in_play(self, in_play = None):
        if in_play is None:
            return self.in_play
        else:
            self.in_play = in_play

    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.scaled_radius

    def get_velocity(self):
        return self.vel
        
    def set_velocity(self, vel):
        self.vel = vel

    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, \
                             [self.image_center[0] + self.image_size[0], self.image_center[1]], \
                              self.image_size, self.pos, self.scaled_image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, \
                              self.pos, self.scaled_image_size, self.angle)
        
        
    def update_angle_velocity(self, vel_a):
        self.angle_vel = vel_a
    
    def set_thrust(self, thrust):
        self.thrust = thrust
        if self.thrust:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
    
    def shoot(self):
        global a_missile
        
        # use Trigonometry to find position of missile
        # the distance from center of ship to tip less a fraction of the 
        # missile width to account for a few pixels of empty space
        hypotenuse = self.scaled_image_size[0] / 2 - missile_info.get_center()[0] // 2
        opposite = math.sin(self.angle) * hypotenuse # the length of the triangle side opposite self.angle
        adjacent = math.cos(self.angle) * hypotenuse # the length of the triangle side adjacent self.angle
        missile_pos = [self.pos[0] + adjacent, self.pos[1] + opposite]
        
        forward_vector = angle_to_vector(self.angle)
        missile_vel = [self.vel[0] + 3 * forward_vector[0], \
                       self.vel[1] + 3 * forward_vector[1]]
        
        #print "Fire the Laser!!!!"
        a_missile = Sprite(missile_pos, missile_vel, 0, 0, \
                           missile_image, missile_info, missile_sound)
        
        missile_group.add(a_missile)
        #print 'lenth of missile_group', len(missile_group)
        #return 

    
    def update(self):
        friction = .01
        self.angle += self.angle_vel

        # update forward velocity based on angle and thrust
        forward_vector = angle_to_vector(self.angle)
        if self.thrust:
            self.vel[0] += 0.1 * forward_vector[0]
            self.vel[1] += 0.1 * forward_vector[1]

        # friction
        self.vel[0] = self.vel[0] * (1 - friction)
        self.vel[1] = self.vel[1] * (1 - friction)
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # wrap screen
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, \
                 sound = None, scale = 1, splitable = True):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_info = info
        self.sound = sound
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
        self.scaled_image_size = list(self.image_size)
        self.scaled_radius = self.radius
        self.is_splitable = splitable
        self.is_split = False
        if scale != 1:
            self.scaled_image_size[0] = self.image_size[0] * scale
            self.scaled_image_size[1] = self.image_size[1] * scale
            self.scaled_radius = self.radius * scale
   
    def get_image(self):
        return self.image

    def get_image_info(self):
        return self.image_info

    def get_scale(self):
        return self.scale
    
    def set_size(scale):
        self.scale = scale
        self.scaled_image_size[0] = self.image_size[0] * self.scale
        self.scaled_image_size[1] = self.image_size[1] * self.scale
        self.scaled_radius = self.radius * scale

    def split(self):
        self.is_split = True
    
    def is_splitable(self):
        return self.is_splitable

    def has_been_split(self):
        return self.is_split
        
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
        
    def get_velocity(self):
        return self.vel
    
    def get_angular_velocity(self):
        return self.angle_vel
        
    def get_sound(self):
        return self.sound
    
    def draw(self, canvas):
        #[64, 64], [128, 128]
        if self.animated:
            center = [self.image_center[0] + self.image_size[0] * self.age, self.image_center[1]]
            #self.image_center[0] = 64 + 128 * self.age
            canvas.draw_image(self.image, center, self.image_size, \
                              self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, \
                              self.pos, self.scaled_image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        # update the sprite age and check for lifespan expiration
        self.age += 1
        if self.age > self.lifespan:
            return True
        else:
            return False
        
    def collide(self, other_object):
        dist_between_objects = dist(self.pos, other_object.get_position())
        sum_of_object_radii = self.scaled_radius + other_object.get_radius()
        if dist_between_objects < sum_of_object_radii:
            return True
        else:
            return False
        
def generate_split_sprites(sprite, split_scale, splitable):

    pos = sprite.get_position()
    vel = sprite.get_velocity()
    ang = 0
    ang_vel = sprite.get_angular_velocity()
    image = sprite.get_image()
    info = sprite.get_image_info()
    sound = sprite.get_sound()
    scale = split_scale
    radius = sprite.get_radius()


    min_vel = 0
    max_vel = 2
    vel_range = max_vel - min_vel
    x_vel = 0
    y_vel = 0
    velocity = []

    num_new_sprites = random.randint(1, 3)
    sprite_group = set([])
    for new_sprite in range(0, num_new_sprites):
        x_vel = random.random() * vel_range + min_vel
        y_vel = random.random() * vel_range + min_vel
    
        #if vel[0] < 0:
        #    x_vel *= -1
        #if vel[1] < 0:
        #    y_vel *= -1

        velocity = [vel[0] + x_vel, vel[1] + y_vel]

        pos[0] += 2 * vel[0] + 2 * x_vel
        pos[1] += 2 * vel[1] + 2 * y_vel
        #print new_sprite, pos, velocity
    
        a_sprite = Sprite(pos, velocity, ang, ang_vel, image, info, sound, scale, splitable)
        sprite_group.add(a_sprite)
    #print 'length sprite_group', len(sprite_group)
    a_sprite = Sprite(pos, velocity, ang, ang_vel, image, info, sound, scale, splitable)

    return sprite_group
    
def respawn_ship(ship, rock_group):
    rock_too_close_to_ship = True
    for rock in rock_group:
        if dist(my_ship.get_position(), rock.get_position()) > 4 * my_ship.get_radius():
            #rock_too_close_to_ship.append(False)
            continue
        else:
            return
        
    ship.set_velocity([0, 0])
    ship.is_in_play(True)
    
def draw(canvas):
    global time, lives, score, end_time, started
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw an explosion for testing
    #an_explosion.draw(canvas)
    
    # draw lives and score
    canvas.draw_text('Lives ' +  str(lives), LIVES_POS, 25, \
                     FONT_COLOR, FONT)
    canvas.draw_text('Score ' +  str(score), SCORE_POS, 25, \
                     FONT_COLOR, FONT)

    if started == False and len(rock_group) == 0:
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), \
                          [WIDTH / 2, HEIGHT / 2], splash_info.get_size())
    
    if started == True:
        # draw ship and sprites
        if my_ship.is_in_play():
            my_ship.draw(canvas)
            my_ship.update()
            if group_collide(rock_group, my_ship) == True:
                lives -= 1
                my_ship.is_in_play(False)
        else:
            respawn_ship(my_ship, rock_group)
        
        process_sprite_group(rock_group, canvas)
        #a_rock.draw(canvas)
        #a_missile.draw(canvas)

        # update ship and sprites
        #a_rock.update()
        #a_missile.update()

        # draw missiles
        process_sprite_group(missile_group, canvas)
        
        # Test for collisions
        score += 10 * group_group_collide(missile_group, rock_group)

        # draw explosion, but save last explosion for later (lives == 0)
        if lives > 0:
            process_sprite_group(explosion_group, canvas)
           
        add_life(score)
        
        # keep track of when the game ends
        end_time = time

        #print end_time
    if lives == 0:
        started = False
        timer.stop()
        process_sprite_group(rock_group, canvas)
        canvas.draw_text(GAME_OVER_TEXT, game_over_pos, GAME_OVER_FONTSIZE, \
                         FONT_COLOR, FONT)

        # pause to give time for explosion to finish and delay splash image
        if time < end_time + 360:
            # process the final explosion from ship hitting a rock
            process_sprite_group(explosion_group, canvas)
            # create explosions for remaining rocks,
            # delay each explosion
            if (time - end_time) % 24 == 23:
                process_end_game(rock_group, canvas)
            return
        
def add_life(score):
    global lives
    if len(add_lives):
        if score < add_lives[0]:
            return
        else:
            add_lives.pop(0)
            lives += 1
            print 'one life added'
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock

    #We suggest you limit it to 12. With too many rocks
    #the game becomes less fun and the animation
    #slows down significantly, so just return if
    #length of rock_group is 12
    if len(rock_group) >= 12 or started == False:
        return

    position = list(my_ship.get_position())

    # compute random position of a_rock (don't allow spawn too close to ship)
    while dist(position, my_ship.get_position()) < 3 * my_ship.get_radius():
        position = [random.randint(0, WIDTH + 1), \
                    random.randint(0, HEIGHT + 1)]
        #print 'rock position =', position
    
    # compute rotation of a_rock
    min_rotation = -0.04
    max_rotation = 0.04
    rotation_range = max_rotation - min_rotation
    angular_velocity = 0    
    #print rotation_range
    # a slow rotation looks funny, exclude a small range by
    # recomputing until the angular velocity is larger
    while -0.01 < angular_velocity < 0.01:
        angular_velocity = random.random() * rotation_range + min_rotation
        #print 'angular_velocity', angular_velocity

    # compute velocity of a_rock, use the 'time' global to increase
    # min_vel & max_vel so game becomes more difficult (faster rocks)
    # as game progresses
    min_vel = -1 - (0.05 * time // 60)
    max_vel = 1 + (0.05 * time // 60)
    vel_range = max_vel - min_vel
    x_vel = 0
    y_vel = 0
    velocity = []
    # a velocity that is too close to horizontal/vertical 
    # looks funny, exclude a small range by
    # recomputing until the horizontal/vertical velocity is larger
    while (-0.2 < x_vel < 0.2) or (-0.2 < y_vel < 0.2):
        x_vel = random.random() * vel_range + min_vel
        y_vel = random.random() * vel_range + min_vel
        velocity = [x_vel, y_vel]
        #print 'vel', velocity
    
    # spawn a new rock
    a_rock = Sprite(position, velocity, 0, angular_velocity, asteroid_image, asteroid_info)
    
    rock_group.add(a_rock)
    #print 'length of rock_group =', len(rock_group)

def process_end_game(remaining_rocks, canvas):
    remove_set = set([])
    if len(remaining_rocks):
        a_rock = remaining_rocks.pop()
    #for a_rock in remaining_rocks:
        #remove_set.add(a_rock)
        # create explosion Sprite and add to explosion_group
        explosion_pos = a_rock.get_position()
        explosion_vel = a_rock.get_velocity()
        #print explosion_pos, explosion_vel
        an_explosion = Sprite(explosion_pos, explosion_vel, 0, 0, \
                              explosion_image, explosion_info, \
                              explosion_sound)
        explosion_group.add(an_explosion)
    
    #remaining_rocks.difference_update(remove_set)

    
def process_sprite_group(set_of_sprites, canvas):
    remove_set = set([])
    for sprite in set_of_sprites:
        sprite.draw(canvas)
        if sprite.update() == True:
            remove_set.add(sprite)
    set_of_sprites.difference_update(remove_set)
    
def group_collide(group, other_object, split_scale = 0.5):
    remove_set = set([])
    add_set = set([])

    for object in group:
        if object.collide(other_object):
            remove_set.add(object)
            # create explosion Sprite and add to explosion_group
            explosion_pos = object.get_position()
            explosion_vel = object.get_velocity()
            #print explosion_pos, explosion_vel
            an_explosion = Sprite(explosion_pos, explosion_vel, 0, 0, \
                                     explosion_image, explosion_info, \
                                     explosion_sound)
            explosion_group.add(an_explosion)

            if not object.has_been_split() and object.is_splitable:
                add_set = generate_split_sprites(object, split_scale, False)
            
    group.difference_update(remove_set)
    if len(add_set):
        #print "lenth of add_set", len(add_set)    
        group.update(add_set)
    
    if len(remove_set):
        return True
    else:
        return False
    
def group_group_collide(group1, group2):
    #remove_set = ([])
    copy_of_group1 = set(group1)
    count_of_collisions = 0
    for object1 in copy_of_group1:
        if group_collide(group2, object1):
            count_of_collisions += 1
            group1.discard(object1)
            
    return count_of_collisions
            
# key handlers    
def turn_left(key):
    my_ship.update_angle_velocity(-1 * angular_velocity)

def turn_right(key):
    my_ship.update_angle_velocity(angular_velocity)

def stop_turn(key):
    my_ship.update_angle_velocity(0)
    
def thrust_on(key):
    #my_ship.set_thrust(True, ship_info)
    if my_ship.is_in_play():
        my_ship.set_thrust(True)

def thrust_off(key):
    #my_ship.set_thrust(False, ship_info)
    my_ship.set_thrust(False)

def fire(key):
    if my_ship.is_in_play():
        my_ship.shoot()

key_press = {"left" : turn_left,
            "right" : turn_right,
               "up" : thrust_on,
            "space" : fire}

key_release = {"left" : stop_turn,
              "right" : stop_turn,
                 "up" : thrust_off}
#,
#              "space" : ?}


def keydown(key):
    for i in key_press:
        if key == simplegui.KEY_MAP[i]:
            key_press[i](key)

def keyup(key):
    for i in key_release:
        if key == simplegui.KEY_MAP[i]:
            key_release[i](key)

def mouse_click(position):
    
    if started == False:
        splash_size = splash_info.get_size()
        # check if click is within splash_image
        if (WIDTH / 2 - splash_size[0] /2 <= position[0] <= WIDTH / 2 + splash_size[0] /2) and \
           (HEIGHT / 2 - splash_size[1] /2 <= position[1] <= HEIGHT / 2 + splash_size[1] /2):

            new_game()

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, .001, asteroid_image, asteroid_info)
rock_spawner()
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
#my_ship.shoot()
#an_explosion = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, \
#                                     explosion_image, explosion_info, \
#                                     explosion_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(mouse_click)
label1 = frame.add_label('1. Additional Lives earned at')
label2 = frame.add_label(str(add_lives) + ' points')
label3 = frame.add_label('\t')
label4 = frame.add_label('2. Ship will delay to respawn until the area is clear of rocks')
game_over_pos[0] = frame.get_canvas_textwidth(GAME_OVER_TEXT, GAME_OVER_FONTSIZE, FONT)
game_over_pos[0] = WIDTH / 2 - game_over_pos[0] / 2

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
soundtrack.play()

