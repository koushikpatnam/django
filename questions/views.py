
from django.http import HttpResponse


def login_view(request):
    return HttpResponse("<h1> Hello This is my new website</h1>")
   # messages.info(request, 'Account not found')
