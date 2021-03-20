from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import contents
from django.template import loader

def index(request):
	return HttpResponse("Hello, world.This is Alikhan.")

@csrf_exempt
def content(request):
	print(request.method)
	if request.method == "GET":
		latest_contents_list = contents.object.all()
		output = ', '.join([f'{c.first_name}{c.last_name}'for c in latest_contents_list])
		return HttpResponse(output)

	if request.method == "POST":
		data = request.POST
		data = dict(data)
		content = contents.objects.create(first_name=data.get('first_name'),last_name=data.get('last_name'),
			number=data.get('number'))
		return HttpResponse("Data Posted")

def penchod_kutta(request):
	template = loader.get_template('contents/kutta.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

def hmmm(request):
	template = loader.get_template('contents/kutti.html')
	context = {

	}
	return HttpResponse(template.render(context, request))
