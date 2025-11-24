import minescript as ms
import minescript_plus as msp
from time import sleep
import math


# Based on code from @thevoid_d, I just ported it over to use minecraft time. They're pretty cool :)


Hud = msp.Hud()

index = Hud.add_text(
    text="",
        x=0,
        y=0,
)

while True:

    
    time = (ms.world_info().day_ticks + 6000) % 24000
    hour = math.floor(time/1000)
    minute = math.floor(((time%1000) * 60) / 1000)
    
    hour = str(hour)
    minute = str(minute)

    if len(hour) == 1:
        hour = "0"+str(hour)
    if len(minute) == 1:
        minute = "0"+str(minute)
    try:
        Hud.update_text(
            index= index,
            text=f"{hour}:{minute}",
            x=0,
            y=0,
            anchorX=1,
            anchorY=1,
            justifyX=1,
            justifyY=1
    
        )
    except:
        pass
    sleep(0.1)
