from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Order
import re


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True, source='user.username')

    class Meta:
        model = Profile
        fields = ('id', 'name', 'nickname', 'phone_number', 'email', 'sex')

    def is_valid(self, raise_exception=False):
        attrs = self.initial_data

        essential_fields = ['name', 'password', 'nickname', 'phone_number', 'email']
        for field in essential_fields:
            if field not in attrs.keys():
                self._errors = {'error': f'{field} is essential field'}
                return False

        # password check
        password = attrs['password']
        if len(password) < 10:
            self._errors = {'error': 'password length at least 10'}
            return False
        include_lowercase, include_uppercase, include_special_char = False, False, False
        for s in password:
            if s.islower():
                include_lowercase = True
            if s.isupper():
                include_uppercase = True
            p = re.match('^[a-zA-Z0-9가-힣]+', s)
            if not p:
                include_special_char = True

        print(include_lowercase, include_uppercase, include_special_char)
        if not (include_lowercase and include_uppercase and include_special_char):
            self._errors = {'error': 'wrong format "password"'}
            return False
        else:
            print('possible')

        # name check
        p = re.match('[가-힣a-zA-Z]+', attrs['name'])
        if attrs['name'] == p.group():
            print('possible')
        else:
            self._errors = {'error': 'wrong format "name"'}
            return False
        # nickname check
        p = re.match('[a-z]+', attrs['nickname'])
        if attrs['nickname'] == p.group():
            print('possible')
        else:
            self._errors = {'error': 'wrong format "nickname"'}
            return False
        # phone number check
        p = re.match('[0-9]+', attrs['phone_number'])
        print(p.group())
        if attrs['phone_number'] == p.group():
            print('possible')
        else:
            self._errors = {'error': 'wrong format "phone_number"'}
            return False
        # email check
        p = re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', attrs['email'])
        if p is not None:
            print('possible')
        else:
            self._errors = {'error': 'wrong format "email"'}
            return False
        # sex check
        if hasattr(attrs, 'sex'):
            if attrs['sex'] not in [str(c[0]) for c in Profile.SEX_CHOICE]:
                self._errors = {'error': 'sex field out of range'}
                return False

        self._errors = {}
        self._validated_data = attrs
        return True

    def create(self, validated_data):
        user = User(
            username=validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile(
            user=user,
            nickname=validated_data['nickname'],
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            sex=validated_data['sex'] if 'sex' in validated_data else None
        )
        profile.save()
        return profile


class ProfileWithLastOrderSerializer(serializers.ModelSerializer):
    last_order = serializers.SerializerMethodField(read_only=True)
    name = serializers.CharField(read_only=True, source='user.username')

    class Meta:
        model = Profile
        fields = ('id', 'name', 'nickname', 'phone_number', 'email', 'sex', 'last_order')

    def get_last_order(self, profile):
        orders = profile.orders.all()
        if orders:
            return OrderSerializer(orders.latest('dt_order')).data
        else:
            return None


class OrderSerializer(serializers.ModelSerializer):
    buyer = ProfileSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'buyer', 'order_number', 'product_name', 'dt_order')