from django.shortcuts import render
from MigrationApp.models import Country,Sector
from MigrationApp.serializers import CountrySerializers,SectorSerializers
from rest_framework import generics

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers
    def get_queryset(self):
        QS = Country.objects.all()
        cname = self.request.GET.get('country_name')
        if cname is not None:
            QS = QS.filter(country_name__icontains=cname)

        return QS


class SectorListView(generics.ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializers
    def get_queryset(self):
        qs = Sector.objects.all()
        secid = self.request.GET.get('sector_id')
        if secid is not None:
            qs = qs.filter(sector_id__icontains=secid)
        return qs