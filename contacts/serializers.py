from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=True)
    class Meta:
        model = Contact
        fields ='__all__'

def validate_name(self, value):
    if value.strip() == "":
        raise serializers.ValidationError("Имя не должно быть пустым!")
    return value

def validate_phone(self, value):
    if len(value) < 9:
        raise serializers.ValidationError('Номер не должен быть пустым!')
    return value