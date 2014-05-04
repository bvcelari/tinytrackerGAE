from django.shortcuts import render
from google.appengine.api import users


def home(request):
    myvalue1= "Yes, I am here"
    template_values = {
        'myvalue1': myvalue1,}
    #return render(request, 'mytemplatefolder/home.html', template_values)
    return render(request, 'mytemplatefolder/base.html', template_values)

