from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','subtitle','content','author','isbn','price',)

    def validate(self,data):
        title = data.get('title',None)
        author = data.get('author',None)

        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":'Siz kitobning nomini kiritishda raqamlardan foydalandinggiz!'
                }
            )
        if Book.objects.filter(title=title,author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": 'Bazada bunday kitob mavjud'
                }
            )
        return data

    def validate_price(self,price):
        if price <0 or price>9999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": 'siz mumkin bo\'lmagan qiymat kiritdinggiz'
                }
            )
        return price