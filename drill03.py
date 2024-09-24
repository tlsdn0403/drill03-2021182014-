from pico2d import*
import math
open_canvas()

grass=load_image('grass.png')
boy= load_image('character.png')
def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.1)

def run_top():
    print('top')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass
def run_right():
    print('right')
    for y in range(550,0,-10):
        draw_boy(790,y)
    pass
def run_bottom():
    print('bottom')
    pass
def run_left():
    print('left')
    pass

def run_circle():

    r=300
    cx=800//2 ##화면 크기의 절반
    cy=600//2
    for degree in range(0,360,3):
        theta=math.radians(degree)
        x=r*math.cos(theta)+cx
        y=r*math.sin(theta)+cy
        draw_boy(x,y)

       
def run_rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass


while True:
    #run_circle()
    run_rectangle()

    break##임시로 넣음