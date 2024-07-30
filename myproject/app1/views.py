from django.http import HttpResponse

def page1(request):
    return HttpResponse("This is content of page-1.")
