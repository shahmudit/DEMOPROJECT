from django.http import HttpResponse

def hello(request):
    v="Hello"
    return HttpResponse(v) 
    