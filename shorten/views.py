import random
import string

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView

from .forms import UrlForm
from .models import UrlList


# Create your views here.

class ShortenerView(FormView):
    form_class = UrlForm
    template_name = 'shorten/shorten.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        url = request.POST['url']

        def id_generator(size=5, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
            return ''.join(random.choice(chars) for _ in range(size))

        short = None
        if UrlList.objects.filter(url=url).exists():
            short = UrlList.objects.get(url=url).short
        else:
            url = UrlList.objects.create(url=url)
            url.short = id_generator()
            short = url.short
            url.save()
        return render(request, self.template_name, {'form': form, 'short': short})


class RedirectView(RedirectView):
    def get(self, request, short, *args, **kwargs):
        if UrlList.objects.filter(short=short).exists():
            url = UrlList.objects.get(short=short).url
            return HttpResponseRedirect(url)
        return HttpResponse('REDIRECT URL NOT FOUND')
