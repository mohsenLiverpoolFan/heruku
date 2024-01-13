from bookreview.models import Author, Book
import names
import random


def run():
    data = []
    for i in range(1, 20):
        data.append({
            'first_name': names.get_first_name(),
            'last_name': names.get_last_name()
        })
    Author.objects.bulk_create([
        Author(**d) for d in data
    ])
    authors_id = Author.objects.all().values('id')
    data = []

    for i in range(1, 30):
        data.append({
            'title': names.get_first_name(),
            'isbn': str(random.randint(10000, 99999)),
            'author': Author.objects.get(id=random.choice(authors_id)['id'])
        })
    Book.objects.bulk_create(
        [Book(**d) for d in data]
    )
