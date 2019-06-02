size(600,600)
background('#004477')
#noFill()
stroke('#FFFFFF')
strokeWeight(3)

size = 40
gap = 20
jitter = 0
n=0

for col in range(gap/2,width,size+gap):
    for row in range(gap/2,height,size+gap):
        quad(col+int(random(-2,2))*jitter,row+int(random(-2,2))*jitter, col+size+int(random(-2,2))*jitter,row+(int(random(-2,2)))*jitter, col+size+int(random(-2,2))*jitter,row+size+(int(random(-2,2)))*jitter, col+int(random(-2,2))*jitter,row+size+int(random(-2,2))*jitter)
        jitter = n*gap/((width/(size+gap))*(width/(size+gap))*2)
        n=n+1
