# star-wars-rest-api
# Pull directly from docker 
https://hub.docker.com/r/danielhasan1/starwars-project
## Docker Setup:

## NEW  
Prerequisites - docker, docker-compose  
Just run `docker-compose up` by copying the `docker-compose.yml` file in your local and you will get a running django server without having to perform any extra steps.  
You can customise the file as per your requirement like changing the mount folder name etc. There is no need to copy the project as image already contains the project.  
Hit `localhost:8000` with below listed resources in your browser.
## OLD
run `docker pull danielhasan1/starwars-project`  
after pulling the image
run `docker run -tip8000:8000 --name starwars starwars-project /bin/bash`  
inside docker container navigate to `/opt/star-wars-api/starWarsApi`  
in base dir of django project run `gnicorn starWarsApi.wsgi:application --bind 0.0.0.0:8000`  

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
