from rest_framework import serializers
from .models import Categories, Transactions

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__   '
        read_only_fields = ['user']

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
        read_only_fields = ['user', 'date']

