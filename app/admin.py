from django.contrib import admin
from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('face_id', 'name', 'address', 'phone', 'email', 'image')
    search_fields = ("face_id",)


admin.site.register(Profile, ProfileAdmin)
