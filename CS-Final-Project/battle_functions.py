import random
import time

import art_archive
import character_creation
import enemy_creation
import archetypes
import main
Test_Character=character_creation.Character("Character",archetypes.Archetypes('Thief'))
Test_Enemy=enemy_creation.Enemy("Enemy",10,5,12,20)
# This function will convert a string into a float if possible. If it is not possible, it will return None
def str_to_float(phr1: str) -> float or None:
   try:
       return float(phr1)
   except ValueError:
       return None

def random_int_generator()->int:
    int_made= random.randint(1,4)
    return int_made


def percent_chance(chance):
    value_generated = random.randint(0,100)
    return value_generated<=chance
#Maybe update chance-agility?



def attack(attacker)->int:
    attack_value=(random.randint(int(attacker.get_strength()*.25), int(attacker.get_strength()*1.5)))
    return attack_value

def hit_victim(victim,attacker):
    current_hp=victim.get_health()-attack(attacker)
    victim.set_health(current_hp)
    return current_hp

def dodge(character):
    if percent_chance(character.get_agility()):
        print(character.get_health())
        return 0
    else:
        print(character.get_health())
        return 1


def run(character):
    if percent_chance(character.get_agility()/2):
        return 0#Sucessful Runaway
    else:
        return 1


def combat_loop(character,enemy):
    while character.get_health()>0 and enemy.get_health()>0:
        store=main.user_input("Do you want to attack or run?", ['attack','run'])
        if store=='attack':
            if dodge(enemy)==0:
                time.sleep(1)
                print("{} dodged {}'s attack".format(enemy.get_name(),character.get_name()))
                if dodge(character)==0:
                    time.sleep(1)
                    print("{} dodged the {} attack, your health is now {}".format(character.get_name(),enemy.get_name(),character.get_health()))
                    print("The {}'s health is still {}".format(enemy.get_name(),enemy.get_health()))
                else:
                    character_hp_after_attack=hit_victim(character,enemy)
                    time.sleep(1)
                    print("{} failed to dodge {} attack,{} has {} health left".format(character.get_name(),enemy.get_name(),character.get_name(),character_hp_after_attack))
                    print("The {}'s health is still {}".format(enemy.get_name(), enemy.get_health()))

            else:
                time.sleep(1)
                print("{} failed to dodge".format(enemy.get_name()))
                enemy_hp_after_attack=hit_victim(enemy, character)
                if enemy_hp_after_attack<=0:
                    enemy_hp_after_attack=0
                time.sleep(1)
                print("{}'s health is now".format(enemy.get_name()),enemy_hp_after_attack)
                if dodge(character)==0 and enemy_hp_after_attack>0:
                    time.sleep(1)
                    print("{} dodged the {} attack, your health is now {}".format(character.get_name(),enemy.get_name(),character.get_health()))
                elif dodge(character)==1 and enemy_hp_after_attack>0:
                    character_hp_after_attack=hit_victim(character,enemy)
                    time.sleep(1)
                    print("{} failed to dodge {},{} has {} health left".format(character.get_name(),enemy.get_name(),character.get_name(),character_hp_after_attack))
        if character.get_health()<=0:
            num=random_int_generator()
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
        if enemy.get_health()<=0:
            enemy.set_health(0)
            print("{} defeated the {}".format(character.get_name(),enemy.get_name()))
            battle_val=1
            return battle_val



        if store=='run':
            if run(character)==0:
                enemy.set_health(-10000)
                print("{} ran away from the {}".format(character.get_name(),enemy.get_name()))
                battle_val = 2
                return battle_val
            elif run(character)==1:
                print("{} failed to run away".format(character.get_name()))#Failed to Run Away
                print(art_archive.trip())
                character_hp_after_attack = hit_victim(character, enemy)
                print("{} attacked {},{} has".format(enemy.get_name(), character.get_name(), character.get_name()),
                      character_hp_after_attack)






