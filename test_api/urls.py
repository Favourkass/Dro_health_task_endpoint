from django.urls import path, include
from test_api.views.create_cycle_view import CreateCycleView

urlpatterns = [
    path('create-cycles', CreateCycleView.as_view(), name='create-cycle'),
]