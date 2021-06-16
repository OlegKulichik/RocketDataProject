from django_seed import Seed

seeder = Seed.seeder()
from employees.models import User
seeder.add_entity(User, 5)

inserted_pks = seeder.execute()
