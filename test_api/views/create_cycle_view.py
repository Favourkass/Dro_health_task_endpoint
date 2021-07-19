from django.shortcuts import render
from rest_framework.serializers import Serializer
from test_api.serializers.create_cycle_serializer import CycleSerializer
from rest_framework.views import APIView
from test_api.models import RegisterUser
from datetime import datetime
import math
from rest_framework.response import Response



class CreateCycleView(APIView):
    serializer_class = CycleSerializer
    date_format = "%d/%m/%Y"

    def change_date_format(self, date):
        new_date=date.split("-")
        return "/".join(new_date[::-1])

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        last_period_date = data.get('last_period_date', '')
        cycle_average = data.get('cycle_average', '')
        period_average = data.get('period_average', '')
        start_date = data.get('start_date', '')
        end_date = data.get('end_date', '')
        print(data)

        if serializer.is_valid() and request.user.is_authenticated:
            update = RegisterUser.objects.get(email=request.user.email)
            update.last_period_date= serializer.data.get('last_period_date')
            update.cycle_average= serializer.data.get('cycle_average')
            update.period_average= serializer.data.get('period_average')
            update.start_date= serializer.data.get('start_date')
            update.end_date= serializer.data.get('end_date')
            update.save()
            format_start_date=self.change_date_format(start_date)
            format_end_date = self.change_date_format(end_date)

            start_date_obj = datetime.strptime(format_start_date, self.date_format)
            end_date_obj = datetime.strptime(format_end_date, self.date_format) 
            
            number_of_days = end_date_obj - start_date_obj
            total_average= int(cycle_average) + int(period_average)
            cycle = math.floor(number_of_days.days/total_average)

            if(cycle<1):
                cycle=1 
                  
            return Response({"total_created_cycles": cycle })

        return Response({"error":serializer.errors})


