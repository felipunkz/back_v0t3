from django.contrib import admin
from apiv0t3.models import (Candidate, Elector, Vote)

admin.site.register(Candidate)
admin.site.register(Elector)
admin.site.register(Vote)