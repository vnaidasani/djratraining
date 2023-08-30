from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Member, Category, Product
from django.template import loader
from django.urls import reverse

# Create your views here.
def hq(request):
    members = Member.objects.all().values()
    categories = Category.objects.all().values()
    # members = Member.objects.filter(isActive="Y")
    template = loader.get_template('home.html')
    context ={
        'members':members,
        'categories':categories
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    fn = request.POST['first']
    ln = request.POST['last']
    member = Member(first_name=fn, last_name=ln)
    member.save()
    return HttpResponseRedirect(reverse('HQ'))

def update(request,id):
    member = Member.objects.get(id=id)
    template = loader.get_template('update.html')
    context ={
        'member':member
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    fn = request.POST['first']
    ln = request.POST['last']
    member = Member.objects.get(id=id)
    member.first_name = fn
    member.last_name = ln
    member.save()
    return HttpResponseRedirect(reverse('HQ'))

def delete(request,id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('HQ'))

def addcategory(request):
    template = loader.get_template('add_category.html')
    return HttpResponse(template.render({},request))

def addcatname(request):
    catname = request.POST['catname']
    category = Category(name=catname)
    category.save()
    return HttpResponseRedirect(reverse('HQ'))

def addproduct(request):
    template = loader.get_template('add_product.html')
    return HttpResponse(template.render({},request))

def addprodname(request):
    prodname = request.POST['prodname']
    product = Product(name=prodname)
    product.save()
    return HttpResponseRedirect(reverse('HQ'))