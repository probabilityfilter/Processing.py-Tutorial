x = random(800)
y = random(600)
xspeed = 2
yspeed = 2
logo = None

if int(random(0,2)) == 0:
    xdirection = 1
else:
    xdirection = -1

if int(random(0,2)) == 0:
    ydirection = 1
else:
    ydirection = -1
    
def setup():
    global logo
    size(800,600)
    logo = loadImage('dvd-logo.png')

def draw():
    global x,y, xspeed,yspeed, logo, xdirection, ydirection
    #x = random(width)
    background('#000000')
    
    if x>width-100 or x<0:
        xdirection = -1 * xdirection
        
    if y>height-40 or y<0:
        ydirection = -1 * ydirection

    x += xdirection * xspeed
    y += ydirection * yspeed
    image(logo, x,y)
