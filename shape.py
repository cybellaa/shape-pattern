import pgzrun
import random

WIDTH = 600
HEIGHT = 600

def draw():
    w = WIDTH
    h = HEIGHT - 500
    screen.fill("pink")
    screen.draw.text("cat",center=(WIDTH/2,HEIGHT/2),color = "purple")
    for i in range(25):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        r1=Rect((300,300),(w,h))
        r1.center=(300,300)
        screen.draw.filled_rect(r1,(r,g,b))
        w -=20
        h +=20





pgzrun.go()