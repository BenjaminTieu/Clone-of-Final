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
import stor

goblin=enemy_creation.Enemy("goblin",30,20,20,20)
if opening_scene.store=="Open it" and opening_scene.store_2=="Yes, it's Questin' Time!!!":
    print(art_archive.forest())
    print("You reach the entrance of the DARK EVIL FOREST.")
    print("On the other side of the DARK EVIL FOREST is Polylandia's capital, Mustang Village.")
    print("You start to have second thoughts about going through.")
    print("After all, there is nothing wrong with watching paint dry.")
    store_3=func.user_input("Do you want to go through the DARK EVIL forest or return back home?", stor.forest_scene_l1)
    if store_3=="Go through the DARK EVIL FOREST":
        print("You overcome your momentary cowardice and venture deeper into the forest.")
        print(art_archive.time_passed())
        print("While you are casually strolling along the DARK EVIL FOREST,")
        print("the bushes start to rustle and you hear strange noises coming from them.")
        store_4=func.user_input("What do you choose to do?",stor.forest_scene_l2)
        if store_4=="Investigate the bushes":
            print("As you near the bushes, you notice a dark green figure hidden between the leaves.")
            print("You recognize this creature as a goblin! It was likely hiding in the bushes to ambush you!")
            print("The goblin is not strong but it is very quick.")
            print(art_archive.goblin())
            print("The goblin immediately attacks you!")

        if store_4=="Ignore it":
            print("You walk past the ominous sounding bush, \"Probably a bunny,\" you tell yourself.")
            print("Suddenly, a goblin leaps out of the bushes and slashes you across the torso!")
            print(art_archive.goblin())
            health_ambush=int((main.character1.get_health())/4)
            main.character1.set_health(health_ambush)
            print("You are severely wounded from the surprise attack. Your health is now only",health_ambush)

        battle_functions.combat_loop(main.character1, goblin)
        func.prompt1()

        if goblin.get_health()==-10000:
            print("You successfully escaped the crafty goblin")
            print("After escaping the goblin, you decide that you might as well keep on running all the way to Mustang Village.")
        if goblin.get_health() == 0:
            print("The broken corpse of the goblin stands before you.")
            print("While staring at the goblin, you notice 2 items on its corpse.")
            print("The goblin's razor sharp blade and also the goblins surprisingly light but thin armor.")
            stat_boost_1 = func.user_input("You notice you can only carry one, which do you take?",stor.forest_scene_l3)
            stat_boost_1 = func.confirm(stat_boost_1, "Are you sure you want to choose the [{}]?",
                                        "Which item do you want to keep?",
                                        stor.forest_scene_l3, stor.forest_scene_dict1)
            if stat_boost_1=="Short Sword":
                new_strength = main.character1.get_strength()+15
                new_dexterity = main.character1.get_dexterity()+5
                new_agility = main.character1.get_agility()+5
                main.character1.set_strength(new_strength)
                main.character1.set_dexterity(new_dexterity)
                main.character1.set_agility(new_agility)
            else:
                new_dexterity = main.character1.get_dexterity()+10
                new_agility = main.character1.get_agility()+10
                main.character1.set_dexterity(new_dexterity)
                opening_scene.starting_health = new_health = main.character1.get_health()+20
                main.character1.set_agility(new_agility)

            print("After your near death encounter with the goblin you realize that")
            print("maybe you shouldn't be walking through the ")
            print("DARK EVIL FOREST OF DOOM")
            print("all by yourself, so you quickly hurry to Mustang Village.")








    else:
        print("Your inner cowardice reveals itself,")
        print("but you are filled with an unyielding desire to watch paint dry")
        print("and lead a very unfulfilling life...")

