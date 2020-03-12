

def word_wrap(strng, length):

	wrd_lst = list(strng.split(" "))

	new_list = []

	new_string = ""

	for i in wrd_lst:
		if new_string == "":
			new_string = i
		else:

			if len(new_string + " " + i) <= length:
				new_string = new_string + " " + i
			else:
				new_list.append(new_string)
				new_string = i

	new_list.append(new_string)

	for i in new_list:
		print(i)


word_wrap("Luna and Tiger are two very great kitties", 10)