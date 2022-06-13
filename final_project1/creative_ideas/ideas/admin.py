from .models import Business_idaea ,Comment ,Offers
from django.contrib import admin




class BusinessAdmin(admin.ModelAdmin):
    list_display = ('ideas', 'cost' ,'idea_owner')

class commetAdmin(admin.ModelAdmin):
    list_display = ( 'comments' ,'investor',"ideas" )

class offersAdmin(admin.ModelAdmin):
    list_display = ("offers_state","ideas","investor")






admin.site.register(Business_idaea,BusinessAdmin )
admin.site.register(Comment,commetAdmin)
admin.site.register(Offers,offersAdmin)