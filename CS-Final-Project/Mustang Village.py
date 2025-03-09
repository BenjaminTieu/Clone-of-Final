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
import forest_scene
import stor

main.character1.set_health(opening_scene.starting_health)
cpt_arm=enemy_creation.Enemy("Captain Armstrong",20,15,50,80)
if forest_scene.store_3=="Go through the DARK EVIL FOREST":
    print("After a fortnight, you reach Mustang Village.")
    print("The ghost town you see before you was a FAR CRY from the Vibrant bustling village of your youth.")
    print("You notice an ominous castle that sits atop a towering mountain that overlooking Mustang village.")
    print("You suspect DARK LORD JOE MAMA and the princess are up in that castle")
    func.prompt1()
    print("An old man approaches you from one of the empty houses")
    time.sleep(0.5)
    store_7=func.user_input("Hello traveller have you come to save the kingdom and the princess from the dark lord JOE MAMA?", stor.mustang_village_l1)
    if store_7=="Yes, I am here to depose the tyrant":
        print("Then I must warn you, traveler. DARK LORD JOE MAMA has sent one of his allies, CAPTAIN ARMSTRONG, into town.")
        print("I dont know who they are or how they look but they use deceit to kill any who oppose JOE MAMA")
        print("Please be on guard. I wish you luck!")
    else:
        print("Fine, you ingrate.")
        print("I hope the dark lord eats your organs for breakfast.")
    print("The old man runs back into the house.")
    time.sleep(0.5)
    print("You start to walk deeper into the ghost town but THEN......")
    func.prompt1()
    print("Your stomach rumbles")
    time.sleep(1.5)
    print("After having eaten only nuts and berries for the past few days, you long for a warm meal.")
    print("You spot a rather empty but still open tavern")
    store_8=func.user_input("Should you go to the tavern for a warm meal or continue on your journey?",stor.mustang_village_l2)
    if store_8=="I long for a warm meal, surely the princess can wait a few more hours to be saved":
        print("You enter the tavern.")
        time.sleep(0.5)
        print("You are greeted with the strong smell of fish and cat fur, but also a warmth that you haven't felt since you left your hut ")
        print("A tired man with a generous belly who stands at the center of the tavern takes notice of your presence.")
        print("Welcome to Mustangs Village's one and only Tavern, what can I do for you?")
        print("The innkeeper hands you a wooden board, you notice it is actually a menu")
        store_9=func.user_input("What should you get?",stor.mustang_village_l3)
        store_9 = func.confirm(store_9, "Are you sure you want to choose the [{}]?",
                               "What should you get?", stor.mustang_village_dict1)
        time.sleep(1)
        print("After some time, you get your meal")
        if store_9=="STEW":
            print("You take a bite and realize that this is the WORST stew you have ever had.")
            print("In fact, it is so terrible that it makes you feel much weaker (-10 health permanently)")
            print("Maybe, listen to me next time?")
            lose_health=main.character1.get_health()-10
            main.character1.set_health(lose_health)
        else:
            print("You take a single bite of the fish and realize that this is the BEST meal you have ever had.")
            print("It imbues your body with new found energy that you have lacked this entire journey (+10 health)")
            print("You will remember this meal for a very long time!")
            gain_health=main.character1.get_health()+10
            main.character1.set_health(gain_health)
        updated_health=main.character1.get_health()
        func.prompt1()
        print("While eating your meal, an adorable house cat curiously walks up to you.")
        print("It is probably the most adorable thing you have ever seen.")
        print("The cat sheepishly walks up to your leg and starts purring at you, almost asking for you to pet him.")
        store_10=func.user_input("Should you pet the adorable little cat", stor.mustang_village_l4)
        if store_10=="Of course! Come here little dude":
            print("As you reach for the cat...")
            time.sleep(1)
            print("the cat lunges at you and mauls your face")
            print("you barely manage to pull it away from your newly mauled face when the cat says")
            print("Fool! You have fallen for my ruse. It is me, CAPTAIN ARMSTRONG all along!")
            print("I will rip you apart and deliver your head to JOE MAMA")
            print("And i shall turn your desecrated body into CAT NIP!!!!!")
            health_ambush = int((main.character1.get_health()) / 4)
            main.character1.set_health(health_ambush)
            print("you are severely wounded from Captain Armstrong's Mauling attack your health is now only", health_ambush)
        elif store_10 == "No, get away from me you flea-stained rodent":
            print("You kick the ugly, little rat away from you.")
            print("The cat hisses at you and says")
            print("Why you little shit! No one ever disrespects me, Captain Armstrong!")
            print("I will shred you into pieces and inform JOE MAMA about your pitiful death")
        else:
            print("You draw your weapon and swing at the innocent cat.")
            print("Guilt immediately overcomes you, why would you ever harm such a pure and majestic creature?")
            print("You realize that you are a monster, a psychopath, a VILLAIN.")
            print("Your truly are the scum of the earth, worse than even the dark lord himself!")
            print("The cat whimpers in pain and hastily backs away from you.")
            print("Why you psychopath, how dare you attack me!")
            print("I, Captain Armstrong was planning on mauling you when you least expected, but you foiled my plans!!!")
            print("While I appreciate a fellow psychopath, I must kill you as there is only enough space for 1 psychopath in Mustang Village!")
            print("You notice the cat is now limping after your initial attack.")
            wound_enemy=int(cpt_arm.get_health()/4)
            cpt_arm.set_health(wound_enemy)
            wound_enemy_agility=int(cpt_arm.get_agility()/4)
            cpt_arm.set_agility(wound_enemy_agility)
        func.prompt1()


        battle_functions.combat_loop(main.character1, cpt_arm)

        func.prompt1()
        if cpt_arm.get_health()==0:
            print("The now defeated Captain Armstrong lies desecrated at your feet.")
            print("The innkeeper walks over to you.")
            print("Thank you for saving my establishment from that fiend. He had kept murdering all of my customers.")
            print("Please, choose one of these as a reward.")
            store_11=func.user_input("Which should you take?",["The HEAVY ARMOR (+40 Health,+25 strength,-25 Agility)","The Light Armor (+10 Health, +20 Agility,"])
            if store_11=="The HEAVY ARMOR (+40 Health,+25 strength,-25 Agility)":
                main.character1.set_health(updated_health)
                health_up=main.character1.get_health()+50
                main.character1.set_health(health_up)
                strength_up=main.character1.get_strength()+25
                main.character1.set_strength(strength_up)
                dec_agil=main.character1.get_agility()-25
                main.character1.set_agility(dec_agil)
                print("The armor's weight restricts your movements, but gives you also a newfound strength")
            else:
                main.character1.set_health(updated_health)
                health_up = main.character1.get_health() + 10
                main.character1.set_health(health_up)
                inc_agil = main.character1.get_agility() + 25
                main.character1.set_agility(inc_agil)
                print("The surprisingly light armor provides a little bit of extra protection while still being very flexible!")
            end_of_Mustang_Village_health=main.character1.get_health()
            print(main.character1.get_health())
            print("You decide it is now best to continue your journey and save the princess")
            print("You now must climb")
            print("DOOM MOUNTAIN")
        else:
            print("You are barely able to escape from the ferocious feline. You hightail it out of the tavern")
            print("and keep running till DOOM MOUNTAIN")

    else:
        print("You leave Mustang Village tired and hungry, yet determined to save the princess")
