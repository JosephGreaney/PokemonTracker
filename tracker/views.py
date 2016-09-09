from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	context = {'img_nums' : range(1, 722)}
	return render(request, './index.html', context)
