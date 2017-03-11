from django.conf.urls import url
from .views import ShortenerView, RedirectView

urlpatterns = [
    url(r'url', ShortenerView.as_view(), name='shortener-view'),
    url(r'(?P<short>\w{0,5})/$', RedirectView.as_view(), name='shortener-view'),]
