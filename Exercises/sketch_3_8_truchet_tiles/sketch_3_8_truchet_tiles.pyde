size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

# arc(0,0, 50,50, 0,PI/2)
# arc(50,50, 50,50, PI,PI+PI/2)

for i in range(0,width/50):
    for j in range(0,height/50):
        if int(random(2)) == 0:
            # top-left & bottom-right
            arc(0+i*50,0+j*50, 50,50, 0,PI/2)
            arc(50+i*50,50+j*50, 50,50, PI,PI+PI/2)
        else:
            # top-right & bottom-left
            arc(50+i*50,0+j*50, 50,50, PI/2,PI)
            arc(0+i*50,50+j*50, 50,50, PI+PI/2,2*PI)
