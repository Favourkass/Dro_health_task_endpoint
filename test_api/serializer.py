from rest_framework import serializers


class CycleSerializer(serializers.Serializer):
    Last_period_date = serializers.DateField()
    cycle_average=serializers.CharField()
    period_average=serializers.CharField()
    start_date=serializers.DateField()
    end_date=serializers.DateField()