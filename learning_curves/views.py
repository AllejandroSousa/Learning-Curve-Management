from django.shortcuts import render

from .models import Topic

def index(request):
    """The initial page of Learning Curve."""
    return render(request, 'learning_curves/index.html')

def topics(request):
    """Show all the topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_curves/topics.html', context)
