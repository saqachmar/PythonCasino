#This program simulates the roulette game in a casino
# Author Soufiane Aqachmar
from math import ceil
from random import randrange
import os

print("Welcome to our Casino; You are about to start playing roulette...")
eligible=True
pas=1
while pas==1:
	print "How much money do you have?"
	money=raw_input()   # used raw_input() instead of input() just not to force users to enter string in  quotes ''
	try:
		money=int(money)
		assert money>0
	except ValueError:
		print "You did not enter a number; Please try again"
		continue
	except AssertionError:
		print "Are you kidding me ? you should enter a positive amount of money"
		continue
	print "Good boy, You are starting the game with an amount of ", money, " dollars"
	pas=0
	
while eligible is True: #eligible untill runs out of money or decides to quit
	choice_number=-1 
	while choice_number < 0 or choice_number > 49:
		choice_number=raw_input("What number you wanna play? ( between 1 and 49)")
		try:
			choice_number=int(choice_number)
			assert choice_number > 0 and choice_number < 50
		except ValueError:
			print "your choice should be a number( integer)"
			continue
		except AssertionError:
			print "your choice should be between 1 and 49"
			continue
	money_to_play=money+1
	while money_to_play>money:
		money_to_play=raw_input("What is your bet?")
		try:
			money_to_play=int (money_to_play)
			assert money_to_play <= money
		except ValueError:
			print "your bet should be a number"
			continue
		except AssertionError:
			print "you cannot bet an amount greater than the money you have"
			continue 	
	winner= randrange(50)
	print "The winning number is",winner
	if winner==choice_number:
		money=money+(money_to_play*3)
		print " Congratulations! You won",money_to_play*3," dollars, and thus your total money becomes",money,"dollars"
		print "DO you want to continue playing? ( Y/N)"
		con=raw_input()
		if con=="n" or con=="N":
			eligible=False
	
 	elif winner%2==choice_number%2:
		money=money-ceil(money_to_play*0.5)
		print "Your choice is of the of the same color as the winning number; you get back fifty percent"
		print "you get back", ceil(money_to_play*0.5)," dollars, and thus your total amount becomes",money,"dollars"
		con=raw_input("DO you want to continue? (Y/N)")
		if con=="n" or con=="N":
			eligible=False
	else:
		money=money-money_to_play
		print " Sorry, you lost",money_to_play,"and thus, your total money becomes",money
		if money<=0:
			print "You are screwed! you have 0 dollars left"
			eligible=False
		else:
			con=raw_input("Do you want to continue?(Y/N)")
			if con=="n" or con=="N":
				eligible=False
			
print "Bye Bye...Hope to see you soon around"
os.system("pause")	

		
