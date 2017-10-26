from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import SubmitUrlForm
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
        if form.is_valid():
            print(form.cleaned_data.get("url"))
        context = {
            "title": "lnkto.co",
            "form": form,
        }
        return render(request, "shortener/home.html", context)


class LnktoCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(LnktoURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)




'''
def lnkto_redirect_view(request, shortcode=None, *args, **kwargs):
    # print(args)
    # print(kwargs)
    # print(shortcode)
    
    obj = get_object_or_404(LnktoURL, shortcode=shortcode)
    

    # try:
    #     obj = LnktoURL.objects.get(shortcode=shortcode)
    # except: 
    #     obj = LnktoURL.objects.all().first()
     
    #  obj_url = None
    # qs = LnktoURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url


    return HttpResponse("hello {sc}".format(sc=obj.url))

'''