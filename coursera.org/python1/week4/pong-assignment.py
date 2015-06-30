# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]; 
    # For the horizontal velocity, we suggest a speed of around 
    # random.randrange(120, 240) pixels per second. For the vertical 
    # velocity, we suggest a speed of around random.randrange(60, 180) 
    # pixels per second. 
    #
    # Convert to 1/60s for slowing down to get realistic speed.
    ball_vel = [random.randrange(120, 240)/60.0, random.randrange(60, 180)/60.0]
    # The velocity of the ball should be 
    #  	upwards and towards the right if direction == RIGHT and 
    #   upwards and towards the left if direction == LEFT
    if (direction == RIGHT):  
            ball_vel[1] = -ball_vel[1]
    else:
            ball_vel[0] = -ball_vel[0]  
            ball_vel[1] = -ball_vel[1]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global ball_velocity, paddle_velocity
    
    # paddle1_pos, paddle2_pos, paddle1_vel and paddle2_vel 
    # should be numbers, NOT lists!
    paddle1_pos = HEIGHT / 2  
    paddle2_pos = HEIGHT / 2  
    paddle1_vel = 0  
    paddle2_vel = 0  
    
    # increase the velocity of the ball by 10% each time it strikes a paddle.
    ball_velocity = 1.10
    # increment of vertical velocity effect on "key down" event
    paddle_velocity = 2.0
    
    # add code to new_game which resets the score before calling spawn_ball
    score1 = 0  
    score2 = 0  
    # random select the direction when game serves from the middle
    spawn_ball(random.choice([LEFT, RIGHT]))
     

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global velocity
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    ##### determine when it hits the top or bottom
         
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT-BALL_RADIUS):    
         ball_vel[1] = -ball_vel[1]  

    ##### determine whether paddle and ball collide            
    # 
    # Check whether the ball is actually striking a paddle when it touches a gutter. 
    # If so, reflect the ball back into play. This collision model eliminates the 
    # possibility of the ball striking the edge of the paddle and greatly simplifies 
    # your collision/reflection code.
            
    # toward edge of left
    if ball_pos[0] <= BALL_RADIUS:    
         # tests whether the ball touches/collides with the left or right gutters. When 
         # the ball touches a gutter, use either spawn_ball(LEFT) or spawn_ball(RIGHT) 
         # to respawn the ball in the center of the table headed towards the opposite gutter. 
         if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:  
              # reflect the ball back into play. 
              ball_vel[0] = -ball_vel[0]    
              # increase the velocity of the ball by 10% each time it strikes a paddle.
              ball_vel[0] = ball_vel[0] * ball_velocity    
              ball_vel[1] = ball_vel[1] * ball_velocity    
         else:    
              spawn_ball(RIGHT)  
              # Add scoring to the game as shown in the Pong video lecture. Each time 
              # the ball strikes the left or right gutter (but not a paddle), the opposite 
              # player receives a point and ball is respawned appropriately.
              score2 += 1    
    # toward edge of right
    elif ball_pos[0] >= (WIDTH - BALL_RADIUS):    
         # tests whether the ball touches/collides with the left or right gutters. When 
         # the ball touches a gutter, use either spawn_ball(LEFT) or spawn_ball(RIGHT) 
         # to respawn the ball in the center of the table headed towards the opposite gutter.
         if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT: 
              # reflect the ball back into play. 
              ball_vel[0] = -ball_vel[0]    
              # increase the velocity of the ball by 10% each time it strikes a paddle.
              ball_vel[0] = ball_vel[0] * ball_velocity    
              ball_vel[1] = ball_vel[1] * ball_velocity    
         else:    
              spawn_ball(LEFT)    
              score1 += 1  
    
    # update the ball position before drawing ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, 20, 1, "Green", "White") 
    
    # updates paddle's vertical position, keep paddle on the screen
    # The vertical positions of these two paddles should depend on two global variables. 
    # (In the template, the variables were paddle1_pos and paddle2_pos.)
    # 
    # modifies the values of these vertical positions via an update in the draw handler.  
    # The update should reference two global variables that contain the vertical 
    # velocities of the paddles. 
    # (In the template, the variables were paddle1_vel and paddle2_vel.)
    #
    # Restrict your paddles to stay entirely on the canvas by adding a check before 
    # you update the paddles' vertical positions in the draw handler.
    # 
    # In particular, test whether the current update for a paddle's position will 
    # move part of the paddle off of the screen. If it does, don't allow the update.

    # "Stuck Paddle"
    # The problem with this solution is that the paddle sticks because when the 
    # condition in the if becomes True, the paddle can't move anymore, ever! 
    # The trick is to replace paddle1_pos in the condition for the if by 
    # paddle1_pos + paddle1_vel. Now, this condition check to see if the next
    # movement for the paddle puts it off the edge. If so, the move is disallowed. 
    # Now, you can move the paddle back down. 
    if HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:  
        paddle1_pos += paddle1_vel    
    if HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:  
        paddle2_pos += paddle2_vel 
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],   
        [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],   
        PAD_WIDTH, "Yellow")     
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],   
        [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT],   
        PAD_WIDTH, "Yellow") 
        
    # draw scores
    canvas.draw_text(str(score1)+"  :  "+str(score2),   
        (WIDTH / 2 - 36, 40), 36, "Yellow")  
        
# To achieve this effect, you will need to use both a keydown and a keyup handler 
# to increase/decrease the vertical velocity in an appropriate manner.        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    global paddle_velocity
 
    # The "w" and "s" keys should control the vertical velocity of the left 
    # paddle while the "Up arrow" and "Down arrow" key should control the 
    # velocity of the right paddle.
    
    # In our version of Pong, the left paddle 
    #     moves up at a constant velocity if the "w" key is pressed and 
    #     moves down at a constant velocity if the "s" is pressed and 
    #     is motionless if neither is pressed. 
    # (The motion if both are pressed is up to you.) 
    
    if key == simplegui.KEY_MAP['s']:    
       paddle1_vel = paddle_velocity   
    elif key == simplegui.KEY_MAP['w']:    
       paddle1_vel = -paddle_velocity   
    elif key == simplegui.KEY_MAP['up']:    
       paddle2_vel = -paddle_velocity
    elif key == simplegui.KEY_MAP['down']:    
       paddle2_vel = paddle_velocity   
   
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key == simplegui.KEY_MAP['s']:    
       paddle1_vel = 0    
    elif key == simplegui.KEY_MAP['w']:    
       paddle1_vel = 0    
    elif key == simplegui.KEY_MAP['up']:    
       paddle2_vel = 0    
    elif key == simplegui.KEY_MAP['down']:    
       paddle2_vel = 0  

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game)  

# start frame
new_game()
frame.start()
