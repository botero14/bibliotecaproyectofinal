from django.contrib import admin
from apps.libro.models import Libro, AutorLibro

# Register your models here.

class MembershipInline(admin.TabularInline):
    model = AutorLibro
    extra = 1

class LibroAdmin(admin.ModelAdmin):
    inlines = (MembershipInline, )

admin.site.register(Libro, LibroAdmin)