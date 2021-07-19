from rest_framework.test import APITestCase
from test_api.views.cycle_event import CycleEventTracker
from rest_framework import status
from django.urls import reverse
from test_api.models import RegisterUser
import datetime
import pdb


class TestCycleEvent(APITestCase):
    def setUp(self):
        self.view = CycleEventTracker()
        self.user=RegisterUser.objects.create(email='test@gmail.com',
                            password='password1234')
        
        
        self.create_url = reverse('create-cycle')
        self.url = reverse('cycle-event', kwargs={'date':'2021-04-19'})
        self.valid_payload = {
            'last_period_date': datetime.date(2021, 7, 14),
            'cycle_average': 25,
            'period_average': 5,
            'start_date': datetime.date(2021, 7, 26),
            'end_date': datetime.date(2022, 7, 26),
        }
         

        print("difference between dates", datetime.date(2024, 7, 26)-datetime.date(2022, 7, 26))
        self.sample_user = RegisterUser.objects.get(email='test@gmail.com')
        

    def test_cycle_event(self):
        self.client.force_authenticate(self.sample_user)
        res = self.client.post(self.create_url, self.valid_payload, format='json')
        print(res.data)
        response=self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_response(self):
        self.client.force_authenticate(self.sample_user)
        res = self.client.post(self.create_url, self.valid_payload, format='json')
        response=self.client.get('/womens-health/api/cycle-event/?date=24-08-2021')
        self.assertEqual(response.data,{"event":"fertility_window", "date":"2021-08-24" } )

        



