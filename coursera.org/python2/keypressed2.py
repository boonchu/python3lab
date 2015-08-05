import simplegui

class Ship(object):
    
    def __init__(self):
        pass
    
    def turn(self, direction):
        if direction == 'Left': print 'turn spaceship counter-clockwise direction'
        elif direction == 'Right': print 'turn spaceship clockwise direction'
        elif direction == 'None': print 'no action'
        else: print 'Unknown'
            
    def thruster(self, bool=True):
        if bool: print 'up and away!'
        else: print 'slowing down'
        
    def shoot(self):
        print 'Bang Bang'
        
        
    # key handler that controls the spaceship
KEY_DOWN_DICT = {
        'left' : lambda: Ship.turn(my_ship, 'Left'), 
        'right' : lambda: Ship.turn(my_ship, 'Right'), 
        'up' : lambda: Ship.thruster(my_ship), 
        'space' : lambda: Ship.shoot(my_ship)
}

KEY_UP_DICT = {
        'left' : (Ship.turn, ['None']), 
        'right' : (Ship.turn, ['None']), 
        'down' : (Ship.thruster, [False])
}

        
def keyup(key):
    for (i, operation) in KEY_UP_DICT.items():
        #print 'i:',i, simplegui.KEY_MAP[i]
        if key == simplegui.KEY_MAP[i]:
            operation[0](my_ship, *operation[1])
            

def keydown(key):
    for (i, operation) in KEY_DOWN_DICT.items():
        #print 'i:',i, simplegui.KEY_MAP[i]
        if key == simplegui.KEY_MAP[i]:
            operation()
            
my_ship = Ship()
        
frame = simplegui.create_frame("Keys", 50, 50)
frame.set_keyup_handler(keyup)
frame.set_keydown_handler(keydown)
frame.start()
