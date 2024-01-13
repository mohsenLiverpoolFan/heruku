from django.contrib import admin
from .models import Vote, Poll, Choice


# Register your models here.

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
