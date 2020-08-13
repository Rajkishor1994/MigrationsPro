from django.contrib import admin
from MigrationApp.models import Country,Sector

class CountryAdmin(admin.ModelAdmin):
    class Meta:
        model = Country
        list_display = ['id','country_id','country_name','name']

admin.site.register(Country,CountryAdmin)

class SectorAdmin(admin.ModelAdmin):
    class Meta:
        model = Sector
        list_display = ['id','sector_id','name']

admin.site.register(Sector,SectorAdmin)