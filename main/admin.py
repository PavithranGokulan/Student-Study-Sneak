from django.contrib import admin
from .models import Notes,Task,NoteApp,Remainder

# Register your models here.

admin.site.register(Notes) 
admin.site.register(NoteApp)
admin.site.register(Task)
admin.site.register(Remainder)