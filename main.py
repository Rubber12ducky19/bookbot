def get_book_text(file_path):
    with open(file_path) as f: #opens the file as f, closing at the end of function
        file_contents = f.read() #makes file_contents into a string
    return (file_contents)

def main():
    import sys #allows access to system level
    if len(sys.argv) <= 1: #checks if there is one or less arguements
        print("Usage: python3 main.py <path_to_book>") #give instructions
        sys.exit(1) #exits the script with stdout(1)
    relative_path = sys.argv[1] # gets the second arguement from the command line
    file_contents = get_book_text(relative_path) #gets the contents of the file as a string
    #print(file_contents) : Printed the contents of file
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at " + (relative_path) + "...")
    print("----------- Word Count ----------")
    get_num_words(file_contents)
    print("--------- Character Count -------")
    count_chars_to_sorted_list(count_characters(file_contents))
    print("============= END ===============")
from stats import get_num_words #imports the get_num_words from stats.py
from stats import count_characters
from stats import count_chars_to_sorted_list

main()