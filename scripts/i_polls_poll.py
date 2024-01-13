from polls.models import Poll
from django.contrib.auth.models import User
import random
import datetime
import lorem
from faker import Faker


def run():
    users_id = User.objects.all().values_list('id', flat=True)
    data = []
    for i in range(1, 30):
        fake = Faker()
        data.append({
            'created_by': User.objects.get(pk=random.choice(users_id)),
            'question': lorem.sentence(),
            'pub_date': fake.date_time_between(start_date='-3y', end_date='now')
        })
    Poll.objects.bulk_create([
        Poll(**d) for d in data
    ])
