
from .views import PlanetList,MovieList,SavedTitles,SavedTitle
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',ReportTypesViewSet.as_view(),name='fetch-data-api'),
    path('planets/',PlanetList.as_view(),name='fetch-planet-data'),
    path('movies/',MovieList.as_view(),name='fetch-movie-data'),
    path('savedtitle/<pk>/',SavedTitle.as_view(),name="fetch-single"),
    path('savedtitles/',SavedTitles.as_view(),name="fetch-local-data"),
]
