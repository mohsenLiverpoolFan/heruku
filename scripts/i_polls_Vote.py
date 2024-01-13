from polls.models import Choice, Poll, Vote
from django.contrib.auth.models import User
import random


def run():
    # users_id = User.objects.all().values_list('id', flat=True)
    poll_id = Poll.objects.all().values_list('id', flat=True)
    user_id = User.objects.filter(is_superuser=False).values_list('id', flat=True)
    choice_id = Choice.objects.all().values_list('id', flat=True)

    data = []
    for i in range(1, 40):
        data.append({
            'choice': Choice.objects.get(id=random.choice(choice_id)),
            'poll': Poll.objects.get(id=random.choice(poll_id)),
            'voted_by': User.objects.get(id=random.choice(user_id)),

        })
    Vote.objects.bulk_create([
        Vote(**d) for d in data
    ])
