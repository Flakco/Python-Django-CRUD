from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Members
# Create your views here.

def index(request):
  mymembers = Members.objects.all().values()
  cnames = Members._meta.get_fields()
  template = loader.get_template('index.html')
  context = {
    'mymembers' : mymembers,
    'cnames' : cnames,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['email']
  c = request.POST['adress']
  v = request.POST['phone']
  member = Members(firstname=x, lastname=y, email=z, adress=c, phone=v)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  email = request.POST['email']
  adress = request.POST['adress']
  phone = request.POST['phone']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.email = email
  member.adress = adress
  member.phone = phone
  member.save()
  return HttpResponseRedirect(reverse('index'))