from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
radian = 0


while (True):
        while(x < 800):
            clear_canvas_now()
            x += 2
            grass.draw_now(400, 30)
            character.draw_now(x, 90)
            delay(0.01)
        while ( x >= 400):
             clear_canvas_now()
             x -= 2
             y += 2
             grass.draw_now(400, 30)
             character.draw_now(x, y)
             delay(0.01)
        while ( x >= 0):
             clear_canvas_now()
             x -= 2
             y -= 2
             grass.draw_now(400, 30)
             character.draw_now(x, y)
             delay(0.01)
        while ( x <= 400):
             clear_canvas_now()
             x += 2
             grass.draw_now(400, 30)
             character.draw_now(x, 90)
             delay(0.01)
        while(radian < 360):
             clear_canvas_now()
             grass.draw_now(400, 30)
             character.draw_now(400 + 210*math.cos((270 + radian)/360*2*math.pi),
                          300 + 210*math.sin((270 + radian)/360*2*math.pi))
             delay(0.01)
             radian += 2
        radian = 0

        

close_canvas()
