from minescript import *
from minescript_plus import *
import ui_container



SHOW_UI_SCRIPTS = False


texts = []
old_texts = []
def get_texts():
    global texts
    texts = []

    if SHOW_UI_SCRIPTS:
        for i in ui_container.scripts:
            texts.append(["UI",i,None])
        


    for i in job_info():
        if "__eval_pyjinn_script__" not in i.command:
            texts.append([i.job_id,i.command,i.parent_job_id])

    



hudelements = []

spacing = 5
sleep(1)
while True:
    try:
        get_texts()

        if old_texts != texts:
            count = 0

            for i in texts:

                if count >= len(hudelements):
                    hudelements.append(Hud.add_text(f"{i[0]} - {i[1]}",x=0,y=spacing+(count*spacing),justifyX=1,justifyY=1,anchorX=1,anchorY=0,scale=.5))


                else:
                    Hud.update_text(hudelements[count],f"{i[0]} - {i[1]}",x=0,y=spacing+(count*spacing),justifyX=1,justifyY=1,anchorX=1,anchorY=0,scale=.5)

                count += 1

        old_texts = texts
    except:
        pass
    sleep(1)
