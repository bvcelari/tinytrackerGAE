from django.shortcuts import render
from google.appengine.api import users

## needed by ajax
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import simplejson
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
import json
## end needed by ajax
import logging

def home(request):
    myvalue1= "Yes, I am here"
    template_values = {
        'myvalue1': myvalue1,}
    #return render(request, 'mytemplatefolder/home.html', template_values)
    return render(request, 'mytemplatefolder/hours.html', template_values)


def userhours(request):
    if request.POST:
    	logging.debug(request.POST)
    	#my_response = request.POST['date_val']
    	my_response = "AA"
    	#data = json.loads(request.body)
    	#result = json.dumps({'messagesent' : "Anything I wan" + "This is how we do it"})
    	#return HttpResponse(result, mimetype='application/javascript')
    else:
	my_response = "BB"
   
    return HttpResponse(simplejson.dumps(my_response),mimetype='application/json')

