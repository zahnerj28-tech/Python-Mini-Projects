# Title:  	Mad Libs
# Author: 	Josh Zahner 
# Purpose:	Creates a story based on verbs, adjectives and nouns that the user inputs
# Usage:	Practice python functions and reusability

# Notes:	Create Mad Libs style game where user inputs certain types of words
#			Story doesn't have to be too long but should have some sort of story line.

# Subgoals:
#			If user puts in a name, change first letter to capital letter
#			Change the word "a" to "an" when next word in sentence begins with a vowel



'''

Your hands feel warm.  You wake up and open your eyes slowly.  While lying down you raise your head.  Glancing down
at your hands and see a frog licking your fingers.  It croaks.  Suddenly it jumps onto your chest.  It stares at your 
forehead.  You decide to kiss it.  The frog is enveloped by an intense white light.  It flickers for a while and is 
now only flickering.  Once the light is gone, the frog that was there before is a beautiful human looking back at you.  
The person says, "Hello my name is J, and I love you."  

You married this person and now you have 8 kids.  And a pet frog.

'''

'''

Your hands feel __(adjective describing touch)__.  You wake up and open your eyes slowly.  
While lying down you raise your head.  Glancing down at your __(body part)__ and see [a] __(animal*)__ licking your fingers.  
It __(animal sound)__.  Suddenly it __(verb describing movement and ends in s)__ onto your chest.  It stares at your 
__(body part)__.  You decide to kiss it.  The __(animal*)__ is enveloped by an intense __(color)__ light.  
It flickers for a while and is now only flickering dimly.  Once the light is gone, the __(animal*)__ that was there before 
is a __(a word to describe your crush)__ human looking back at you.  

The person says, "__(greeting)__ my name is __(name of your crush/lover)__, and I love you."  

You married this person and now you have __(number)__ kids.  And a pet __(animal*)__.

'''

from time import sleep

#Define Start Time 
now = datetime.datetime.now()

def madlibs():
	print("Madlibs starting, please enter the words below: ")
	print("------------------------------------------------")
	touchAdj = input("An adjective describing touch: ")
	bodyPart = input("A body part: ")
	animal = input("An animal: ")
	animalSound = input("A sound an animal makes: ")
	color = input("A color: ")
	name = input("The name someone you like: ")
	adjective = input("An adjective to describe someone you like: ")
	number = input("A number from one to 50: ")
	greeting = input("A greeting to your good friend: ")
	verbMove = input("A verb describing movement that ends in 's' (e.g., jumps, floats, runs): ")
	adverbKiss = input("An adverb (a word ending in -ly, like quickly or gently): ")

	print("\n------------------------------------------------")
	print("Word gathering complete.  Creating story...")
	sleep(5)
	print("\nYour skin feels " + touchadj + "as you wake up inside a strange mental chamber.")
	sleep(2)
	print("You rub your " + bodypart + " and realize you're aboard a spaceship drifting through the stars.")
	sleep(2)
	print("Suddenly, a small " + animal + " floats into the room, wearing a tiny space helmet.")
	sleep(2)
	print("It makes a strange noise: '" + animalSound + ",' which echoes through the cabin.")
	sleep(2)
	print("Before you can react, the creature " + vertMove + " through zero gravity toward you.")
	sleep(1)
	print("You watch " + adverbKiss + " as the " + animal + " begins to glow with a pulsing " + color + " light.")
	sleep(2)
	print("The glow intensifies until the entire chamber is filled with swirling colors.")	
	sleep(2)
	print("When the light fades, the " + animal + " is gone-replaced by a " + adjective + " human.")
	sleep(2)
	print("Together, you explore distant planets, discovering new worlds and raising " + number + "cosmic children-")
	sleep(2)
	print("The person says, \"" + greeting + " my name is " + name + ", and I love you.\"")
	sleep(2)
	print("All while your old friend, the " + animal + ", watches over your adventures from the stars.")
	sleep(2)

	print(("\nTime to generate story: " + str(datetime.datetime.now()-now)
	print("\nThe End.\n\n")

madlibs()



