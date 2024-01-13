from django.contrib.auth.models import User
import names
import random


def run():
    data = []
    for i in range(1, 25):
        data.append({
            'username': names.get_full_name(),
            'password': '{0}_{1}'.format(names.get_first_name(), 123),
            'first_name': names.get_first_name(),
            'last_name': names.get_last_name(),
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        })
    User.objects.bulk_create([
        User(**d) for d in data
    ])
