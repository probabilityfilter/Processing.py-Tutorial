y = 1

def setup():
    size(500,500)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(3)
    print(y)

def draw():
    global y
    background('#004477')
    y += 1
    print(y)
    ellipse(height/2,y, 47,47)
    
    if frameCount % 100 == 0:
        saveFrame()
