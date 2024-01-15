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
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #Page to add a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #Page to add a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
