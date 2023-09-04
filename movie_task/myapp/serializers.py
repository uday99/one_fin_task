from .models import Register,CollectionModel
from rest_framework import serializers





class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    

    class Meta:
        model=Register
        fields='__all__'




class MovieSerializer(serializers.Serializer):

    title=serializers.CharField(max_length=80 )
    description=serializers.CharField(max_length=100)
    genres=serializers.CharField(max_length=120)
    uuid=serializers.UUIDField()





class CollectionSerializer(serializers.ModelSerializer):  
    user=RegisterSerializer(many=False,read_only=True) 
    class Meta:
        model=CollectionModel
        fields="__all__"

    def create(self, validated_data):        
        collection = CollectionModel.objects.create(**validated_data)
        return collection
    
    # def update(self,instance,validate_data):
    #     pass


    


# movies=serializers.ListField(child=MovieSerializer())
#     user=RegisterSerializer(many=False)