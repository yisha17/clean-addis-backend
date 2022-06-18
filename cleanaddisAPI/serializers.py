
from rest_framework import serializers
#from yaml import serialize
from .models import Address, Announcement, Company, Notifications, PublicPlace, Report, Seminar, User, Waste, WorkSchedule
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['role'] = self.user.role
        data['address'] = self.user.address
        return data



class UserSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(
        max_length=None, use_url=True
    )
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = '__all__'
        print("working here")

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password','address','phone']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 



class RegisterWebSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email', 'password','role','address']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance   

class UpdatePasswordSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = User
        fields = ['password']
        extra_kwargs = {
            'password': {'write_only': True},
        }


    def update(self, instance, validated_data):
    # #     print(validated_data)
        
        password = validated_data.pop('password', None)
    #     # email = validated_data['email']
    #     # username = validated_data['username']
        
        
    #     # address = validated_data['address']
    #     # phone = validated_data['phone']
    #     instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
    #     # if email is not None:
    #     #     instance.email = validated_data['email']
    #     # if username is not None:
    #     #     instance.username = validated_data['username']
    #     # if validated_data['profile'] is not None:
    #     #     instance.profile = validated_data['profile']
    #     # if phone is not None:
    #     #     instance.phone = validated_data['phone']
    #     # if address is not None:
    #     #     instance.address = validated_data['address']
        
        
        instance.save()
        return instance

        


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','address','phone','profile']

        
class AddressSerializer(serializers.ModelSerializer):
    model = Address
    fields = '__all__'
class CompanySerializer(serializers.ModelSerializer):

    address = AddressSerializer(many=True)

    class Meta:

        model = Company
        depth = 1
        fields = '__all__'


class WasteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waste
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waste
        lookup_field = 'buyer'
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Waste
        lookup_field = 'seller'
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ReporterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = '__all__'
        lookup_field = 'reportedBy'
class PublicPlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PublicPlace
        fields = '__all__'
        lookup_field = 'publicType'
class SeminarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seminar
        fields = '__all__'
class WorkScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkSchedule
        fields = '__all__'
class AnnouncementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Announcement
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'