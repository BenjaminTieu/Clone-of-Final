import random
import sys
import time
import func
import art_archive
import character_creation
import enemy_creation
import archetypes
import game_runner
import main
Test_Character=character_creation.Character("Character",archetypes.Archetypes('Thief'))
Test_Enemy=enemy_creation.Enemy("Enemy",10,5,12,20)
# This function will convert a string into a float if possible. If it is not possible, it will return None

def random_int_generator()->int:# Generates a random integer from 1 to 4
    int_made= random.randint(1,4)
    return int_made#return is a integer from 1 to 4


def percent_chance(chance : int)->bool:#This function generates a random integer from 1 to 100 and will compare it to the already input chance value. Returns True if Chance is greater than value generated
    value_generated = random.randint(0,100)
    return value_generated<=chance
#Maybe update chance-agility?


#returns a attack value which is randomized from 25% of the attackers strength attribute to 150% of the players strength attribute, returns the attack value
def attack(attacker)->int:
    attack_value=(random.randint(int(attacker.get_strength()*.25), int(attacker.get_strength()*1.5)))
    if percent_chance(attacker.get_dexterity()):
        attack_value*=2
        print("{} did a CRITICAL HIT".format(attacker.get_name()))
    return attack_value
#function basically subtracts the victims health before the attack minus the attackers attack value, this creates current_hp which is set as the players new health
def hit_victim(victim,attacker)->int:
    current_hp=victim.get_health()-attack(attacker)
    if current_hp<0:
        current_hp=0
    victim.set_health(current_hp)
    return current_hp#New HP is a Integer
#utiliezes the percent chance function where the players agility is chance, if value generated is less than chance you successfully dodge which returns a 0, if you fail to dodge returns a 1
def dodge(character)->int:
    if percent_chance(character.get_agility()):
        return 0#Succesful dodge
    else:
        return 1#Failed to dodge


def run(character)->int:#Uses percent chance function with the charachters agility value as the chance value, will return 0 if charachter agility greater than random number generated will return a 0 indictating a sucessful runaway attempt
#If agility is less than random number generated will be a unsuccessful run away attempt
    if percent_chance(character.get_agility()/2):
        return 0#Sucessful Runaway
    else:
        return 1#Unsucessful escape


def combat_loop(character,enemy):#A combat loop between the enemy and character. Will continue to loop until either the character or enemies health is 0
    #Both the enemy and character are classes. The user can choose the stats for the character while the enemies stats are prebuilt in
    # The user has 2 options to attack or run. Running will use the run function while attacking will first use dodge function on the enemy.
    #If enemy dodge fails the enemy will lose health, if it suceed the enemy will "dodge" the attack and loose no health. No matter if the enemy fails or succeeds to dodge
    #The enemy wil retaliate with a attack which the player will have the chance to dodge using the dodge function and just as before If they succeed no damage taken, if they fail damage taken
    #If player fails run they automatically will take damage with no ability to dodge or retailate
    #If they succeed to runaway it will end the combat encounter. This is done here by just setting the enemies health to -10000
    #after every loop of attack or run you will be given the same options again until you or the enemies health value gets less than 0
    while character.get_health()>0 and enemy.get_health()>0:
        store=func.user_input("Do you want to attack or run?", ['attack','run'])
        if store=='attack':
            if dodge(enemy)==0:#Enemy successful dodge
                time.sleep(1)
                print("{} dodged {}'s attack".format(enemy.get_name(),character.get_name()))
                if dodge(character)==0:#Player successful dodge
                    time.sleep(1)
                    print("{} dodged the {} attack, your health is now {}".format(character.get_name(),enemy.get_name(),character.get_health()))
                    print("The {}'s health is still {}".format(enemy.get_name(),enemy.get_health()))
                else:#player failed to dodge enemies attack
                    print("{} failed to dodge {} attack".format(character.get_name(),enemy.get_name()))
                    character_hp_after_attack=hit_victim(character,enemy)#Player looses health aft failing to dodge
                    time.sleep(1)
                    print("{} has {} health left".format(character.get_name(),character_hp_after_attack))
                    print("The {}'s health is still {}".format(enemy.get_name(), enemy.get_health()))

            else:#Enemy fails to dodge
                time.sleep(1)
                print("{} failed to dodge".format(enemy.get_name()))
                enemy_hp_after_attack=hit_victim(enemy, character)#Enemy looses health to charachter hit
                if enemy_hp_after_attack<=0:#
                    enemy_hp_after_attack=0#Ensures that that the enemy will never have a health lower than 0
                time.sleep(1)
                print("{}'s health is now".format(enemy.get_name()),enemy_hp_after_attack)
                if dodge(character)==0 and enemy_hp_after_attack>0:#Player successfully dodges enemies attack after the enemy fails to dodge
                    time.sleep(1)
                    print("{} dodged the {} attack, your health is now {}".format(character.get_name(),enemy.get_name(),character.get_health()))
                elif dodge(character)==1 and enemy_hp_after_attack>0:#Player fails to dodge after enemy fails to dodge
                    print("{} failed to dodge {} attack".format(character.get_name(), enemy.get_name()))
                    character_hp_after_attack=hit_victim(character,enemy)#Player looses health
                    time.sleep(1)
                    print("{} has {} health left".format(character.get_name(),character_hp_after_attack))




        if store=='run':#If player chooses to 'run'
            if run(character)==0:#successful run away
                enemy.set_health(-10000)#sets enemy health to a large value below zero which the player can never reach, this is to end the loop
                print("{} ran away from the {}".format(character.get_name(),enemy.get_name()))
            elif run(character)==1:#If player fails to run away
                print("{} failed to run away".format(character.get_name()))#Failed to Run Away
                print(art_archive.trip())#ascii art recieved from the art archive
                character_hp_after_attack = hit_victim(character, enemy)# player health after attack by enemy, no chance to dodge
                print("{} attacked {},{} has".format(enemy.get_name(), character.get_name(), character.get_name()),
                      character_hp_after_attack)

        if character.get_health()<=0:# Death screens, randomized , will happen when the players health is less than or equal to 0!
            character.set_health(0)
            num=random_int_generator()#random number generator from 1 to 4
            if num==1:
                print("The {} obliterated {} skull".format(enemy.get_name(),character.get_name()))
                print(art_archive.player_death_img())
            if num == 2:
                print("The {} ate {} alive".format(enemy.get_name(),character.get_name()))
                print(art_archive.player_death_img())
            if num == 3:
                print("Your spine was snapped in half by the {}".format(enemy.get_name()))
                print(art_archive.player_death_img())
            if num == 4:
                print("{} isn't getting up...".format(character.get_name()))
                print(art_archive.player_death_img())
            sys.exit()
        if enemy.get_health()<=0:#If enemy health less than 0 returns this message
            enemy.set_health(0)
            print("{} defeated the {}".format(character.get_name(),enemy.get_name()))




