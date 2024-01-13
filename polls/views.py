from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import PollSerializer, VoteSerializer, ChoiceSerializer
from .models import Poll, Choice, Vote
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListCreateAPIView, ListAPIView
from rest_framework import status


@api_view(["GET"])
def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = PollSerializer(polls, many=True).data
    # data = {'results': list(polls.values('question', 'created_by__username'))}

    return Response(data)


class pollsListView(ListCreateAPIView):
    # def get(self, request, format=None):
    #     polls = Poll.objects.all()[:20]
    #     data = PollSerializer(polls, many=True).data
    #     return Response(data)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class pollsDetailView(RetrieveAPIView):
    # def get(self, request, pk, format=None):
    #     poll = get_object_or_404(Poll, pk=pk)
    #     data = PollSerializer(poll).data
    #     return Response(data)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


@api_view(["GET"])
def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {'results': {'question': poll.question,
                        'created_by': poll.created_by.username,
                        'pub_date': poll.pub_date}}
    data = PollSerializer(poll).data
    return Response(data)


class ChoiceListView(ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetailView(RetrieveAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class VoteListView(ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class VoteDetailView(RetrieveAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class ChoiceListPollView(ListAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset

    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get("voted_by")
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
