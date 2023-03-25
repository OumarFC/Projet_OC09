from django.contrib import admin
from review.models import Review
from review.models import Ticket

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Review)
