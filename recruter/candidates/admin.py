from django.contrib import admin
from candidates.models import *

class CandidateAdmin(admin.ModelAdmin):
	list_display = ('name', 'date_added',)
	list_filter = ['date_added']
	search_fields = ['name']

#admin.site.register(Candidate)
admin.site.register(Technology)
admin.site.register(Candidate, CandidateAdmin)
