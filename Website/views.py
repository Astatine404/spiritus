# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import MusicForm
from django.shortcuts import render
from .models import Music
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
	if request.method == 'POST':
		form = MusicForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			vid = Music.objects.all().last()
			print(vid)
			return render(request, 'Website/index.html', {'vid': vid})
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		# vid = Music.objects.all()
		vid = None
		form = MusicForm()
		return render(request, 'Website/index.html', {'form': form, 'vid': vid})