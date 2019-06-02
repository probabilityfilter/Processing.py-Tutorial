size(600,600)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

for i in range(0,10):
    line(75,138+i*10, 228,88+i*10)

c = 2
for i in range(0,10):
    line(370,80+i*c, 522,80+i*c)
    c += 2
    
for i in range(0,9):
    if i%2 == 0:
        line(225,370+i*10, 300,370+i*10)
    else:
        line(300,370+(i*10), 375,370+(i*10))
