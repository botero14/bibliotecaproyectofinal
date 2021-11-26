from django.contrib import admin
from apps.ejemplar.models import Ejemplar, Prestamo

# Register your models here.

class MembershipInline(admin.TabularInline):
    model = Prestamo
    extra = 1
    
class EjemplarAdmin(admin.ModelAdmin):
    inlines = (MembershipInline, )

admin.site.register(Ejemplar, EjemplarAdmin)