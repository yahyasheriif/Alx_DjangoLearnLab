book.delete()
Book.objects.all()
# Output: <QuerySet []>

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)

book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Output: 'Nineteen Eighty-Four'

book.delete()
Book.objects.all()
# Output: <QuerySet []>
