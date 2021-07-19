from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from test_api.models import RegisterUser
from django.contrib.auth import authenticate,get_user_model


class RegisterUserSerializer(RegisterSerializer):
    # email = serializers.EmailField(
    #     required=True, unique = True)
    # last_period_date = serializers.DateField()
    # cycle_average = serializers.IntegerField()
    # leriod_average = serializers.IntegerField()
    # start_date = serializers.DateField()
    # end_date = serializers.DateField()
    # password = serializers.CharField(max_length=68, min_length=8, write_only=True,
    #                     style={'input_type': 'password'}, trim_whitespace=True)

    USERNAME_FIELD = 'email'
    username = None
    REQUIRED_FIELDS = []
    # def get_cleaned_data(self):
    #     data_dict = super().get_cleaned_data()
    #     data_dict['first_name'] = self.validated_data.get('first_name', '')
    #     data_dict['last_name'] = self.validated_data.get('last_name', '')
    #     data_dict['phone_number'] = self.validated_data.get('phone_number', '')
    #     return data_dict

class MembersUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=False,
        max_length=50,
    )
    last_period_date = serializers.DateField()
    
    cycle_average = serializers.IntegerField()
    Period_average = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    password = serializers.CharField(max_length=68, min_length=8, write_only=True,
                        style={'input_type': 'password'}, trim_whitespace=True)

    # subscription_type = serializers.MultipleChoiceField(
    #     choices=subscription_tarrif)

class LoginSerializer(serializers.ModelSerializer):
    """Login Serialization for email"""
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
    def _validate_email(self, email, password):
        user = None
        if email and password:
            user = authenticate(email=email, password=password)
        else:
            raise Exception.ValidationError('email does not exist')
        return user
    def validate(self, attrs):
        password = attrs.get('password')
        email = attrs.get('email')
        user = self._validate_email(email, password)
        attrs['user'] = user
        return attrs