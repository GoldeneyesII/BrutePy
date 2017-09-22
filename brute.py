#Python script to generate brute-forced word list

#Successfully appends list to file
#Successfully reads last line of file (without reading whole file)
#Need to create a "starting point" for generate
#Starting point includes how many chars are in word
#Starting point includes ord(char) for each char in word
#Generate continues generating from there (adding 1 to index 0)

def generate():
	global chars
	chars = [chr(i) for i in range(32,127)]

	my_list = []
	word = []

	i = 0
	while len(my_list)<= 50000:
		print(len(my_list))
		word.append('')
		counter(i, my_list, word)
		i += 1

	print("Length: {}".format(len(my_list)))
	print("Last Word: {}".format(word))
	record(my_list)
	print("Recorded")


def counter(indx, my_list, word):
	if len(my_list) > 500000:
		return
	elif indx == 0:
		for c in chars:
			word[0] = c
			my_list.append(''.join(word))
	else:
		for ch in chars:
			word[indx] = ch
			counter(indx - 1, my_list, word)

def starter(my_file):
	last_pos = get_last(my_file)
	print("Last String: {}".format(last_pos))
	#use ord() to get chr positions to continue at.
	word_pos = []
	for char in last_pos:
		word_pos.append(ord(char))
	print("Word Position: {}".format(word_pos))


def get_last(my_file):
	with open(my_file, "rb") as f:
		f.seek(-2, 2)
		while f.read(1) != b"\n":
			f.seek(-2, 1)
		return list(f.readline().decode().strip(" \n"))
	return ""

def record(my_list):
	with open("wordlist.gold", 'a') as f:
		for word in my_list:
			f.write("{}\n".format(word))

generate()
#starter("wordlist.gold")

#		word[indx] = chars[char]
#		char += 1
#		counter(char, indx -= 1)
