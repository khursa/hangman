import random

words = (
	 'light', 'profit', 'girl', 'heat', 'woman', 'child', 'friend', 'neighbor', 'guest', 'chief', 'client', 'parents',
     'beach', 'ocean', 'rate', 'teacher', 'sound', 'change', 'front', 'artist', 'bird', 'mouse', 'monkey', 'hospital',
     'discount', 'relation', 'servant', 'driver', 'insurance', 'lawyer', 'actor', 'police', 'market', 'company', 'snow',
     'punishment', 'iron', 'bit', 'forest', 'field', 'socket', 'bread','lunch', 'spring', 'winter', 'something','flower', 
     'garden', 'hate', 'price', 'judge', 'orange', 'honey', 'picture', 'length', 'depth', 'delivery', 'story', 'road',
     'bridge', 'side', 'stage', 'sugar', 'turn', 'wax', 'money', 'party', 'kitchen', 'mountain', 'machine', 'brother',
     )

hangman_1 = [
['		     _________'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============\n']
]

hangman_2 = [
['		     _________'],
['		     |       |'],
['		     |       |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============']
]

hangman_3 = [
['		     _________'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============']
]

hangman_4 = [
['		     _________'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		    / \      |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============']
]

hangman_5 = [
['		     _________'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		    /|\      |'],
['		     |       |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============']
]

hangman_6 = [
['		     _________'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		    /|\      |'],
['		     |       |'],
['		    / \      |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============']
]

hangman_7 = [
['		     _________'],
['		             |'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		    /|\      |'],
['		     |       |'],
['		    / \      |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============\n\n\n\n\n']
]

hangman_8 = [
['		     _________'],
['		             |'],
['		             |'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		    /|\      |'],
['		     |       |'],
['		    / \      |'],
['		             |'],
['		             |'],
['		             |'],
['		==============\n\n\n\n\n']
]

hangman_9 = [
['		     _________'],
['		             |'],
['		             |'],
['		             |'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		    /|\      |'],
['		     |       |'],
['		    / \      |'],
['		             |'],
['		             |'],
['		==============\n\n\n\n\n']
]

hangman_10 = [
['		     _________'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		     |       |'],
['		     |       |'],
['		     0       |'],
['		    /|\      |'],
['		     |       |'],
['		    / \      |'],
['		             |'],
['		==============\n\n\n\n\n']
]

hangman_11 = [
['		     _________'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		   \ \ / /   |'],
['		==============\n\n\n\n\n']
]

hangman_12 = [
['		     _________'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		  GAME OVER! |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		             |'],
['		==============\n\n\n\n\n']
]

hangman_13 = [
['                     _________'],
['                             |'],
['                             |'],
['                             |'],
['                             |'],
['           --------          |'],
['          | Hooray! \        |'],
['           ----------\       |'],
['                      0/     |'],
['                     /|      |'],
['                      |      |'],
['                     / \     |'],
['                ==============']
]

hangman = (hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7, hangman_8, hangman_9, hangman_10, hangman_11, hangman_12)
h = 0

while True:
	start = input('Enter "OK" and start fun game: ' )
	if start == 'OK'.lower():
		break
print('\n' * 20)

keyword = (random.choice(words))
key_list = []
key_list = keyword[:]

for row in hangman_1:
    for elem in row:
        print(elem, end=' ')
    print()

sum_of_letters = len(keyword)
unsuitable_letters = []
underline = str('_'*sum_of_letters)
underlist = []
underlist = list(underline[:])
end_of_game = False

while h < 6:
	if underlist.count('_') == 0:
		print('\n' * 30)
		for n in hangman_13:
			for row in n:
				for elem in row:
					print(elem, end='')
				print()
				break

	if underlist.count('_') == 0:
		print('\nCongratulations! You won!!!')
		end_of_game = True
	if end_of_game != True:
		print(str(sum_of_letters) + ' letters:')

	if underlist.count('_') != 0:
		for m in underlist:
			for elem in m:
				print(elem, end=' ')

	if h <= 0 and underlist.count('_') != 0:
		print('\n')
	elif underlist.count('_') == 0:
		break
	else:
		print('\nUnsuitable letters: %s' % ', ' .join(unsuitable_letters))

	letter = input('Guess this word! Enter your letter: ' )
	print('\n' * 30)
	for j in [key_list]:
		if letter in key_list:
			for n in hangman[h]:
				for row in n:
					for elem in row:
						print(elem, end='')
					print()
			print('\nCongratulations! You guessed the letter!')
			position = key_list.index(letter)
			underlist.pop(position)
			underlist.insert(position, letter)
			continue
		else:
			h = h + 1
			for n in hangman[h]:
				for row in n:
					for elem in row:
						print(elem, end='')
					print()
			print('\nThe word doesn`t contain your letter.')
			unsuitable_letters.append(letter)

from time import sleep
seconds_left = 5

if end_of_game == False:
	while seconds_left > 0:
		print('\n' * 30)
		h = h + 1
		for p in hangman[h]:
			for row in p:
				for elem in row:
					print(elem, end='')
				print()
		seconds_left -= 1
		try:
			sleep(1)
		except:
			pass
		continue

print('The word:', keyword)