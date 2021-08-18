# star-wars-rest-api
# Pull directly from docker 
https://hub.docker.com/r/danielhasan1/starwars-project
## Docker Setup:
OLD
run `docker pull danielhasan1/starwars-project`  
after pulling the image
run `docker run -tip8000:8000 --name starwars starwars-project /bin/bash`  
inside docker container navigate to `/opt/star-wars-api/starWarsApi`  
in base dir of django project run `gnicorn starWarsApi.wsgi:application --bind 0.0.0.0:8000` 
NEW
Just run `docker-compose up` by copying the file in your local in with any folder named as project to mount

## Or  
Optionally you can also clone this project. 
Create a virtual env  
run `pip install -r requirements.txt`  
directly run django from `manage.py runserver`  

# List of resources  
`/api/planets/` -> load all planets from star wars remote server (GET)  
`/api/movies/` -> load all movies from star wars remote server (GET)  
`/api/planets/?q=Name` -> search specefic planet on star wars remote server (GET)  
`/api/savedtitles/` -> if any planet name is saved then list of saved records will be returned. (GET or POST, ADD API)  
`/api/savedtitle/pk/` -> get or put specefic record via id or remove it (GET or PUT or DELETE)  
