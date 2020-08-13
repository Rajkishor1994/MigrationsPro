from rest_framework import serializers
from MigrationApp.models import Country,Sector

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_id','name']

class SectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'


#username: Migration
#password: raj@1994