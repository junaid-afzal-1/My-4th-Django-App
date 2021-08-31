from django.db.models import fields
from SerializerTry.models import Person,Student
from rest_framework import serializers



class PersonSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    age = serializers.PositiveIntegerField()
    contact = serializers.CharField(max_length=15)

    def create(self, validated_data):
        return Person.objects.create(validated_data)


    def update(self, instance, validated_data):

        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.age)
        instance.contact = validated_data.get('contact',instance.contact)

        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['name','contact','roll_no','section','cgpa','semester']