def format(time):
    # convert to .10s
    tenths = time % 10
    # convert to absolute seconds
    sec = (time / 10) % 60
    # convert to absolute minutes
    min = ((time / 10) % 60) / 60
    return '%d:%02d.%d' % (min, sec, tenths)


print    format(0), ' = 0:00.0'
print    format(11), ' = 0:01.1'
print    format(321), ' = 0:32.1'
print    format(613), ' = 1:01.3'
