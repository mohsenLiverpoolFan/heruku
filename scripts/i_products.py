from products.models import Product


# import


def run():
    data = []
    data.append({
        'title': 'hello wolrd 2 ',
        'content': 'there is amazing too',
        'price': 12.02
    })
    Product.objects.bulk_create([Product(**d) for d in data])
