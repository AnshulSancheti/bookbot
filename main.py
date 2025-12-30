def main():
    book = get_books_text("/home/intelligentape/bookbot/books/frankenstein.txt")
    print(book)



def get_books_text(file_path):
    with open (file_path) as f:
        file_contents = f.read()
        return file_contents
    
main()
