size(500,500)
background('#004477')
noFill()
stroke('#FFFFFF')
strokeWeight(3)

x = 100
y = 100
i = 1
j = 1

while x*i < 500:
    ellipse(x*i,y, 80,80)
    while y*j < 500:
        ellipse(x*i,y*j, 80,80)
        j += 1
    i += 1
    j = 1
