from rest_framework import serializers
from .models import Vote, Choice, Poll
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ('id')
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class VoteSerializer(serializers.ModelSerializer):
    # choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')

    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, read_only=True, source='vote_set')

    class Meta:
        model = Choice
        fields = '__all__'
        additional_fields = 'votes'


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')

    class Meta:
        model = Poll
        fields = "__all__"
        additional_fields = 'choices'
