from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

def index(request):
    """The initial page of Learning Curve."""
    return render(request, 'learning_curves/index.html')

def topics(request):
    """Show all the topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_curves/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and its all entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_curves/topic.html', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_curves:topics'))
        
    context = {'form': form}
    return render(request, 'learning_curves/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry to a specific topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_curves:topic', args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_curves/new_entry.html', context)
