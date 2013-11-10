import os
import random
import re
import string
from urlparse import urljoin
from django.core.mail.message import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import simplejson
from django.template import RequestContext, loader, Context
from django.contrib import auth
from django.core.context_processors import csrf
import datetime
import settings

def home(request):
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))
def index_ben(request):
	return render_to_response('index_ben.html', locals(), context_instance=RequestContext(request))
def index_abby(request):
    return render_to_response('index_abby.html', locals(), context_instance=RequestContext(request))
def index_justin(request):
    return render_to_response('index_justin.html', locals(), context_instance=RequestContext(request))