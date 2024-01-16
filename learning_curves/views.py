from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The initial page of Learning Curve."""
    return render(request, 'learning_curves/index.html')

@login_required
def topics(request):
    """Show all the topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_curves/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and its all entries."""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_curves/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_curves:topics'))
        
    context = {'form': form}
    return render(request, 'learning_curves/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry to a specific topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            if topic.owner != request.user:
                raise Http404
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_curves:topic', args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_curves/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_curves:topic', args=[topic.id]))
        
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_curves/edit_entry.html', context)
