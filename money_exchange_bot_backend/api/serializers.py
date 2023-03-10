from rest_framework import serializers

from exchange.models import User, Request


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'fee', 'paid_fee', 'role')
        read_only_fields = ('id', 'referrer',)
        model = User


class UserAdminSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username',  'role', 'referrer', 'paid_fee', 'fee')
        model = User


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id', 'creation_date', 'owner', 'status', 'city', 'sold_currency', 'sold_currency_amount',
            'purchased_currency_amount', 'currency_rate', 'commission_fee',
        )
        model = Request
