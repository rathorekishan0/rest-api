from rest_framework import serializers
from . import models

class helloserializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)

class userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields=('name','email','age','password','id')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user=models.UserProfile(email=validated_data['email'],name=validated_data['name'],age=validated_data['age'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class profilefeedserializer(serializers.ModelSerializer):
    class Meta:
        model=models.profilefeedmodel
        fields=('id','user_profile','status_text','created_on')
        extra_kwargs={'user_profile':{'read_only':True}}