from pico2d import*
import math
open_canvas()

grass=load_image('grass.png')
boy= load_image('character.png')
def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    grass.draw_now(400, 30) 
    delay(0.01)

def run_top():
    for x in range(800,10,-10):
        draw_boy(x,550)
    pass
def run_right():
    for y in range(90,550,10):
        draw_boy(790,y)
    pass
def run_bottom():
    for x in range(10,800,10):
        draw_boy(x,90)
    pass
def run_left():
    for y in range(550,90,-10):
        draw_boy(10,y)
    pass

def run_tri_bottom():
    for x in range(10,700,10):
        draw_boy(x,90)
    pass
def run_tri_right():
    x=700
    y=90
    while(x>400):
        draw_boy(x,y)
        y=y+8
        x=x-5
    print(y)
def run_tri_left():
    x=400
    y=570
    while(x>100):
        draw_boy(x,y)
        y=y-8
        x=x-5
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
    run_bottom()
    run_right()
    run_top()
    run_left()
    pass
def run_triangle():

    run_tri_bottom()
    run_tri_right()
    run_tri_left()

while True:
    run_circle()
    run_rectangle()
    run_triangle()

    break##임시로 넣음