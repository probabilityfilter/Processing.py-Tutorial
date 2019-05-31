size(800,800)
grid = loadImage('grid.png')
beziers = loadImage('beziers.png')
image(grid, 0, 0)
image(beziers, 0, 0)
noFill()
stroke('#FFFFFF')
strokeWeight(3)

beginShape()
vertex(180,120)
bezierVertex(120,220, 320,250, 275,320)
endShape()

beginShape()
vertex(475,120)
bezierVertex(450,280, 700,280, 650,120)
endShape()

beginShape()
vertex(260,450)
bezierVertex(220,720, 75,475, 320,580)
endShape()

beginShape()
vertex(680,500)
bezierVertex(650,400, 480,420, 600,520)
bezierVertex(710,620, 580,730, 480,630)
endShape()
