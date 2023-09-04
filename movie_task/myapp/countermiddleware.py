
from typing import Any

from .models import CountModel
class CountMiddleware:
    def __init__(self,response):


        
        self.get_response=response

    
    def __call__(self,request):
        response=self.get_response(request)
        obj=CountModel.objects.get(id=1)
        print(obj,'--',obj.count)
        obj.count+=1
        obj.save()
        return  response
    
   




