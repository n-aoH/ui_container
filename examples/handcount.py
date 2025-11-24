from minescript_plus import *
from minescript import *
from time import *





text1 = Hud.add_text("",x=0,y=0,anchorX=.5,anchorY=.5,justifyX=0,justifyY=0,scale=1,screens=["all"])
hand = ""

def loop():
    global hand
    while True:
            if hand != player_inventory():
                
                inv = player_inventory()
                hand = player_hand_items()
                count = 0

                for itemstack in inv:
                      if itemstack.item in str(hand.main_hand):
                        count += itemstack.count
                try:
                  Hud.update_text(text1,text=str(count),x=0,y=-30,anchorX=.5,anchorY=1,justifyX=0,justifyY=-1,scale=1,alpha=140,color=(255,255,255))
                except:
                    pass

            
sleep(.2)
loop()
