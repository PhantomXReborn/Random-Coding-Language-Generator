'''
Program: Random-Coding-Language-Generator
Purpose: Generate a random language and project idea
Language: Python
Author: Reece Hannah
'''

# Imports
import os
import random
import linecache
from time import sleep

# clear_screen Function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading():
    for i in range(5):
        for j in range(3):
            print(j*"*")
            sleep(0.1)
            clear_screen()

        clear_screen()

# Menu Screen
def mainMenu():
    print("\n\tRandom Coding Language Generator")
    print("\n\nMade by: Reece Hannah")

    print("\n\nChoose a difficulty range for your program: ")
    print("1. BEGINNER PROJECTS")
    print("2. INTERMEDIATE PROJECTS")
    print("3. ADVANCED PROJECTS")
    choice = int(input(("---> ")))

    if not input("Press ENTER to generate an idea (or type anything to exit): "):
        return choice
    else:
        print("Exiting program.")

# RCLG Program
def RCLG(choice):
    with open("codeLang.txt", 'r') as file:
        lines1 = len(file.readlines())

    with open("ideas.txt", 'r') as file:
        lines2 = len(file.readlines())

    print("Language: ")
    print(linecache.getline('codeLang.txt', random.randint(0, lines1-1)))
    print("\n\n")

    print("Code Idea: ")
    if choice == 3:
        print(linecache.getline('ideas.txt', random.randint(92, lines2-1)))
    elif choice == 2:
        print(linecache.getline('ideas.txt', random.randint(42, 87)))
    else:
        print(linecache.getline('ideas.txt', random.randint(0, 43)))


match mainMenu():
    case 1:
        loading()
        RCLG(1)
    case 2:
        loading()
        RCLG(2)
    case 3:
        loading()
        RCLG(3)

