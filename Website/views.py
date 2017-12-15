# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import MusicForm
from django.shortcuts import render
from .models import Music
from django.http import HttpResponseRedirect
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.editor as mpe
import os

# Create your views here.

def index(request):
	form = MusicForm()

	if request.method == 'POST':
		
		old_root = os.path.abspath(os.path.dirname(__file__))
		new_root = old_root.replace("/Website", "")

		root = new_root + "/Spiritus"
		myfile = request.FILES['myfile']
		
		vvid = Music()
		vvid.video = myfile
		vvid.save()
 
		vids = root + "/media/" + str(vvid.video)
		auds = root + "/media/mozz.mp3"
		resu = "/media/final_" + str(vvid.video)
		resl = root + resu

		ovid = Music()
		ovid.video = resu
		ovid.save()

		videoclip = VideoFileClip(vids)
		background_music = mpe.AudioFileClip(auds)

		if videoclip.duration < background_music.duration:
			clipped_back = background_music.set_end(videoclip.duration)
		else:
			clipped_back = background_music

		vvid.delete()

		new_clip = videoclip.set_audio(clipped_back)
		new_clip.write_videofile(resl)

		if myfile:
			return render(request, 'Website/index.html', {'form': form, 'vid': myfile, 'resu': resu})
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		vid = Music.objects.all()
		print vid
		vid.delete()
		vid = None
		
		return render(request, 'Website/index.html', {'form': form, 'vid': vid})