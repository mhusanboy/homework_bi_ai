class BookNotFoundException(Exception):
    def __init__(self, msg: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg 
    
    def __str__(self):
        return self.msg 


class BookAlreadyBorrowedException(Exception):
    def __init__(self, msg: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg 
    
    def __str__(self):
        return self.msg 

class MemberLimitExceededException(Exception):
    def __init__(self, msg: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = msg 
    
    def __str__(self):
        return self.msg 

class Book:
    count = 0
    def __init__(self, name, author, is_borrowed = False):
        self.name = name
        self.author = author 
        self.is_borrowed = is_borrowed
        self.id = Book.count
        Book.count += 1
    
    def __str__(self):
        return f"{self.id}, {self.name}, {self.author}"

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.author}"
    



class Member:
    count = 0
    def __init__(self, name, borrowed_books = []):
        self.name = name 
        self.id = Member.count
        Member.count += 1
        if len(borrowed_books) > 3:
            raise MemberLimitExceededException('Cannot initialize object with exceeded limit')
        self.borrowed_books = borrowed_books 
    
    def __str__(self):
        return f"{self.name}"

    def borrowBook(self, book):
        self.borrowed_books.append(book)

    def returnBook(self, book):
        self.borrowed_books.remove(book)


class Library:
    
    def __init__(self):
        self.books = dict()
        self.members = dict()

    def addBook(self, *books):
        for book in books:
            self.books[book.id] = book
    
    def addMember(self, *members):
        for member in members:
            self.members[member.id] = member

    def getMember(self, name : str):
        for member in self.members.values():
            if name == member.name:
                return member.id 
        
        raise Exception('Member not found.')
    
    def getBook(self, name :str):
        for book in self.books.values():
            # print(book.name, )
            if book.name == name:
                return book.id 
        
        raise BookNotFoundException('Book not found.')

    def borrowBook(self, book_name : str, member_name : str):
        book_id = self.getBook(book_name)
        member_id = self.getMember(member_name)
    
        if self.books[book_id].is_borrowed:
            raise BookAlreadyBorrowedException('Book is already borrowed.')
        
        if len(self.members[member_id].borrowed_books) >= 3:
            raise MemberLimitExceededException('Member exceeded the limit for borrowed books')
        
        self.members[member_id].borrowBook(self.books[book_id])
        self.books[book_id].is_borrowed = True 

    def returnBook(self, book_name : str, member_name : str):
        book_id = self.getBook(book_name)
        member_id = self.getMember(member_name)
    
        if self.books[book_id].is_borrowed:
            raise BookAlreadyBorrowedException('Book is already borrowed.')
        
        if len(self.members[member_id].borrowed_books) >= 3:
            raise MemberLimitExceededException('Member exceeded the limit for borrowed books')
             
        self.members[member_id].returnBook(self.books[book_id])
        self.books[book_id].is_borrowed = False 

def run():
    library = Library()
    book1 = Book("Harry Potter", "J. Rowling")
    book2 = Book("Shum Bola", "G'afur G'ulom")
    book3 = Book("The Alchemist", "Paulo Coelho")
    book4 = Book("Game of thrones", "R. Martin")
    member1 = Member("Husanboy")
    member2 = Member("Hasanboy")
    member3 = Member("Salohiddin")
    library.addBook(book1,book2,book3,book4)
    library.addMember(member1,member2,member3)
    library.borrowBook(member_name="Husanboy",book_name="The Alchemist")
    library.borrowBook(member_name="Husanboy",book_name="Harry Potter")
    library.borrowBook(member_name="Hasanboy",book_name="Harry Potter")
    library.borrowBook(member_name="Husanboy",book_name="The Hobbit")
    library.returnBook(member_name="Husanboy",book_name="The Alchemist")

if __name__ == "__main__":
    run()   