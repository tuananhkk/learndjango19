from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request):
    if request.user.is_authenticated():
        context = {
            "title":"Details"
        }
    else:
        context = {
            "title":"User unauthenticated"
        }
    return render(request, 'list.html',context)
    