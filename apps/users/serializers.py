from rest_framework import serializers

from apps.users.models import User 
from apps.users.admin import UserAdmin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'profile_image')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=100, write_only=True
    )
    username = serializers.CharField(
        max_length=100, write_only=True
    )


    class Meta:
        model = User 
        fields = ('username', 'profile_image', 'password', 'confirm_password')

    def validate(self,attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        common_passwords = ['1234567890', 'qwertyui', '12345678','123456789','asdfghjkl',] 
        if password != confirm_password:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        elif password == username:
            raise serializers.ValidationError("password:Пароль и имя одиннаковы")
        elif len(password) < 8:
            raise serializers.ValidationError("Password:Пароль слишком короткий ")
        elif password in common_passwords:
            raise serializers.ValidationError("Password:Пароль слишком простой")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            profile_image=validated_data['profile_image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user