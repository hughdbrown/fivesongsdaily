from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from fivesongsdaily.message.models import Message

@login_required
def show_all(request):
    template_name = 'messages.html'
    messages = Message.objects.filter(active=True).order_by('-created_at')[:5]
    return render_to_response(template_name, {'messages':messages}, context_instance=RequestContext(request))

