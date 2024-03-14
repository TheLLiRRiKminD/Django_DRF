from rest_framework import serializers

from lms.models import Course
from lms.serializers import CourseSerializer
from services import stripe_session_create
from users.models import Payments, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class PaymentsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    price = CourseSerializer(source='paid_course.price', read_only=True)
    print(Course.price)

    class Meta:
        model = Payments
        fields = '__all__'

    def get_url(self):
        return stripe_session_create(self.price)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user
