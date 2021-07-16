from django.shortcuts import render
from rest_framework.serializers import Serializer
from test_api.serializer import CycleSerializer
from rest_framework.views import APIView
from datetime import datetime
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
        start_date = data.get('start_date', '')
        cycle_average = data.get('cycle_average', '')
        period_average = data.get('period_average', '')
        start_date = data.get('start_date', '')
        end_date = data.get('end_date', '')

        if serializer.is_valid():
            format_start_date=self.change_date_format(start_date)
            format_end_date = self.change_date_format(end_date)

            start_date_obj = datetime.strptime(format_start_date, self.date_format)
            end_date_obj = datetime.strptime(format_end_date, self.date_format) 
            

            number_of_days = end_date_obj - start_date_obj
            total_average= int(cycle_average) + int(period_average)
            cycle = number_of_days.days/total_average
            if(cycle<1):
                cycle=1
                
            return Response({"total_created_cycles": cycle })

        return Response({"error":serializer.errors})


