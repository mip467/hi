#file = open ("writingData.txt","w")

#file.write("New Row")

#fileToWrite = open("writingData.txt","w")

#print 1 to 10 to writingData.txt

#for i in range (10):
#	content = str(i+1)
#	fileToWrite.write(content)
#	fileToWrite.write("\n")

#fileToWrite.close() 

#Challenge 2
#print even numbers from 1 to 1000
#fileToWrite = open("writingData.txt","w")

#for i in range (1001):
#	if i%2 == 0:
#		content = str(i)
#		fileToWrite.write(content)
#		fileToWrite.write("\n")

#fileToWrite.close() 


#Challenge 2
#print odd numbers from 1 to 1000
fileToWrite = open("writingData.txt","w")

for i in range (1001):
	if i%2 == 0:
		content = str(i)
		fileToWrite.write(content)
		fileToWrite.write("\n")

fileToWrite.close() #Challenge 2
#print even numbers from 1 to 1000
fileToWrite = open("writingData.txt","w")

for i in range (1001):
	if i%2 != 0:
		content = str(i)
		fileToWrite.write(content)
		fileToWrite.write("\n")

fileToWrite.close() 









