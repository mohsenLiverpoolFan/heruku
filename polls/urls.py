from django.urls import path

from .views import polls_list, poll_detail, pollsListView, pollsDetailView, ChoiceDetailView, ChoiceListView, \
    VoteListView, VoteDetailView, ChoiceListPollView, CreateVote
from .apiviews import PollViewSet, ChoiceViewSet, VoteViewSet, Usercreate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='polls')
router.register('votes', VoteViewSet, basename='votes')
router.register('choices', ChoiceViewSet, basename='choices')
# router.register('usercreate', Usercreate.as_view(), basename='usercreate')

app_name = 'polls'
urlpatterns = [
    # path('polls_d/', polls_list, name='polls_list'),
    # path('polls_d/<int:pk>/', poll_detail, name='poll_detail'),
    # path('polls/', pollsListView.as_view(), name='pollsListView'),
    # path('polls/<int:pk>/', pollsDetailView.as_view(), name='pollsDetailView'),
    # path('votes/', VoteListView.as_view(), name='votesListView'),
    # path('votes/<int:pk>/', VoteDetailView.as_view(), name='votesDetailView'),
    # path('choices/', ChoiceListView.as_view(), name='choicesListView'),
    # path('choices/<int:pk>/', ChoiceDetailView.as_view(), name='choiceDetailView'),
    path("polls/<int:pk>/choices/", ChoiceListPollView.as_view(), name="choice_poll_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="choice_poll_list"),
    path('users/', Usercreate.as_view(), name="user_create")

]
urlpatterns += router.urls
