import time, math
posb=[0,0.1]
iposb=[0,0]
moveb=[0,0]
screen=["0","0","0","0","0","0","0","0","0","0"]
a=""
for k in range(10):
    screen=[0,0,0,0,0,0,0,0,0,0]
    move=input("점프하려면 j, 이동하려면 r, l")
    if move!=move.replace("j","a"):
        moveb[1]=1.5
        posb[1]=0.1
    if move!=move.replace("r","a"):
        moveb[0]=moveb[0]+1
    if move!=move.replace("l","a"):
        moveb[0]=moveb[0]-1
    while moveb[0]>0.1 or moveb[0]<-0.1 or posb[1]>0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        posb[0]+=moveb[0]
        posb[1]+=moveb[1]
        moveb[1]-=0.2
        moveb[0]*=0.8
        if posb[0]<0:
            posb[0]=0
            moveb[0]=0
        if posb[0]>9:
           posb[0]=9
           moveb[0]=0
        if posb[1]<0:
           posb[1]=0
        iposb[0]=int(posb[0])
        iposb[1]=int(posb[1])
        if iposb[1]<10:
            for j in range(10):
                for i in range(10):
                    
                    if iposb[0]==i and iposb[1]==j:
                        a+="2"
                    else:
                        a+="1"
                screen[j]=a
                a=""
        else:
            for j in range(10):
                for i in range(10):
                    a+="1"
                screen[j]=a
                a=""
        for i in range(10):
            print(screen[9-i].replace("1","□").replace("2","■"))
        if posb[1]<0:
                posb[1]=0
        time.sleep(0.05)
from pynput import keyboard

print('Press s or n to continue:')

with keyboard.Events() as events:
    # Block for as much as possible
    event = events.get(1e6)
    if event.key == keyboard.KeyCode.from_char('s'):
        print("YES")