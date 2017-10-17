from rest_framework import serializers
from task.models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
class CitySerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    
    def get_country(self,obj):
        return '<a href="/details/?type=country&val=' + obj.countrycode.name + '">'+ obj.countrycode.name + '</a>'

    class Meta:
        model = City
        fields = ('name', 'district', 'population', 'country')

class LanguageSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    
    def get_country(self,obj):
        return '<a href="/details/?type=country&val=' + obj.countrycode.name + '">'+ obj.countrycode.name + '</a>'

    class Meta:
        model = Countrylanguage
        exclude = ('countrycode', )   