from django.contrib import admin
from tracker.models import Entry, Project, Task
#class EntryAdmin(admin.ModelAdmin):
#	fieldsets = (
#        (None, {
#            'fields':  ('task_description','pub_date','hours',)
#		}),
#	)
admin.site.register(Entry)
admin.site.register(Project)
admin.site.register(Task)

# Register your models here.
