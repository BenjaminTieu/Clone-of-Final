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
main.character1.set_health(opening_scene.starting_health)
cpt_arm=enemy_creation.Enemy("Captain Armstrong",20,15,50,80)
if forest_scene.store_3=="Go through the DARK EVIL FOREST":
    print("after a fortnight you reach Mustang Village")
    print("the ghost town you see before you was a FAR CRY from the Vibrant bustling village of your youth")
    print("you notice a ominous looking mountain in the background with a castle overlooking Mustang village")
    print("you suspect DARK LORD JOE MAMA and the princess is up there in that castle")
    print( "an old man approaches you from one of the empty houses")
    store_7=func.user_input("hello traveller have you come to save the kingdom and the princess from the dark lord JOE MAMA",["Yes, i am here to depose the tyrant","Shut up old man and mind your business"])
    if store_7=="Yes, i am here to depose the tyrant":
        print("That's good to hear, though traveller watch out, DARK LORD JOE MAMA has sent one of his allies, CAPTAIN ARMSTRONG into town")
        print("I dont know who they are or how they look but they uses deceit to kill any who oppose JOE MAMA")
        print("Be on guard traveller, I wish you luck!")
    else:
        print("Fine you ingrateful brat")
    print("The old man runs back into the house")
    print("you start to walk deeper into the ghost town but THEN......")
    print("your stomach rumbles")
    print("after having eaten only nuts and berries for the past few days you long for a warm meal")
    print("you spot a rather empty but still open tavern")
    store_8=func.user_input("Should you go to the tavern for a warm meal or continue on your journey",["I long for a warm meal, surely the princess can wait a few more hours to be saved","Time is of the esenence, I must continue on my quest."])
    if store_8=="I long for a warm meal, surely the princess can wait a few more hours to be saved":
        print("you head toward the tavern")
        print("Entering the tavern you are greeted with the strong smell of fish and cat fur but also a warmth that you havent felt since you left your hut ")
        print("The tired and fat innkeeper takes notice of your prescence")
        print("Welcome to Mustangs Village's one and only Tavern, what can I do for you?")
        print("The innkeeper hands you a wooden board, you notice it is actually a menu")
        store_9=func.user_input("What should you get?",["STEW!","FISH"])
        print("after some time you get your meal")
        if store_9=="STEW":
            print("You take a bite and realize that this is PROBALLY ONE OF THE WORST STEWS you have ever had in your life")
            print("It is so terrible in fact that it makes you feel much weaker (-10 health permanently)")
            loose_health=main.character1.get_health()-10
            main.character1.set_health(loose_health)
        else:
            print("You take on a single bite of the fish and realize that this is the BEST MEAL you have ever had in your life")
            print("it imbues your body with new found energy that you have lacked this entire journey(+10 health)")
            print("you will remember this meal for a very long time!")
            gain_health=main.character1.get_health()+10
            main.character1.set_health(gain_health)
        updated_health=main.character1.get_health()
        print("While eating your meal a adorable house cat curiously walks up to you")
        print("it is probably the most adorable thing you have ever seen in your entire life")
        print("The car walks up sheepishly to your leg and starts meowing at you almost asking for you to pet him")
        store_10=func.user_input("Should you pet the Adorable little cat",["Of course, Come here little dude","No get away you ugly rat","Attack the Cat"])
        if store_10=="Of course, Come here little dude":
            print("While reaching for the cat...")
            print("the cat lunges and mauls you face")
            print("you barely manage to pull it away from your newly mauled face when the cat says")
            print("Fool you have fallen for my ruse. I, CAPTAIN ARMSTRONG will rip you apart and deliver your head to JOE MAMA")
            print("And i shall turn your broke body into CAT NIP!!!!!")
            health_ambush = int((main.character1.get_health()) / 4)
            main.character1.set_health(health_ambush)
            print("you are severely wounded from Capatin Armstrong's Mauling attack your health is now only", health_ambush)
            battle_functions.combat_loop(main.character1,cpt_arm)
        if store_10=="No get away you ugly rat":
            print("You kick the ugly little rat away from you")
            print("The cat hisses at you and says")
            print("Why you little shit, No one ever disrespects Captain Armstrong!")
            print("I will shred you into peices and inform JOE MAMA about your pitiful death")
        else:
            print("You draw your weapon and swing it the innocent cat")
            print("Guilt immediately overcomes, why would you ever harm such a magestic creature")
            print("You realize that you are a monster, a pyschopath, a VILLIAN")
            print("Your truly are the scum of the earth!")
            print("The cat wimpers in pain and hastily backs away from you")
            print("Why you pyschopath, how dare you attack me!")
            print("I,Captain Armstrong was planning on mauling you and you foiled my plans!!!")
            print("While i appreciate a fellow pyschopath, I must kill you as there is only enough space for 1 pyschopath in mustang village!")
            print("You notice the cat is now limping after you intial attack")
            wound_enemy=int(cpt_arm.get_health()/4)
            cpt_arm.set_health(wound_enemy)
            wound_enemy_agility=int(cpt_arm.get_agility()/4)
            cpt_arm.set_agility(wound_enemy_agility)



        battle_functions.combat_loop(main.character1, cpt_arm)
        if cpt_arm.get_health()==0:
            print("The now defeated Captain Armstrong's lies broken at your feat")
            print("The innkeeper walks over to you")
            print("Thank you for saving my establishment from that fiend, he had kept murdering my all my customers")
            print("As a reward for accomplishments please take one of my valuables!!")
            store_11=func.user_input("What should you take",["The HEAVY ARMOR (+40 Health,+25 strength,-25 Agility)","The Light Armor (+10 Health, +20 Agility,"])
            if store_11=="The HEAVY ARMOR (+40 Health,+25 strength,-25 Agility)":
                main.character1.set_health(updated_health)
                health_up=main.character1.get_health()+50
                main.character1.set_health(health_up)
                strength_up=main.character1.get_strength()+25
                main.character1.set_strength(strength_up)
                dec_agil=main.character1.get_agility()-25
                main.character1.set_agility(dec_agil)
                print("the armor's weight restricts your movements but gives you also a newfound strength")
            else:
                main.character1.set_health(updated_health)
                health_up = main.character1.get_health() + 10
                main.character1.set_health(health_up)
                inc_agil = main.character1.get_agility() + 25
                main.character1.set_agility(inc_agil)
                print("The suprisingly light armor provides a little bit of extra protection while still being very flexible!")
            end_of_Mustang_Village_health=main.character1.get_health()
            print(main.character1.get_health())
            print("after your encounter in the tavern you decide it is best to continue your journey and save the princess")
            print("you now much climb")
            print("DOOM MOUNTAIN")
        else:
            print("You barely are able to escape from the fericous feline, you hightail it out of the tavern")
            print("and keep running till DOOM MOUNTAIN")

    else:
        print("You leave Mustang Village tired and hungry yet determined to save the princess")
