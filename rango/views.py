from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello")

def about(request):
	return HttpResponse("hello rashmi")