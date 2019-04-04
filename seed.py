#!/usr/bin/env python3

import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dr.settings')

import django
django.setup()

from faker import Faker

from portal.models import Event, PersonStatus, Person


Event.objects.all().delete()
PersonStatus.objects.all().delete()

fire_event = Event(name='fire_sale')
fire_event.save()

missing_status = PersonStatus(name='missing')
missing_status.save()

safe_status = PersonStatus(name='safe')
safe_status.save()

# to do: create 30 Person objects using Faker



# Sending 30 fake accounts to Class Person and there it will push it to the data base.
def people():
    faker = Faker()
    for x in range(30):
        person = Person()
        person.first_name = faker.first_name()
        person.last_name = faker.last_name()
        person.other_name = faker.name()
        person.id_number = faker.random_int(min=10000, max=99999)
        person.email = faker.email()
        person.description = faker.text(max_nb_chars=200)
        person.save()
#people()

