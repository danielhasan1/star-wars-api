from rest_framework import serializers

from star_wars_data.models import StarWarsPlanets

class StarWarsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarWarsPlanets
        fields = [
            'pk',
            'title',
            'my_title',
            'favourite',
            'timestamp'
        ]

#converts to json and validates 
    # def validate(self,data):
    #     qs = StarWarsPlanets.objects.filter(my_title__iexact=data.get('my_title'),title___iexact=data.get('title'),favriote__exact=data.get('favriote'))
    #     if qs.exists():
    #         return serializers.ValidationError("already exist")
    #     return value

# class StarWarsSerializer(serializers.Serializer):
#     def update(self,instance,validated_data):
#         instance.my_title = validated_data.get('my_title')
#         instance.favriote = validated_data.get('favriote')
#         instance.save()
#         return instance

# from rest_framework import serializers

class RemoteMovieDataSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
   title = serializers.CharField(max_length=240)
   created = serializers.DateTimeField()

class RemotePlanetDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=240)
    created = serializers.DateTimeField()