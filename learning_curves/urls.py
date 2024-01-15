"""Define URL patterns to learning_curves."""

from django.urls import path

from . import views

app_name = 'learning_curves'

urlpatterns = [
    #Initial page
    path('', views.index, name='index'),

    #Show all the topics
    path('topics/', views.topics, name='topics'),

    #Detail page for one topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
