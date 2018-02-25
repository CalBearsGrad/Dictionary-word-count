# put your code here.

short_text = open("test.txt")
""" This function will display the words as keys and return the number of 
occurences as values"""


#create a function
def counting_words(text_file):
    #Created a new set
    word_counts = {}
    #Looping through each line in text file
    for line in text_file:
        #for each word in each line in text file
        line[0:-2]
        print line
        word_list = line.split(" ")
            #we will split each line by a space and add that word
        print word_list

        for word in word_list: # itterate throught the word_list
            low_word = word.lower()
            #if word is not in dictionary, set 0 and incrt 1
            #if word is in dict and grabs value, and increment 1
            word_counts[low_word] = word_counts.get(low_word, 0) + 1
    print word_counts
    return word_counts

            
    
    #print set_of_split_line
    #make a blank dictionary
    #in a loop...
        #Assign each set item as key in dictionary
        # set deflault value as 0     
    #print keys followed by the number of occurences

counting_words(short_text)
