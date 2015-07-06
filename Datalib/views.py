from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from Datalib.models import Person
from django.http import HttpResponseRedirect

def insert(request):
    # If this is a post request we insert the person
    if request.method == 'POST':
        p = Person(
            name=request.POST['name'],
            phone=request.POST['phone'],
            age=request.POST['age']
        )
        p.save()
    t = loader.get_template('insert.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))

def index(request):
    people = Person.objects.all()
    t = loader.get_template('index.html')
    c = Context({'people': people})
    return HttpResponse(t.render(c))

def delete(request, person_id):
    p = Person.objects.get(pk=person_id)
    p.delete()
    return HttpResponseRedirect('/')

def edit(request, person_id):
    p = Person.objects.get(pk=person_id)
    if request.method == 'POST':
        p.name = request.POST['name']
        p.phone = request.POST['phone']
        p.age = request.POST['age']
        p.save()
    t = loader.get_template('insert.html')
    c = RequestContext(request, {
        'person': p
    })
    return HttpResponse(t.render(c))