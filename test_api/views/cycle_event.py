from django.http import request
import math
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from test_api.models import RegisterUser
from datetime import timedelta, datetime

class CycleEventTracker(APIView):
    date_format = "%Y-%m-%d"

    def change_date_format(self, date):
        new_date=date.split("-")
        return "-".join(new_date[::-1])

    def find_date(self, given_date, list_dates):
            for key, value in list_dates.items():
                if given_date in value:
                    return key
            return "Out Of Specified Range or Nothing today"

    def get(self, request, date):

        date1 = request.GET.get('date', '')
        change_gotten_date = self.change_date_format(date1)
        current_user = RegisterUser.objects.get(id=request.user.id)
        try:
            last_period_date=current_user.last_period_date
            cycle_average=current_user.cycle_average
            period_average=current_user.period_average
            start_date=current_user.start_date
            end_date=current_user.end_date
            
        except:
            return Response({"status": "failure", "message": "Sorry please follow the instructions on the readme"})

       

        date_difference = end_date - start_date

        period_start_date =[]
        for i in range(1, date_difference.days + 1):
             if i %cycle_average==0:
                 gotten_date = last_period_date+timedelta(days=i)
                 period_start_date.append(gotten_date.strftime(self.date_format))

        period_end_date = []
        for i in range(1, date_difference.days + 1):
            if i % (period_average + cycle_average)== 0:
                gotten_date1=last_period_date + timedelta(days=i)
                period_end_date.append(gotten_date1.strftime(self.date_format))

        ovulation_date = []
        for i in range(1, date_difference.days + 1):
            if i % (math.floor(cycle_average/2) + cycle_average) == 0:
                gotten_date2 = last_period_date + timedelta(days=i)
                ovulation_date.append(gotten_date2.strftime(self.date_format))
                

        
        fertility_window = []
        for i in range(1, date_difference.days + 1):
            if i % (math.floor(cycle_average/2) + cycle_average) == 0:
                get_ovulation_date = last_period_date + timedelta(days=i)
                fertility_window_start = get_ovulation_date - timedelta(days=4)
                fertility_window_end = get_ovulation_date + timedelta(days=4)
                format_date1=fertility_window_start.strftime(self.date_format)
                format_date2=fertility_window_end.strftime(self.date_format)
                fertility_window.append(format_date1)
                fertility_window.append(format_date2)

        
        pre_ovlation_window = []
        for i in range(0, date_difference.days + 1):
            if i % (1+(period_average + cycle_average)) == 0:
                after_period_end = last_period_date + timedelta(days=i)
                pre_ovlation_window_start = after_period_end - timedelta(days=4)
                pre_ovlation_window_end = after_period_end + timedelta(days=4)

                
        dates = {"fertility_window":fertility_window,
                 "period_start_date":period_start_date, 
                 "period_end_date":period_end_date, 
                 "ovulation_date":ovulation_date,}

        return Response({"event": self.find_date(change_gotten_date, dates), "date": change_gotten_date})
    





    



