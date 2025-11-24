from minescript import *
from minescript_plus import *
from time import sleep

text1 = Hud.add_text("",x=0,y=0)

old_num_players = 0

while True:
    num_entities = len(get_entities())-1
    num_players = len(get_players())-1

    
    try:
        Hud.update_text(text1,f"E: {num_entities} P: {num_players}",0,-10,anchorX=1,anchorY=1,justifyX=1,justifyY=1,scale=.5)
        if num_players != old_num_players:
            Util.play_sound(Util.get_soundevents().BELL_BLOCK, Util.get_soundsource().BLOCKS)
        old_num_players = num_players
    except:
        pass
    sleep(0.1)
