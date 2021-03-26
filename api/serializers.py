from rest_framework import serializers
from .models import CompanyModel
from rest_framework.serializers import ValidationError


class Companyserializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = "__all__"
 
 
     
    
    

     