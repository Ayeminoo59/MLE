class Book:
    def __init__(self, title, author, price):
        print(f"DEBUG: Creating book with title={title}, author={author}, price={price}")
        self.title = title
        self.author = author
        self.price = price
    
    def get_description(self):
        print(f"DEBUG: get_description called")
        print(f"DEBUG: self.title = {self.title}")
        print(f"DEBUG: self.author = {self.author}")
        result = f"{self.title} by {self.author}"
        print(f"DEBUG: result = {result}")
        return result

# create object with debugging
ayeminoo_book = Book( "love you", "$8999")
print(ayeminoo_book.get_description())

# Error example for debugging practice
try:
    bad_book = Book("", "", "")
    print(bad_book.get_description())
except Exception as e:
    print(f"ERROR: {e}")
    print("This is how we catch and debug errors!")
