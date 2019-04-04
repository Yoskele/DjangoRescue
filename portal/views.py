from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import PersonStatus

from .models import Person, Event, PersonStatus

from django.contrib import messages





def index(request):
    return render(request, 'portal/index.html')


def add_person(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        other_name = request.POST.get('other_name')
        status = request.POST.get('status')
        id_number = (request.POST.get('id_number'))
        mobile = (request.POST.get('mobile'))
        email = request.POST.get('email')
        description = request.POST.get('description')

        data = Person(first_name=first_name, last_name=last_name, 
        other_name=other_name, status=status, 
        id_number=id_number, mobile=mobile, 
        email=email, description=description)

        data.save()
        messages.add_message(request, messages.SUCCESS, "You have registered successfully")
        return render (request, 'portal/add_person.html')
    return render(request, 'portal/add_person.html')


def show_person(request, person_id):
    person = Person.objects.get(id=person_id)
    context = {
        'person':person
    }
    # ... 
    return render(request, 'portal/show_person.html', context)


def show_safe_persons(request):
    # Need to fetch all the people who has Safe in Status
    persons = Person.objects.filter(status='safe')
    context = {
        'persons':persons
    }
    return render(request, 'portal/show_persons.html', context)


def search_person(request):
    context = None
    if request.method != 'POST':
        return redirect('portal:index')

    text = request.POST.get('search', '')
    # results = Person.objects.filter(
    #     Q(first_name__icontains=text) |
    #     Q(last_name__icontains=text) |
    #     Q(other_name__icontains=text) |
    #     Q(description__icontains=text))

    # to do: render a page with the results.
