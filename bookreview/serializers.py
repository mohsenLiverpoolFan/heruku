from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    book_written = BookSerializer(read_only=True, many=True, source="book_set")
    kalam_yakonte = serializers.SerializerMethodField('sikim_agzoa')
    
    '''
    Serializer for Author
    '''

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'kalam_yakonte', 'book_written')

    def sikim_agzoa(self, obj):
        return "title is :{}".format(obj.last_name)
