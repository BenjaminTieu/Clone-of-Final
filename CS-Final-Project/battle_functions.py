import random
import time
import character_creation
import enemy_creation
Test_Character=character_creation.Character("Character",100000,40,30,10,"test")
Test_Enemy=enemy_creation.Enemy("Enemy",100000,124,12,20)
# This function will convert a string into a float if possible. If it is not possible, it will return None
def str_to_float(phr1: str) -> float or None:
   try:
       return float(phr1)
   except ValueError:
       return None


# This function will ask the user for an input. If the input is not an expected value, then the user will be re-prompted
def user_input(phr1:str, accepted_choices: list):
   check = False
   # This while loop will run while check is False
   while check is False:
       print("Error. You have entered an invalid option.")
       val = input(phr1)
       for val2 in accepted_choices:
           # If statement to check if the input is a valid number
           if str_to_float(val) is not None:
               if str_to_float(val) == val2:
                   return val
           # If statement to check if the input is a valid String
           if isinstance(phr1, str) and isinstance(accepted_choices[0], str):
               if val.upper() == val2.upper():
                   return val.lower()



def percent_chance(chance):
    value_generated = random.randint(0,100)
    return value_generated<=chance



def attack(attacker)->int:
    attack_value=(random.randint(int(attacker.get_strength()*.25), int(attacker.get_strength()*.5)))
    return attack_value

def hit_victim(victim,attacker):
    current_hp=victim.get_health()-attack(attacker)
    victim.set_health(current_hp)
    return current_hp

def dodge(character):
    if percent_chance(character.get_agility()):
        return 0
    else:
        return 1

def run(character):
    if percent_chance(character.get_agility()/2):
        return 0#Sucessful Runaway
    else:
        return 1


def combat_loop(character,enemy):
    while character.get_health()>0 and enemy.get_health()>0:
        store=user_input("Do you want to attack or run?", ['attack','run'])
        if store=='attack':
            if dodge(enemy)==0:
                time.sleep(1)
                print("{} dodged".format(enemy.get_name()))
                if dodge(character)==0:
                    time.sleep(1)
                    print("{} dodged the {} attack, your health is now {}".format(character.get_name(),enemy.get_name(),character.get_health()))
                else:
                    character_hp_after_attack=hit_victim(character,enemy)
                    time.sleep(1)
                    print("{} failed to dodge {},{} has {} health left".format(character.get_name(),enemy.get_name(),character.get_name(),character_hp_after_attack))

            else:
                time.sleep(1)
                print("{} failed to dodge".format(enemy.get_name()))
                enemy_hp_after_attack=hit_victim(enemy, character)
                time.sleep(1)
                print("{} health is now".format(enemy.get_name()),enemy_hp_after_attack)
                if dodge(character)==0:
                    time.sleep(1)
                    print("{} dodged the {} attack, your health is now {}".format(character.get_name(),enemy.get_name(),character.get_health()))
                else:
                    character_hp_after_attack=hit_victim(character,enemy)
                    time.sleep(1)
                    print("{} failed to dodge {},{} has {} health left".format(character.get_name(),enemy.get_name(),character.get_name(),character_hp_after_attack))



        if store=='run':
            if run(character)==0:
                enemy.set_health(0)
                print("{} ran away from the {}".format(character.get_name(),enemy.get_name()))
            elif run(character)==1:
                print("{} failed to run away".format(character.get_name()))#Failed to Run Away
                character_hp_after_attack = hit_victim(character, enemy)
                print("{} attacked {},{} has".format(enemy.get_name(), character.get_name(), character.get_name()),
                      character_hp_after_attack)
print(combat_loop(Test_Character,Test_Enemy))






