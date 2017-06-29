# #Challenge1 count number of lines in a file
# file = open ("randomData.txt","r")

# count = 0

# content = file.readline()

# while (content):
# 	count+=1
# 	content = file.readline()
	
# print count

#Challenge2 count number of words in a file
file = open ("shortStory.txt","r")

wordCount = 0

content = file.readline()

while (content):
	wordsInLine = content.split()
	wordCount+=len(wordsInLine)
	content = file.readline()

print wordCount