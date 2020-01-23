from django.contrib import admin

# Register your models here.
from ..personal_data.models import Person

admin.site.register(Person)
