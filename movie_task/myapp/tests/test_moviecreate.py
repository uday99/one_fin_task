from rest_framework.test import APIClient
from django.test import TestCase, TransactionTestCase
from django.test.utils import override_settings
from django.conf import settings

from requests import request
from rest_framework.test import APIClient
from myapp.models import Register,CollectionModel
import json

from django.urls import reverse



class Movies_Test(TransactionTestCase):

    @override_settings(ROOT_URLCONF='movie_task.urls')
    def test_register_user_view(self,request=request):
        client= APIClient()

        headers={
            'content_type':'application/json'
        }


        data={"username":"gandhi","email":"gandhi@gmail.com","password":"IM.gandhi@@"}
        

        
        data=json.dumps(data)
        url=reverse('reg_user')
        response=client.post(url,data,**headers)
        print(response.content)
        self.assertEqual(response.status_code,201)
    

    @override_settings(ROOT_URLCONF='movie_task.urls')
    def test_createcollection_view(self,request=request):
        
        client= APIClient()
        url=reverse('reg_user')
        response=client.post(url,{"username":"gandhi","email":"gandhi@gmail.com","password":"IM.gandhi@@"},format="json")
        print(response.content)
        token = response.data['token']

        client= APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' +token)

        rg=Register(username='gandhi',email="gandhi@gmail.com",password="IM.gandhi@@")

        headers={
            "Authorization":"JWT "+token,
            'content_type':'application/json'
        }

        data={
    
                "title":"prabhas collection",
                "description":"We provide  collection of movies for prabhas",
                "movies":[
                    {
                        "title":"Bahuballii",
                        "description":"got describes the war and the power of a king",
                        "genres":"bhaubali"
                        
                    },
                    {
                        "title":"sahoo",
                        "description":"the revenge of father by son",
                        "genres":"gangstar and busineess man"
                        
                    },
                    {
                        "title":"radhyashyyam",
                        "description":"the love story of engergitic person",
                        "genres":"palmist"
                        
                    }
                    

                ]
            }
        data=json.dumps(data)
        url=reverse('coll_movie')
        response=client.post(url,data,**headers)
        print(response.content)
        self.assertEqual(response.status_code,201)
    







        
        
        
