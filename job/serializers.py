from rest_framework import serializers
from .models import User,CandidateMaster, AcademicMaster,ExperienceMaster,LanguageKnownMaster,TechnologyKnownMaster,ReferenceMaster,PreferenceMaster

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = ('url', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


        def create(self,validated_data):
            password = validated_data.pop('password')
            user= User(**validated_data)
            user.set_password(password)
            user.save()
            return user


        def update(self,instance, validated_data):
            instance.email = validated_data.get("email", instance.email)
            instance.save()
            return instance

class AcademicSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = AcademicMaster
        fields= '__all__'

class ExperienceSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceMaster
        fields= '__all__'

class LanguageSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = LanguageKnownMaster
        fields= '__all__'



class TechnologySerialiazer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyKnownMaster
        fields= '__all__'




class ReferenceSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceMaster
        fields= '__all__'



class PreferenceSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = PreferenceMaster
        fields= '__all__'


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CandidateMaster
        fields = '__all__'
        def create(self, validated_data):
            candidate = CandidateMaster.objects.create(**validated_data)
            candidate.save()
            return candidate