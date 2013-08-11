from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *

def home(request):
    return render_to_response('homepage.html')

def overview(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('overview.html', locals(),
                              context_instance=RequestContext(request))

def study(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('study.html', locals(),
                              context_instance=RequestContext(request))

def eat(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('eat.html', locals(),
                              context_instance=RequestContext(request))

def eat(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('eat.html', locals(),
                              context_instance=RequestContext(request))

def play(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('play.html', locals(),
                              context_instance=RequestContext(request))

def do(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('do.html', locals(),
                              context_instance=RequestContext(request))

def tips(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('tips.html', locals(),
                              context_instance=RequestContext(request))

def travel(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('travel.html', locals(),
                              context_instance=RequestContext(request))

def weekend(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('weekend.html', locals(),
                              context_instance=RequestContext(request))

def contribute(request, place_slug):
    place = Place.objects.get(slug=place_slug)
    return render_to_response('contribute.html', locals(),
                              context_instance=RequestContext(request))
