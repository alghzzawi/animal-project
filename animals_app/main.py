import json
import pprint
from animals import Animals

animal = Animals()
# print(Animals.instance_caunt)
# name_Python = 'Spider Ball Python'

def user_interface():
    '''
    A class to get info based on a animals name
    Enter the full name for animal and the applction 
    will show for you some information for this animal
    chosse the The information you want to know about it
    the steps to start the application:
    1- enter animal name
    2- read the options and choose number
    3- enter q if you want to exit
    '''
    print('************************************')
    print('** Welcome to Animale application **')
    print('************************************')
    animals=input('Enter animal name: ')
    animal.set_name(animals)
    option=input(f'Options: \nEnter 1 to know whit color {animal.get_full_name()} have \nEnter 2 to know length {animal.get_full_name()} \nEnter 3 to know the life span of a {animal.get_full_name()} \nEnter 4 to know where do {animal.get_full_name()} live \nEnter 5 to find out which species the {animal.get_full_name()} belongs to \nEnter q to exit the program \n> ')

    while option != 'q':
        if option == '1':
            try:
                print(f'{animal.get_full_name()} have {animal.get_color()} color')
            except:
                print(f'we can`t find color for {animal.get_full_name()}')
                pass
        elif option == '2':
            try:
                print(f'length {animal.get_full_name()} is {animal.get_length()}')
            except:
                print(f'we can`t find length for {animal.get_full_name()}')
                pass
        elif option == '3':
            try:
                print(f'The lifespan of a {animal.get_full_name()} of {animal.get_lifeSpan()}')
            except:
                print(f'we can`t find the lifespan  for {animal.get_full_name()}')
                pass
        elif option == '4':
            try:
                print(f'{animal.get_full_name()} live in {animal.get_locations()}')
            except:
                print(f'we can`t find where {animal.get_full_name()} live')
                pass
        elif option == '5':
            try:
                print(f'{animal.get_full_name()} belongs to {animal.get_animale_belongs()} family')
            except:
                print(f'we can`t find where {animal.get_full_name()} belongs to')
                pass
        elif option == 'q':
            return
        option=input('> ')

user_interface()