# Create a class Book with title, author, list of reviews and add methods to: add a new review, count reviews and display all reviews

class Book:

    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.reviews = reviews

    def add_new_review(self, new_review):
        self.reviews.append(new_review)
        return "Review added successfully!"
    
    def count_reviews(self):
        return len(self.reviews)
    
    def display_reviews(self):
        return self.reviews
    
bookOne = Book("Something", "Some Author", ["good", "interesting"])
bookOne.add_new_review("Amazing!")
print(bookOne.display_reviews())
print(bookOne.count_reviews())

