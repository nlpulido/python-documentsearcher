def main():
	# standard code in order to create a list of all files
	from os import listdir 
	from os.path import isfile, join

	mypath = "/Users/neil/Documents/cs110 /projects/project3/docs/" # path to the folder that contains all the text files
	allfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

	wordDct = {} # initializes the huge dictionary containing words from all doc files

	for file in allfiles: # for each file
		if file !=".DS_Store": # if file is not DS_Store
			currentFile = open(mypath+file, "r") # opens each file in loop
			fileLines = currentFile.readlines() # creates a list of lines in the current file
			for line in fileLines: # for each line in the file
				split = line.split() # splits the line in order to go word for word
				for word in split: # for each word in the line
					loweredWord = word.lower() # lowers the word by default
					if loweredWord in wordDct: # if the word exists already in the huge dictionary
						wordDct[loweredWord].append(line) # append the line containing the word to the word's list of lines (that contain the word)
					else: # if the word doesn't already exist in the huge dictionary
						wordDct[loweredWord] = [] # initializes the word to have an empty list as a value
						wordDct[loweredWord].append(line) # appends the current line containing the word into the list of lines (that contain the word)
			currentFile.close() # closes the file after it's done adding each word to the huge dictionary

	# creates the dictionary summary file
	summaryFile = open("dictionary-summary.txt", "w") # opens it for writing
	importantKeyPairs = {} # creates an empty dictionary of those KeyPairs that will be written into dictionary-summary.txt
	for aword in wordDct: # for each word in the huge dictionary
		if len(aword) > 6: # if the key is longer than six characters
			importantKeyPairs[aword] = wordDct[aword] # add the word and key value pair to the important Key Pairs dictionary
	importantKeyPairs = str(importantKeyPairs) # makes the important Key Pairs dictionary a string
	summaryFile.write(importantKeyPairs) # writes it to the dictionary-summary.txt
	summaryFile.close() # closes it

	# opens searchResults.txt file
	searchFile = open("searchResults.txt", "w")

	# asks a user for a word to search in the dictionary
	userWord = input("Enter a keyword and I will print out all lines with that word.") 
	userWord = userWord.lower() # initializes word to be lower by default
	if userWord in wordDct: # if the word is in the dictionary
		results = str(wordDct[userWord])
		searchFile.write(userWord) # writes search word
		searchFile.write(":") # formats the value
		searchFile.write(results) # writes all lines containing the word to searchResults.txt
	else: # if not in the dictionary
		searchFile.write("I could not find your keyword in the dictionary.") # writes out error message to searchResults.txt
	# closes searchResults file
	searchFile.close()
	
main()