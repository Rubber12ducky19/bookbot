def get_num_words(contents):
    sum = 0 # declares an integer as sum
    words = contents.split() #turns contents into a list
    for word in words: # for each word in the words list
        sum += 1
    print (f"Found {sum} total words")

def count_characters(contents):
    lower_case_contents = contents.lower() #turns contents into lower case letters
    letters = {} # creates a dictionary to store character values
    for character in lower_case_contents: #for each character in lower_case_contents
        if character not in letters: # if there is no key with character
            letters[character] = 1 # creates one and starts it at 1
        else:
            letters[character] += 1 # adds 1 to an existing character
    #print(letters)   
    return(letters)

def count_chars_to_sorted_list(dict):
    result = [] #creates a list to store dictionaries
    for char,count in dict.items(): # creates the values char & count for each character in the dictionary
        char_dict = {"char": char, "num": count} #formats the list for key -> value
        result.append(char_dict) # adds to the list
    def sort_on(d): #declares a function to sort based on "num" value
        return d["num"]
    result.sort(reverse=True, key=sort_on) #sorts the list in reverse based on the value
    for char_data in result: #for each data value in the list
        char = char_data["char"] #makes sure we are going for "char" values
        if char.isalpha(): # if it's a letter
            count = char_data["num"] #collects the value of "num"
            print(f"{char}: {count}") #prints the key->values in a format we want
    #print(result)
    return result
