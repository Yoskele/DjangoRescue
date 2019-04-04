from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from .models import PersonStatus

from .models import Person





def index(request):
	return render(request, 'portal/index.html')


def add_person(request):
    # if request.method == 'POST':
        # ...
        # return redirect('portal:index')
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        other_name = request.form.get('other_name')
        status = request.form.get('status')
        id_number = request.form.get('id_number')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        description = request.form.get('description')

        person = Person(first_name, last_name, other_name, status,
                            id_number, mobile, email, description
                        )
        person.save()
    return render(request, 'portal/add_person.html')


def show_person(request, person_id):
    # ... 
    pass


def show_safe_persons(request):
    persons = None # ... change this line!
    return render(request, 'portal/show_persons.html', {
        'title': 'Persons marked as Safe',
        'main_heading': 'Persons Marked as Safe',
        'persons': persons })


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
