members = open('list.txt',"r")
lines = members.readlines()

for word in lines:
	thisline = word.split(" ")
	print word