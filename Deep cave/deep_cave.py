import random ,sys, time


width = 62
pause_num = 0.05 
print (" Your are going to fall now ")
print("Press Ctrl + C to stop ")
time.sleep(2)


leftwidth = 20
gapwidth = 10

while True:

    right_width = width-gapwidth-leftwidth
    print(('#' * leftwidth) + ( ' ' * gapwidth) + ('#' * right_width))
    try:
        time.sleep(pause_num)

    except KeyboardInterrupt:
        sys.exit()

    diceroll = random.randint(1,6)
    if diceroll == 1 and leftwidth > 1:
        leftwidth = leftwidth -1 
    elif diceroll == 2 and leftwidth + gapwidth < width -1 :
        leftwidth = leftwidth + 1 
    else:
        pass     