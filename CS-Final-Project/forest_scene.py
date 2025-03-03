#Lukas
import random
import time
import func
import opening_scene
import battle_functions
import art_archive
import character_creation
import enemy_creation
import archetypes
import main
goblin=enemy_creation.Enemy("goblin",30,20,50,50)
if opening_scene.store=="Open it" and opening_scene.store_2=="Yes, its Questin Time!!!":
    print(art_archive.forest())
    print("you reach the base of dark evil forest")
    print("on the other side of the DARK EVIL FOREST is Polylandia's capital, Mustang Village")
    print("you start to have second thoughts of going through, after all there is nothing wrong with watching paint dry")
    store_3=func.user_input("Do you want to go through the DARK EVIL forest or return back home",["Go through the DARK EVIL FOREST","Return Home and watch paint dry"])
    if store_3=="Go through the DARK EVIL FOREST":
        print("you overcome your momentary cowardice and venture deeper into the forest")
        print(art_archive.time_passed())
        print("While you are casauly walking through the DARK EVIL FOREST")
        print("you oddly enough start to hear strange ominous sounds coming from the bushes")
        store_4=func.user_input("""you oddly enough start to hear strange ominous sounds coming from the bushes""",["investigate the bushes","ignore it"])
        if store_4=="investigate the bushes":
            print("Inspecting the bushes reveals a crouching goblin who was waiting to ambush you")
            print("You notice that while the goblin is weak he is very quick")
            print(art_archive.goblin())
            print("the goblin immediately attacks you")
            battle_functions.combat_loop(main.character1,goblin)

        if store_4=="ignore it":

            print("You walk past the ominous sounding bush, probably a bunny you tell yourself")
            print("just as you think that a goblin leaps out of the bushes and slashes you across the torso")
            print(art_archive.goblin())
            health_ambush=int((main.character1.get_health())/4)
            main.character1.set_health(health_ambush)
            print("you are severely wounded from the suprise attack your health is now only",health_ambush)
            battle_functions.combat_loop(main.character1, goblin)
        if goblin.get_health()==-10000:
            print("You successfully escaped the crafty goblin")
            print("after escaping the goblin you decide that you might as well keep on running all the way to Mustang Village")
        if goblin.get_health() == 0:
            print("The broken corpse of the goblin stands before you")
            print("While staring at the goblin you notice 2 things on the corpse")
            print("The goblins heavy but razor sharp blade and also the goblins surprisingly light but thinner armor")
            stat_boost_1=func.user_input("You notice you can only  carry one, which do you take",["The sword (+10 strength)","The boots (+10 dexterity)"])
            if stat_boost_1=="The sword (+10 strength)":
                new_strength=main.character1.get_strength()+10
                main.character1.set_strength(new_strength)
            else:
                new_dexterity=main.character1.get_dexterity()+10
                main.character1.set_dexterity(new_dexterity)
            print("After your near death encounter with the goblin you realize that maybe you should be walking through the")
            print("DARK EVIL FOREST OF DOOM")
            print("all by yourself, so you quickly hurry to Mustang Village!")








    else:
        print("Your Inner Coward reveals itself")
        print("but you are filled with anticpation to watch paint dry")
        print("and lead a very unfulfilling life...")

