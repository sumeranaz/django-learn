from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Contact
# Create your views here.

def index(request):
	return HttpResponse("This is index one")


def index1(request):
	return HttpResponse("This is Ali Khan")

def index2(request):
	return HttpResponse("Hello, world. This is sami")

@csrf_exempt
def contact(request):
	print(request.method)
	if request.method == "GET":
		latest_contact_list = Contact.objects.all()
		output = ', '.join([f'{c.first_name} {c.last_name}' for c in latest_contact_list])
		return HttpResponse(output)
	if request.method == "POST":
		data = request.POST
		data = dict(data)
		contact = Contact.objects.create(first_name=data.get('first_name'), last_name=data.get('last_name'),
			number=data.get('number'))
		return HttpResponse("Data Posted")

# def index(request):
# 	def content(request):
# 		print(request.method)
# 		if request.method =="GET"
# 		latest_contents_list = contents.object.all()
# 		output= ', '.join(['f'{c.first_name}{c.last_name}for c in latest_contents_list])
# 		return HttpResponse(output)
    
#     def mobile(request):
#     	print (request.method)
#     	if request.method == "GET"
#     	latest_mobile_list = mobile.objects.all()
#     	output = ', '.join(['f'{m.first_name}{m.last_name} for m in latest_mobile_list])
#     	return HttpResponse(output)


#     if request.method =="POST"
#     data = request.POST
#     data = dict(data)
#     contents = contents.object.create(first_name=data.get('first_name'),last_name=data.get('last_name'),number=data.get('number'))
#     return HttpResponse(data)



# Task 1
# Create a view in which at get request you show data from contact table 
# but in the response you send html template
from django.template import loader

def say_hello(request):
    template = loader.get_template('contact/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

   