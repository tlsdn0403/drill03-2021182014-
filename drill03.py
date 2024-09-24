from pico2d import*

open_canvas()

grass=load_image('grass.png')
boy= load_image('character.png')

def run_circle():
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)

    pass
def run_rectangle():
    print('rectangle')
    pass


while True:
    run_rectangle()
    run_circle()
    break##임시로 넣음