class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author


# creating object
my_book = Book("The Midnight Library", "Matt Haig")

# accessing the attributes
print(my_book.name)
print(my_book.author)
