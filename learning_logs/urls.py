"""Defines URL patterns for learning_logs."""

from django.urls import path  #path is needed when mapping urls to views 

from . import views

app_name = 'learning_logs' # helps django differentiate this urls file from other url files for other apps 
urlpatterns = [
    # Home page

    # the path function takes three arguments 
    # 1st is a string that helps django the current request properly 
    # 2nd is the view function that's supposed to be refernced/ called in views.py
    # 3rd is the name of that we can refference in other files throughout the project
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for adding a new Topic 
    path('new_topic/', views.new_topic, name ='new_topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]