
from django.http import HttpResponse
from django.template import loader
from .models import City


def city_home(request):
    template = loader.get_template('city_home.html')
    return HttpResponse(template.render())

def city_list(request):
  mycity = City.objects.all().values()
  template = loader.get_template('city_list.html')
  context = {
    'mycity': mycity,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mycity = City.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mycity': mycity,
  }
  return HttpResponse(template.render(context, request))