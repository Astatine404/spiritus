# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import MusicForm
from django.shortcuts import render
from .models import Music
from django.http import HttpResponseRedirect
from moviepy.editor import VideoFileClip, AudioFileClip
import moviepy.editor as mpe

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = MusicForm()
		myfile = request.FILES['myfile']
		vvid = Music()
		vvid.video = myfile
		vvid.save()

		videoclip = VideoFileClip("/home/abhay/Desktop/Django/spiritus/Spiritus/media/SampleVideo_1280x720_5mb.mp4")
		background_music = mpe.AudioFileClip("/home/abhay/Desktop/Django/spiritus/Spiritus/media/mozz.mp3")
		new_clip = videoclip.set_audio(background_music)
		new_clip.write_videofile("/home/abhay/Desktop/Django/spiritus/Spiritus/media/final_cut.mp4")

		vidloc = vvid.video
		vid = str(vidloc)

		if myfile:
			return render(request, 'Website/index.html', {'form': form, 'vid': vid})
		else:
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
	else:
		vid = Music.objects.all()

		vid.delete()
		vid = None
		form = MusicForm()
		return render(request, 'Website/index.html', {'form': form, 'vid': vid})