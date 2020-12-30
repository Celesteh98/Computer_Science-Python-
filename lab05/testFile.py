#testFile
from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

# Book Test
def test_getTitle():
    b0 = Book("Cujo", "King, Stephen", 1981)
    assert b0.getTitle() == "Cujo"

def test_getAuthor():
    b1 = Book("The Shining", "King, Stephen", 1977)
    assert b1.getAuthor() == "King, Stephen"

def test_getYear():
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b2.getYear() == 2011

def test_getBookDetails():
    b3 = Book("Rage", "King, Stephen", 1977)
    assert b3.getBookDetails() == "Title: Rage, Author: King, Stephen, Year: 1977"
    

#BookCollection Tests

b0 = Book("Cujo", "King, Stephen", 1981)
b1 = Book("The Shining", "King, Stephen", 1977)
b2 = Book("Ready Player One", "Cline, Ernest", 2011)
b3 = Book("Rage", "King, Stephen", 1977)
        
def test_isEmpty():
    bookCollection = BookCollection()
    assert bookCollection.isEmpty() == True
    bookCollection.insertBook(b0)
    bookCollection.insertBook(b1)
    assert bookCollection.isEmpty() == False

def test_insertBook():
    bookCollection = BookCollection()
    bookCollection.insertBook(b0)
    bookCollection.insertBook(b1)
    assert bookCollection.getAllBooksInCollection() == 'Title: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n'

def test_getBookByAuthor():
    bookCollection = BookCollection()
    bookCollection.insertBook(b2)
    bookCollection.insertBook(b3)
    assert bookCollection.getBooksByAuthor("KING, Stephen") == 'Title: Rage, Author: King, Stephen, Year: 1977\n'

def test_getAllBooksInCollection():
    bookCollection = BookCollection()
    bookCollection.insertBook(b0)
    bookCollection.insertBook(b1)
    bookCollection.insertBook(b2)
    bookCollection.insertBook(b3)
    assert bookCollection.getAllBooksInCollection() == 'Title: Ready Player One, Author: Cline, Ernest, Year: 2011\nTitle: Rage, Author: King, Stephen, Year: 1977\nTitle: The Shining, Author: King, Stephen, Year: 1977\nTitle: Cujo, Author: King, Stephen, Year: 1981\n'

#BookCollectionNode Tests

def test_getData():
    bookCollectionNode = BookCollectionNode(b0)
    assert bookCollectionNode.getData() == b0

def test_getNext():
    bookCollectionNode = BookCollectionNode(b0)
    assert bookCollectionNode.getNext() == None

def setData():
    bookCollectionNode = BookCollectionNode(self.b1)
    assert bookCollectionNode.setData(self.b1) == Book("The Shining", "King, Stephen", 1977)
        
def setNext():
    bookCollectionNode = BookCollectionNode(self.b3)
    assert bookCollectionNode.setNext(self.b3) == Book("Rage", "King, Stephen", 1977)  
