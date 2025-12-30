from stats import *



def main():
    book = get_books_text("./books/frankenstein.txt")
    # print(book)
    words = count_words(book)
    # print(
    #     f"Found {words} total words"
    # )

    occurence = count_occurence(book)
    # print(occurence)


    occurence = sort(occurence)
    path = "./books/frankenstein.txt"
    printdic(occurence,path)



main()
