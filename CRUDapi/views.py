from django.shortcuts import render
from rest_framework.views import APIView
from .models import Contacts
from CRUDapi.serializers import ContactsSerializers
from rest_framework.response import Response
from rest_framework import status,generics
from django.contrib import messages



class Search(APIView):

    def get(self,request,*args, **kwargs):
        para = kwargs
        print(para['name'])
        par_lis= para['name'].split('-')
        con = Contacts.objects.filter(name=par_lis[0],email=par_lis[1])
        seri= ContactsSerializers(con,many=True)
        return Response(seri.data)

class Contact(generics.ListCreateAPIView):

    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializers

    def post(self,request):
        ser = ContactsSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response({"Email Already Exists! Try another one"})


class ContactDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts
    serializer_class = ContactsSerializers


class ContactUpdate(APIView):
    def get_object(self,name):
        try:
            return Contacts.objects.get(name=name)
        except Contacts.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,name):
        con= self.get_object(name)
        serialobj = ContactsSerializers(con)
        return Response(serialobj.data)

    def put(self,request,name):
        cono = self.get_object(name)
        conserializ = ContactsSerializers(cono,data=request.data)
        if conserializ.is_valid():
            conserializ.save()
            return Response(conserializ.data,status=status.HTTP_200_OK)
        return Response(conserializ.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,name):
        con = self.get_object(name)
        con.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
