
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home_page_old(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def home_page(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))