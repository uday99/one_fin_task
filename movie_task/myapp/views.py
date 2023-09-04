from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer,CollectionSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from .models import Register,CollectionModel,CountModel
jwt_payload_handler=api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
import json
from django.db.models import Count
from django.contrib.auth.hashers import make_password
from django.contrib.postgres.fields.jsonb import KeyTextTransform
from django.db.models import Q
import http
class Register_user(APIView):
    print("enternnn")

    def post(self,request):
        data=request.data
        print(data)

        try:
            rs=RegisterSerializer(data=data)
            if rs.is_valid():
                password=make_password(data['password'])

                rs.save(password=password)
                usr=Register.objects.get(id=rs.data['id'])
                #print(data)
                payload=jwt_payload_handler(usr)
                token=jwt_encode_handler(payload)
                content={'message':"User Register successfully",'token':token}            
                return Response(content,status=status.HTTP_201_CREATED)
            else:
                return Response(rs.errors)

            
        except Exception as e:
            
            return Response(str(e))
        



class Create_collection_movie(APIView):
    authentication_classes=[JSONWebTokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        try:
            usrid=request.user.pk

            cdata=CollectionModel.objects.filter(user_id=usrid)
            cs=CollectionSerializer(cdata,many=True)
            return Response(cs.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))
    
    
    
    def post(self,request):
        data=request.data
        usrid=request.user.pk
        print(usrid,'USeriiid')
        try:
            rg=Register.objects.get(id=usrid)
            data['user']=rg
            cs=CollectionSerializer.create(self,data)                        
            cs.save()
            print(cs.uuid)
            
            data={'collection_uuid':cs.uuid}
            return Response(data,status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(str(e))
        
        
class List_collections(APIView):
    authentication_classes=[JSONWebTokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,collection_uuid):
        try:
            print(collection_uuid)
            cdata=CollectionModel.objects.get(uuid=collection_uuid)
            cs=CollectionSerializer(cdata)
            return Response(cs.data)
        except Exception as e:
            return Response(e)
        
    
    def put(self,request,collection_uuid):
        print('putt method')
        data=request.data
        
        try:
            
            cdata=CollectionModel.objects.get(uuid=collection_uuid)
            cs=CollectionSerializer(cdata,data=data)
            if cs.is_valid():
                cs.save()
                return Response(cs.data)
            else:
                return Response(cs.errors)
        except Exception as e:
            return Response(str(e))
    

    def delete(self,request,collection_uuid):
        try:
            CollectionModel.objects.get(uuid=collection_uuid).delete()
            return Response({"message":"collection Delete successfully"})
        except Exception as e:
            return Response(str(e))

import requests
from requests.auth import HTTPBasicAuth
import environ

env = environ.Env()
environ.Env.read_env()

class Movies_list(APIView):

   
    def get(self,request):
        
              
        r=requests.get('https://demo.credy.in/api/v1/maya/movies/',auth = HTTPBasicAuth('iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0',env("PASSWORD")))
        data=r.content
        dict_data=json.loads(data)
        print(dict_data)
        if  ('results' in dict_data)  and dict_data['results']:
            return Response(dict_data)
                
        else:
            print('error')

            msg={'message':"Retry the Server "}
            return Response(msg)
            
        



class Count_value_request(APIView):

    def get(self,request):

        cm=CountModel.objects.get(id=1)
        count_value=cm.count
        
        msg={'request':"No of request serverd till now is:"+str(count_value)}
        return Response(msg,status=status.HTTP_200_OK)



class Count_request_reset(APIView):
    def post(self,request):
        cm=CountModel.objects.get(id=1)
        cm.count=0
        cm.save()
        msg={'message':"Request count reset successfull"}
        return Response(msg,status=status.HTTP_200_OK)