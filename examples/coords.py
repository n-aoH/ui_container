from minescript_plus import *
from minescript import *
from time import *
from math import floor, ceil
import threading



SCALING = .5
xanchor = 1
yanchor = 1
justifyy = -1
justifyx = 1
X = 0
Y = -20


text1 = Hud.add_text("TEST",x=0,y=0,anchorX=.5,anchorY=.5,justifyX=0,justifyY=0,scale=1,screens=["None"],alpha=255)

toggle = 0



def keythread(): # currently no way to auto get dimension so this is close
    global toggle
    with EventQueue() as event_queue:
        event_queue.register_key_listener()
        while True:
            event = event_queue.get()
            if event.key == 320 and event.action == 0:
                toggle = toggle +1
                if toggle > 2:
                    toggle = 0
                

threading.Thread(target=keythread,daemon=True).start()

while True:
    coords = get_player().position
    coords[0] = floor(coords[0])
    coords[1] = floor(coords[1])
    coords[2] = floor(coords[2])

    try:
        if toggle == 0:
            Hud.update_text(text1,text=str(coords),x=X,y=Y,anchorX=xanchor,anchorY=yanchor,justifyX=justifyx,justifyY=justifyy,scale=SCALING,alpha=255,color=(255,255,255))
        elif toggle == 1:
            coords[0] = ceil(coords[0]/8)

            coords[2] = ceil(coords[2]/8)

            Hud.update_text(text1,text=str(coords),x=X,y=Y,anchorX=xanchor,anchorY=yanchor,justifyX=justifyx,justifyY=justifyy,scale=SCALING,alpha=255,color=(255,100,100))
        elif toggle == 2:
            coords[0] = (coords[0]*8)

            coords[2] = (coords[2]*8)

            Hud.update_text(text1,text=str(coords),x=X,y=Y,anchorX=xanchor,anchorY=yanchor,justifyX=justifyx,justifyY=justifyy,scale=SCALING,alpha=255,color=(100,255,100))
    except:
        pass
