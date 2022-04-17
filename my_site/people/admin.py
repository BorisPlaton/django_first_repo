from django.contrib import admin

# Register your models here.
from .models import Person, Country


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'age', 'country')
    list_display_links = ('id', 'country')
    list_filter = ('first_name', 'second_name', 'country')
    search_fields = ('country__name',)


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', 'id')


admin.site.register(Person, PersonAdmin)
admin.site.register(Country, CountryAdmin)
