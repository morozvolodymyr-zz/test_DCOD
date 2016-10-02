from django.conf.urls import url
from test_DCOD_app.views import DCODView, get_regions, update_region

urlpatterns = [
    url(r'^$', DCODView.as_view()),
    url(r'^add$', get_regions),
    url(r'^update_region', update_region),
    url(r'^statistics$', get_regions),
]
