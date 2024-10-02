from django.contrib import admin

from .models import Portfolio
from .models import Hobbies
from .models import Contact
# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Hobbies)
admin.site.register(Contact)