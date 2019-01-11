import time

x = 0
y = 0
velx = 1
vely = 0
accy = .1
jumping = True


while True:
    if x % 100 == 0:
        jumping = True
        vely = -2
    x += velx
    y += vely
    if jumping:
        vely += accy
        if y >= 0:
            y = 0
            vely = 0
            jumping = False



    print(f"{x}, {y}")
    time.sleep(.1)