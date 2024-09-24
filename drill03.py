from pico2d import*
import math
open_canvas()

grass=load_image('grass.png')
boy= load_image('character.png')

def run_circle():

    r=300
    cx=800//2 ##화면 크기의 절반
    cy=600//2

    for degree in range(0,360,3):
        theta=math.radians(degree)
        x=r*math.cos(theta)+cx
        y=r*math.sin(theta)+cy

        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.1)
    pass
def run_rectangle():
    print('rectangle')
    pass


while True:
    run_rectangle()
    run_circle()
    break##임시로 넣음