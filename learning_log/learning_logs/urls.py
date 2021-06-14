from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path(r'topics/(?p<topic_id>\d+)/$', views.topic, name='topic'),
]