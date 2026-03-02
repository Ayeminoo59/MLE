
"""
class main_door:
    def __init__(self,name):
        print("Welcome from my home")
        self.name = name 
    def search_room(self):
        print(f"welcome from my {self.name}")
    def inheritance(self):
        self.search_room()
# create obj
ayeminoo = main_door("ayeminoo")
ayeminoo.inheritance()


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def get_description(self):
        return f"{self.title} by {self.author}"

# create object
ayeminoo_book = Book("ayeminoo", "love you", "$8999")
print(ayeminoo_book.get_description())

"""