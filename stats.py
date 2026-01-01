def get_books_text(file_path):
    with open (file_path) as f:
        file_contents = f.read()
        return file_contents


def count_words(file):
    words = file.split()
    return len(words)

def count_occurence(file):
    text = file.lower()
    occurence_dict = {}
    for letter in text:
        if not letter.isalpha():
            continue
        occurence_dict[letter] = occurence_dict.get(letter, 0) + 1

    return occurence_dict

def sort(occurrence_dict):
    items = []
    for key, value in occurrence_dict.items():
        if key.isalpha():
            items.append({"char": key, "num": value})

    # sort by frequency descending, then by character ascending for ties
    items.sort(key = sort_on, reverse=True)
    return items
               
def sort_on(items):
    return items["num"]



def printdic(path):
    file_contents = get_books_text(path)
    words = count_words(file_contents)
    occurence = count_occurence(file_contents)
    items = sort(occurence)
    print(
        f"============ BOOKBOT ============ \n"
        f"Analyzing book found at {path}...\n"
        f"----------- Word Count ----------\n"
        f"Found {words} total words\n"
        f"--------- Character Count -------"
    )
    for dict in items:
        print(f"{dict['char']}: {dict['num']}")
    
    print("============= END ===============")