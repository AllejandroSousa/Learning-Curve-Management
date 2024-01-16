from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

def logout_view(request):
    """Logout the user."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_curves:index'))
