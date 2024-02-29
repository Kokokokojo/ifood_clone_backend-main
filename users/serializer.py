from rest_framework import serializers
from users.models import CustomUser, Address



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

            'is_active',
            'is_superuser',
            'is_staff',
            'google_id',
        ]

    def create(self, validated_data):

        google_id = str(validated_data.get('google_id', ''))
        
        user = CustomUser.objects.create(
            google_id =google_id,
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

        