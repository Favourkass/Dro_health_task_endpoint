from rest_framework.test import APITestCase
from test_api.views.create_cycle_view import CreateCycleView
from rest_framework import status
from django.urls import reverse
from test_api.models import RegisterUser
import datetime



class CreateCycleTest(APITestCase):
    def setUp(self):
        self.view = CreateCycleView()
        RegisterUser.objects.create(email='test@gmail.com',
                            password='password1234')

        self.valid_payload = {
            'last_period_date': '2021-07-14',
            'cycle_average': 25,
            'period_average': 5,
            'start_date': str(datetime.date.today()),
            'end_date': str(datetime.date.today()),
        }
        self.update_payload = {
            'last_period_date': str(datetime.date(2021, 7, 11)),
            'cycle_average': 23,
            'period_average': 5,
            'start_date': str(datetime.date(2021, 7, 14)),
            'end_date': str(datetime.date(2021, 11, 14)),
        }
        self.valid_url = reverse('create-cycle')
        self.sample_user = RegisterUser.objects.get(email='test@gmail.com')

    def test_create_cycle(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.post(
            self.valid_url,
            self.valid_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_cycle(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.post(
            self.valid_url,
            self.valid_payload,
            self.update_payload,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_response_data(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.post(
            self.valid_url,
            self.valid_payload,
            format='json'
        )

        self.assertEqual(res.data.get('total_created_cycles'),  1)

    def test_response_data_update(self):
        self.client.force_authenticate(user=self.sample_user)
        res = self.client.post(
            self.valid_url,
            self.valid_payload,
            self.update_payload,
            format='json'
        )
        self.assertEqual(res.data.get('total_created_cycles'),  4)
    
