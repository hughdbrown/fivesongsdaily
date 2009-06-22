#import logging
#import datetime
#from time import strftime

#from django.conf import settings
#from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
#from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
#from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.template.loader import render_to_string

from fivesongsdaily.message.models import Message

@login_required
def show_all(request):
    print "show_all"
    template_name = 'messages.html'

    try:
        messages = Message.objects.filter(active=True).order_by('-created_at')[:5]
    except ObjectDoesNotExist:
        messages = None

    return render_to_response(template_name, {'messages':messages}, context_instance=RequestContext(request))

