from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from candidates.models import *
from django import forms
from forms import *


def profile_view(request, offset):
    na = offset.split('_')[0]
    sur = offset.split('_')[1]
    i = Candidate.objects.get(name=na, surname=sur)     # get values from 1st table
    tech = [str(item) for item in i.specification.all()]
    context = ({
        'name': na,
        'surname': sur,
        'tech': tech,
        })

    return render(request, 'candidates/profile.html', context)


def search(request):
    html = '<html><body> Here are you candidates <body><html>'
    return HttpResponse(output)


def index(request):
    latest_candidate_list = Candidate.objects.all()[:5]
    context = ({'latest_candidate_list': latest_candidate_list})
    return render(request, 'candidates/index.html', context)


def edit_profile(request, offset):
    if request.method == 'POST':
        form = ProfileForm(request.Post)
        if form.is_valid():
            return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    context = ({'form': form})

    return render(request, 'candidates/profile_edit.html', context )


    return HttpResponse(html)
