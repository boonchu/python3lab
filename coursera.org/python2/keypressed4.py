down_key_map = dict()
up_key_map = dict()

def init_keys():
    # Key mappings -- simplegui.KEY_MAP key, (object method, object, arguments)
    # Object is part of the list -- in case we need to controll some other object
    # with the keyboard. For example, we might add another ship.
    down_keys = [
        # name      method        obj       args
        ("left",  ("turn",       my_ship, [-ANGLE_INC])), 
        ("right", ("turn",       my_ship, [ANGLE_INC])), 
        ("up",    ("set_thrust", my_ship, [On])),
        ("p",      (game_pause,   None,    [])),
        ("q",      (game_quit,      None,   [])),
        ("space", ("shoot",      my_ship, []))
    ]

    up_keys =  [
        # name      method        obj       args
        ("left",  ("turn",       my_ship, [ANGLE_INC])), 
        ("right", ("turn",       my_ship, [-ANGLE_INC])), 
        ("up",    ("set_thrust", my_ship, [Off]))
    ]
    
    def init_key_map(key_def, key_map):
        for key_name, key_ops in key_def:
            key = simplegui.KEY_MAP[key_name]
            key_map[key] = key_ops
            
    init_key_map(down_keys, down_key_map)
    init_key_map(up_keys, up_key_map)
    
# Helper function for key handlers. Try/catch to handle unsupported keys
def do_keys(key, key_map):
    try:
        method, obj, args = key_map[key]
        if obj: getattr(obj, method)(*args)
        else: method(*args)
    except:    
        return # ignore all other keys

# Key handlers
def keyup(key):
    do_keys(key, up_key_map)
    
def keydown(key):
    do_keys(key, down_key_map)      
