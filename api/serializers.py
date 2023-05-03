from rest_framework import serializers
from .models import Student


#validation with validators
def start_with_k(value):
    if value[0].lower()!='k':  
        raise serializers.ValidationError("Name should start with k")
    return value

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length =100,validators=[start_with_k])
    class Meta:
        model = Student
        fields = ['name','rollNo','address']
        
#field level validaiton
    def validate_rollNo(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Erro')
        return value

#object level validation
    def validate(self, data):
        name = data.get('name')
        rollNo = data.get('rollNo')
        if rollNo>=200 and name.lower() == 'kuldeep':
            raise serializers.ValidationError('object level validation')
        return data
        
        
        