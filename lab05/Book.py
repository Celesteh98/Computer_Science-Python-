#Celeste Herrera
#Book.py
class Book:
    def __init__(self,title = "",author = "",year = None):
        self.title= title
        self.author = author
        self.year = year

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookDetails(self):
        details = "Title: {}, Author: {}, Year: {}".format(self.title,self.author,self.year)
        return details
    
    def __gt__(self,a):
        if self.author == a.author:
            if self.year == a.year:
                if self.title > a.title:
                    return True
                elif self.title < a.title:
                    return False
       
            else:
                if self.year > a.year:
                    return True
                elif self.year < a.year:
                    return False

        else:
            if self.author > a.author:
                return True
            elif self.author < a.author:
                return False
