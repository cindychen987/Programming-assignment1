import random

x = 0

MouseMove = False
FirstTime = True
lpointX = list()
lpointY = list()
lSz = list()

black_rect_height = 25
grey_frame_width = 8
blue_grey_height = black_rect_height + grey_frame_width

pannel_red_width = 100
pannel_grey_width = 80
pannel_height = 20

def setup():
    background(0)
    size(600, 600)
    global x
    x = width / 2 - pannel_red_width / 2
    frameRate(50)
        
def draw_rect_grey():
    fill(119, 117, 125)
    rect(0, black_rect_height, width, height - black_rect_height)

def draw_rect_blue():
    fill(23, 15, 87)
    rect(grey_frame_width, blue_grey_height, width - grey_frame_width * 2, height - blue_grey_height)

def draw_rect_small_red():
    fill(240, 10, 10)
    stroke(0)
    rect(grey_frame_width, blue_grey_height,(width - grey_frame_width * 2) / 10, (width - grey_frame_width * 2) / 10 / 2)

def draw_sparkle():
    noFill()
    stroke(255)
    rect(-4, -4, 8, 8)

def draw_star():
    global lpointX 
    global lpointY 
    global lSz

    col2 =- 1676082
    FirstTime = False
    for i in range(1):
        x = map(random.random(), 0, 1, 8, 580)
        y = map(random.random(), 0, 1, 40, 600)
       
        if get(int(x), int(y)) == col2:
            continue
        pushMatrix()
        translate(x, y)
        sz = map(random.random(), 0, 1 , 0.5, 1)
        
        scale(sz, sz)
        draw_sparkle()
        popMatrix()
        lpointX.append(x)
        lpointY.append(y)
        lSz.append(sz)
    
    for i in range(len(lpointX) - 1):
        x = lpointX[len(lpointX) - i - 1]
        y = lpointY[len(lpointX) - i - 1]
        if get(int(x), int(y)) == col2:
            continue
        pushMatrix()
        translate(x, y)
        sz = lSz[len(lpointX) - i - 1]
        scale(sz - 0.4, sz - 0.4)
        draw_sparkle()
        popMatrix()
        
    if len(lpointX) > 100:
        lpointX.pop(0)
        lpointY.pop(0)
        lSz.pop(0)
        
def draw():
    global x
    global MouseMove
    time = millis()
    delta = 5
    space = 1
    brick_width = ((width - grey_frame_width *2) / 10) + 0.3
    brick_height = brick_width / 2


    draw_rect_grey()
    draw_rect_blue()
    draw_star()
    
    for j in range (8):
        for i in range(10):
            fill(random.randint(240, 255), random.randint(10, 50), random.randint(10, 50))
            stroke(0,0,0)
            rect((grey_frame_width + space) + i * (brick_width), blue_grey_height + j * (brick_height), brick_width - space, brick_height-space)


    if keyPressed:
        if keyCode == LEFT:
            x-=delta
        if keyCode == RIGHT:
            x+=delta
        MouseMove=False
    else:
        if mousePressed:
            if mouseButton == LEFT:
                MouseMove=True
                
    if MouseMove:
        x=mouseX 

    if x > width - grey_frame_width - pannel_red_width:
        x = width - grey_frame_width - pannel_red_width
    if x < grey_frame_width:
        x = grey_frame_width

    pannel(x) 

def pannel(x):
    fill(255, 51, 0)
    rect(x, height * 0.9, pannel_red_width, pannel_height, 10, 10, 10, 10)
    fill(119, 117, 125)
    rect(x + 10, height * 0.9, pannel_grey_width, pannel_height)