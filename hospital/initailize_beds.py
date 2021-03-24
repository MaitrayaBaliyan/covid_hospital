import sys, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hospital.settings")
import django
django.setup()

from api_app.models import BedAvailability


max_beds = 12

obj_list = []
is_private = False
for i in range(0, max_beds):
	_type = None
	if i % 2 == 0:
		_type = 'General'
	else:
		if is_private:
			_type = 'Private'
			is_private = False
		else:
			_type = 'Semi-Private'
			is_private = True

	obj_list.append(BedAvailability(id=i, type=_type))

BedAvailability.objects.bulk_create(obj_list)