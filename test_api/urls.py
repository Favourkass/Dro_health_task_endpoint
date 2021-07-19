from django.urls import path, include
from test_api.views.create_cycle_view import CreateCycleView
from django.conf.urls import url 
from test_api.views.cycle_event import CycleEventTracker

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path('create-cycles/', CreateCycleView.as_view(), name='create-cycle'),
    url(r'^cycle-event?(?P<date>.+)/$', CycleEventTracker.as_view(), name = 'cycle-event'),
    # http://localhost:8080/women-health/api/cycle-event?date=2021-20-19
]