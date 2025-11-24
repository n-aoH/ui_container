from minescript_plus import *
from minescript import *
from time import *


helmet_indicator = "H"
leggings_indicator = "P"
chestplate_indicator = "C"
boots_indicator = "B"

durabilities = {
    "minecraft:elytra": ["ELY",432],
    "minecraft:diamond_boots": [boots_indicator,429],
    "minecraft:diamond_leggings": [leggings_indicator,495],
    "minecraft:diamond_chestplate": [chestplate_indicator,528],
    "minecraft:diamond_helmet": [helmet_indicator,363],
    "minecraft:netherite_boots": [boots_indicator,481],
    "minecraft:netherite_leggings": [leggings_indicator,555],
    "minecraft:netherite_chestplate": [chestplate_indicator,592],
    "minecraft:netherite_helmet": [helmet_indicator,407],
    "minecraft:iron_boots": [boots_indicator,195],
    "minecraft:iron_leggings": [leggings_indicator,225],
    "minecraft:iron_chestplate": [chestplate_indicator,240],
    "minecraft:iron_helmet": [helmet_indicator,165],
    "minecraft:golden_boots": [boots_indicator,91],
    "minecraft:golden_leggings": [leggings_indicator,105],
    "minecraft:golden_chestplate": [chestplate_indicator,112],
    "minecraft:golden_helmet": [helmet_indicator,77],
    "minecraft:chainmail_boots": [boots_indicator,195],
    "minecraft:chainmail_leggings": [leggings_indicator,225],
    "minecraft:chainmail_chestplate": [chestplate_indicator,240],
    "minecraft:chainmail_helmet": [helmet_indicator,165],
    "minecraft:copper_boots": [boots_indicator,143],
    "minecraft:copper_leggings": [leggings_indicator,165],
    "minecraft:copper_chestplate": [chestplate_indicator,176],
    "minecraft:copper_helmet": [helmet_indicator,121],

    "minecraft:leather_boots": [boots_indicator,65],
    "minecraft:leather_leggings": [leggings_indicator,75],
    "minecraft:leather_chestplate": [chestplate_indicator,80],
    "minecraft:leather_helmet": [helmet_indicator,55],

}
text1 = Hud.add_text("TEST",x=0,y=0,anchorX=.5,anchorY=.5,justifyX=0,justifyY=0,scale=.5,screens=["None"],alpha=255)


inv = ""
while True:
    if inv != player_inventory():
        inv = player_inventory()

        boots = boots_indicator
        pants = leggings_indicator
        chestplate = chestplate_indicator
        helmet = helmet_indicator


        for i in inv:
            if i.slot == 36:
                name = durabilities[i.item][0]
                max = durabilities[i.item][1]
                
                if i.nbt != None and "damage" in i.nbt:
                    damage = i.nbt.split('damage":')[1].split('}')[0]
                    damage = int(damage)
                else:
                    damage = 0
                boots = f"{name}:{max-damage}"

            if i.slot == 37:
                name = durabilities[i.item][0]
                max = durabilities[i.item][1]
                if i.nbt != None and "damage" in i.nbt:
                    damage = i.nbt.split('damage":')[1].split('}')[0]
                    damage = int(damage)
                else:
                    damage = 0
                pants = f"{name}:{max-damage}"

            if i.slot == 38:
                name = durabilities[i.item][0]
                max = durabilities[i.item][1]
                if i.nbt != None and "damage" in i.nbt:
                    damage = i.nbt.split('damage":')[1].split('}')[0]
                    damage = int(damage)
                else:
                    damage = 0
                chestplate = f"{name}:{max-damage}"

            if i.slot == 39:
                name = durabilities[i.item][0]
                max = durabilities[i.item][1]
                if i.nbt != None and "damage" in i.nbt:
                    damage = i.nbt.split('damage":')[1].split('}')[0]
                    damage = int(damage)
                else:
                    damage = 0
                helmet = f"{name}:{max-damage}"
        #echo(inv)
        try:
            Hud.update_text(text1,text=f"{boots} | {pants} | {chestplate} | {helmet}",x=0,y=-10,anchorX=0,anchorY=1,justifyX=-1,justifyY=-1,scale=.75,alpha=255,color=(255,255,255))
        except:
            pass
    
    sleep(.1)
