from rest_framework import serializers
from .models import Candidate
import phonenumbers
import requests

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = '__all__'

    def validate(self, validate_data):
        """
            Validation Function
        """
        if validate_data.get('number'):
            '''
                Validating PhoneNumber
            '''
            phone_number = str(validate_data['number'])
            first_digit = phone_number[0]

            if not phone_number.startswith('+91'):
                phone_number = '+91' + phone_number[1:] if first_digit == '0'  else  '+91' + phone_number
                phone_number = phonenumbers.parse(str(phone_number))
                if not phonenumbers.is_valid_number(phone_number):
                    raise serializers.ValidationError('Given Number is not a Valid Number')

        if validate_data.get('location'):
            '''
                Validating City 
            '''
            data = requests.get('https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population')
            data  = data.text.lower()
            city_name = str(validate_data['location'])

            if city_name not in data:
                raise serializers.ValidationError('Given City is not Present in our Database Currently')

        return validate_data