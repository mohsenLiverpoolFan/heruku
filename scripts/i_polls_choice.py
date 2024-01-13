from polls.models import Choice, Poll

from faker import Faker
import random


def run():
    # users_id = User.objects.all().values_list('id', flat=True)
    poll_id = Poll.objects.all().values_list('id', flat=True)
    data = []
    for i in range(1, 40):
        fake = Faker()
        data.append({
            'choice_text': fake.sentence(),
            'poll': Poll.objects.get(id=random.choice(poll_id))
        })
    Choice.objects.bulk_create([
        Choice(**d) for d in data
    ])
