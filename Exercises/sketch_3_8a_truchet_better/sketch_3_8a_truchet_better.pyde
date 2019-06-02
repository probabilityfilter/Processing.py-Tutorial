size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

size = 50;

for col in range(0,width,size):
    for row in range(0,height,size):
        if int(random(2)) == 0:
            # top-left & bottom-right
            arc(col,row, size,size, 0,PI/2)
            arc(col+size,row+size, size,size, PI,PI+PI/2)
        else:
            # top-right & bottom-left
            arc(col+size,row, size,size, PI/2,PI)
            arc(col,row+size, size,size, PI+PI/2,2*PI)
