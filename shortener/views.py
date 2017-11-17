from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.views import View
from .forms import SubmitUrlForm
from analytics.models import ClickEvent
# Create your views here.

from .models import LnktoURL

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "lnkto.co",
            "form": the_form,
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "lnkto.co",
            "form": form,
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            # 2017-11-16
            # at this point, if the url entered in the form does not contain 'http://' 
            # but the database already contains a the contatination of 'http://' + url
            # it will create a new url shortcode for the identical url.
            # the save function in models is where the http is added. 
            print(new_url)
            # 2017-11-16
            # we must check for and add the http if it is missing BEFORE running 
            # the get_or_create function to prevent duplicate urls from being entered            
            if not new_url.startswith("http"):
                new_url = "http://" + new_url
            # new url now contains http://
            print(new_url)
            obj, created = LnktoURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"
        
        return render(request, template, context)


class UrlRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = LnktoURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
