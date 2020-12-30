#BookCollection
from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        curr  = self.head
        counts = 0
        while curr != None:
            counts += 1
            curr = curr.getNext()
        return counts

    def insertBook(self, book):
        curr = self.head
        prev = None
        stop = False
        while curr != None and not stop:
            if curr.getData() > book:
                stop = True
            else:
                prev = curr
                curr =  curr.getNext()

        temp = BookCollectionNode(book)

        if prev == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(curr)
            prev.setNext(temp)
                

    def getBooksByAuthor(self,author):
        curr = self.head
        listbook = ""
        while curr !=  None:
            if curr.getData().getAuthor().upper() == author.upper():
                listbook += curr.getData().getBookDetails() + "\n"
            curr = curr.getNext()
        return listbook                

    def getAllBooksInCollection(self):
        curr = self.head
        finalList = ""
        while curr !=  None:
            finalList += curr.getData().getBookDetails() + "\n"
            curr = curr.getNext()
        return finalList                
