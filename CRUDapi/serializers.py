from rest_framework import serializers
from .models import Contacts

class ContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model= Contacts
        fields = ['name','email','phone_no']
    