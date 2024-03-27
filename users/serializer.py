from rest_framework import serializers
from users.models import CustomUser
from addresses.models import Address
from users.validators import CustomUserValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser

        fields = [
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'cpf',

            'created_at',
            'updated_at',
            'phone_confirmed_in',
            'email_confirmed_in',
            'is_active',
            'is_superuser',
            'is_staff',
            'receive_ads',
        ]

    def create(self, validated_data):
        user = CustomUser.objects.create(
            first_name = validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
            phone=validated_data.get('phone', '')
        )

        user.save()
        return user
        
       


class UserPatchCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'cpf',
            'is_active',
        ]


    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.is_active = True
        instance.save()

        return instance





# def required(value):
#     if value is None:
#         raise serializers.ValidationError('This field is required')
    
class UserPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'cpf',
        ]

    def validate(self, attrs):

        # if self.instance is not None and attrs.get('coisa_aqui') is None:
        #     attrs['coisa_aqui'] = self.instance.coisa_aqui
        
        CustomUserValidator(data=attrs, ErrorClass=serializers.ValidationError)

        return super().validate(attrs)