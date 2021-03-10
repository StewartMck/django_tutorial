from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [

    # Without using generic views:
    # /polls/
    # path('', views.index, name='index'),
    # #/polls/1/
    # path('<int:question_id>/', views.detail, name='detail'),
    # #/polls/1/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # #/polls/1/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # With generic views:
    # /polls/
    path('', views.IndexView.as_view(), name='index'),
    #/polls/1/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #/polls/1/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #/polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/delete/', views.QuestionDelete.as_view(), name='delete'),
]