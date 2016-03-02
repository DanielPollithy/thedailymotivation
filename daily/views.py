from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Quote
from .forms import UploadFileForm

import datetime


def index(request):
    today = datetime.date.today()
    datestring = today.strftime('%d. %b %Y')
    quote = None
    try:
        quote = Quote.objects.get(date=today)
        quote_exists = True
    except:
        quote_exists = False
    template = loader.get_template('daily/index.html')
    form = UploadFileForm()
    context = {
        'quote': quote,
        'quote_exists':quote_exists,
        'form': form,
	'date': datestring
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    if request.method == 'POST' and not Quote.imageForToday():
        print request.FILES
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            quote = Quote(image=request.FILES['uploadImage'], text=request.POST['text'])
            quote.save()
    return HttpResponseRedirect('.')
