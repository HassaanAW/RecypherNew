from django.contrib import admin
from home.models import Registerations, Team, Item, User_Emails, Scores
from embed_video.admin import AdminVideoMixin

# Register your models here.
admin.site.register(Registerations)
admin.site.register(Team)
admin.site.register(User_Emails)
admin.site.register(Scores)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass
admin.site.register(Item, MyModelAdmin)

