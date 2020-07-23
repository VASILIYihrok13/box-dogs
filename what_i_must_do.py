import random


def random_choice(my_favorites):
	''' повертає рандомне значення зі списку'''
	print(random.choice(my_favorites))

def main():
	
	user_things = []
	while True:
		thing = input('What you can do now?: ')
		if not thing:
			break
		user_things.append(thing)
	return user_things

random_choice(main())


