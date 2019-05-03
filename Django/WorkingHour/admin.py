from django.contrib import admin

from .models import User, Project, WorkForm, WorkCount, WorkKinds, FormStream
# Register your models here.


admin.site.register(User)
admin.site.register(Project)
admin.site.register(WorkForm)
admin.site.register(WorkCount)
admin.site.register(WorkKinds)
admin.site.register(FormStream)


