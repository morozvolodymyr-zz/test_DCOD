from django.conf.urls import url
from test_DCOD_app.views import DCODView, get_regions

urlpatterns = [
    url(r'^$', DCODView.as_view()),
    url(r'^add$', get_regions),
]
