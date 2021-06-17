import os
import sys

import django

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'RocketDataProject.settings'
django.setup()

from django_seed import Seed
from employees.models import Employee, User

seeder = Seed.seeder()
seeder.add_entity(User, 5, {
    'middle_name': lambda x: seeder.faker.name(),
    'first_name': lambda x: seeder.faker.first_name(),
    'last_name': lambda x: seeder.faker.name(),
})
seeder.add_entity(Employee, 5, {
    'head': None,
})
inserted_pks = seeder.execute()