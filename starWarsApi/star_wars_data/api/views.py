import requests
from star_wars_data.models import StarWarsPlanets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializer import StarWarsDataSerializer,RemoteMovieDataSerializer,RemotePlanetDataSerializer
URL = "https://swapi.dev/api/"

class SavedTitle(generics.RetrieveUpdateDestroyAPIView):
    """
    Do update on basis of primary key
    """
    lookup_field = "pk"
    serializer_class = StarWarsDataSerializer
    queryset = StarWarsPlanets.objects.all()


class PlanetList(APIView):
    """
    Load all Planets or search a planet by concatenating ?q=planet_name in url.
    """
    serializer_class = StarWarsDataSerializer #for post

    def get(self, request, format=None):
        query = '/'
        list_names = []
        if request.GET.get('q'):
            query = "/?search=" + request.GET.get('q')
        uri = URL+'planets'
        while uri:
            res = requests.get(uri+query,verify=False)
            if res.status_code == 200:
                data = res.json()
                uri = data.get('next',False)
                query = '' # in case if searched query is also giving paginated results then we can simply change the query
                list_names += [{'name':i.get('name'),'created':i.get('created')} for i in data.get('results')]
            else:
                # log the error in case if status code is not 200 and return empty result
                print(res.status_code,res.json())
                uri = False
        return Response({'count':len(list_names),'planet_names':list_names})


class MovieList(APIView):
    """
    Load all movie titles.
    """
    serializer_class = RemoteMovieDataSerializer
    def get(self,request,format=None):
        uri = URL+'films'
        list_names = []
        while uri:
            res = requests.get(uri,verify=False)
            if res.status_code == 200:
                data = res.json()
                uri = data.get('next',False)
                list_names += [{'title':i.get('title'),'created':i.get('created')} for i in data.get('results')]
            else:
                # log the error in case if status code is not 200 and return empty result
                print(res.status_code,res.json())
                uri = False
    
        return Response({'count':len(list_names),'movie_titles':list_names})

class SavedTitles(APIView):
    """
    List all planets locally saved, update or create a new planet.
    """
    serializer_class = StarWarsDataSerializer
    def get(self,request,format=None):
        PlanetsTitles = StarWarsPlanets.objects.all()
        serializer = StarWarsDataSerializer(PlanetsTitles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StarWarsDataSerializer(data=request.data)
        if serializer.is_valid():
            qs = StarWarsPlanets.objects.filter(title__iexact=request.data.get('title'))
            if qs.exists():
                qs.update(
                    my_title=serializer.data.get('my_title'),
                    favourite=serializer.data.get('favourite')
                )
                return Response(serializer.data)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

