from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import UPR_submission, UPR_question

class UPRSubAdmin(admin.ModelAdmin):
    pass
admin.site.register(UPR_submission, UPRSubAdmin)

admin.site.register(UPR_question)