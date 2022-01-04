class Books:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # toString() method
    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is deleted")


my_book = Books("Game of Thrones", "George R R Martin", 750)
print(my_book)
print(len(my_book))
del my_book
