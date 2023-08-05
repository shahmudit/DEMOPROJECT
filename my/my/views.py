from django.http import HttpResponse

def hello(request):
    v="Hii"
    return HttpResponse(v) 
    