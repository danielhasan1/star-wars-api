from rest_framework.test import APITestCase
from rest_framework import status
from star_wars_data.models import StarWarsPlanets
MOVIE_DATA_SET = {
    "count": 6,
    "movie_titles": [
        {
            "title": "A New Hope",
            "created": "2014-12-10T14:23:31.880000Z"
        },
        {
            "title": "The Empire Strikes Back",
            "created": "2014-12-12T11:26:24.656000Z"
        },
        {
            "title": "Return of the Jedi",
            "created": "2014-12-18T10:39:33.255000Z"
        },
        {
            "title": "The Phantom Menace",
            "created": "2014-12-19T16:52:55.740000Z"
        },
        {
            "title": "Attack of the Clones",
            "created": "2014-12-20T10:57:57.886000Z"
        },
        {
            "title": "Revenge of the Sith",
            "created": "2014-12-20T18:49:38.403000Z"
        }
    ]
}
class SavedTitles(APITestCase):

    def test_post_titles(self):
        data = {'title': 'new idea'}
        response = self.client.post('/api/savedtitles/',data)
        data = response.json()
        data.pop('timestamp')
        # test status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test posted data
        self.assertEqual(data, {'pk': 1, 'title': 'new idea','my_title': None,'favourite': False})
        title_count = StarWarsPlanets.objects.all().count()
        self.assertEqual(title_count,1)
        self.assertNotEqual(title_count,0)
    
    def test_sw_search_planet(self):
        data = {
                "count": 1,
                "planet_names": [
                    {
                        "name": "Alderaan",
                        "created": "2014-12-10T11:35:48.479000Z"
                    }
                ]
            }
        response = self.client.get('/api/planets/?q=Alderaan')
        # test planet search result
        self.assertEqual(response.json(), data)


    def test_sw_fetch_movie(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.json(), MOVIE_DATA_SET)