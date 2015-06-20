# A simplified Clock example. Just draw the "second" hand
#
import simplegui
import math
import time

# Game constants
WIDTH = 220
HIGHT = 220

# Some extra features
is_analog = True		# Toggle analog display, default to yes
mode_str = ["Analog", "Digital"]	# Human readable output

def draw_clock_hand(canvas, center, length, w, color, degrees):
    """ Compute line start and end based on the angle in degrees """
    end = [0, 0]
    end[0] = center[0] + length * math.sin(math.radians(degrees))
    end[1] = center[1] - length * math.cos(math.radians(degrees))
    canvas.draw_line(center, end, w, color)

def draw_clock_face(canvas, center, radius, color):
    """ Draw the clock dial based on the center and radius """
    ns = [0, 0]
    ne = [0, 0]
    for i in range(60):
        if i % 5 == 0:
            len = radius / 10 + 1
        else:
            len = radius / 20 + 1
        ns[0] = center[0] + (radius - len) * math.sin(math.radians(i*6))
        ns[1] = center[1] - (radius - len) * math.cos(math.radians(i*6))
        ne[0] = center[0] + radius * math.sin(math.radians(i*6))
        ne[1] = center[1] - radius * math.cos(math.radians(i*6))
        canvas.draw_line(ns, ne, 2, color)

# define draw handler
def draw(canvas):
    seconds = int(time.time()) % 60
    if is_analog:
        text_size = 24
        text_start = [WIDTH/2-10, HIGHT-10]
    else:
        text_size = 64
        text_start = [WIDTH/2-30, HIGHT/2]
    canvas.draw_text(str(seconds), text_start, text_size, "Crimson")

    # Just for fun, draw the clocks
    if is_analog:
        ps = [WIDTH/2, HIGHT/2]
        canvas.draw_circle(ps, 80, 2, "Gray")
        canvas.draw_circle(ps, 2, 1, "Gray", "Crimson")
        draw_clock_face(canvas, ps, 80, "Gray")
        degrees = seconds * 6
        draw_clock_hand(canvas, ps, 70, 2, "Crimson", degrees)


def clock_mode():
    global is_analog
    is_analog = not is_analog
    mode_button.set_text(mode_str[is_analog])
    
# create frame
frame = simplegui.create_frame("Stopwatch: a game of reflexes", WIDTH, HIGHT)
frame.set_draw_handler(draw)

# register event handlers
mode_button = frame.add_button(mode_str[is_analog], clock_mode, 75)

# start frame
frame.start()


