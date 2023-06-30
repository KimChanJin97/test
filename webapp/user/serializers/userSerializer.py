from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from field.serializers import FieldSerializer
from user.models import User, UserUnivIdentification


class UserUnivIdentificationSerializer(serializers.ModelSerializer):
    univ_identification = serializers.ImageField(use_url=True)

    class Meta:
        model = UserUnivIdentification
        fields = ['univ_identification']


class UserSerializer(WritableNestedModelSerializer):
    univ_identifications = UserUnivIdentificationSerializer(many=True, read_only=True)

    def get_univ_identifications(self, obj):
        univ_identification = obj.univ_identification.all()
        return UserUnivIdentificationSerializer(instance=univ_identification, many=True, context=self.context).data

    class Meta:
        model = User
        fields = ['id', 'kakaoId', 'thumbnail_image', 'email', 'phone_number', 'name',
                  'birth_date', 'job', 'univ', 'major', 'univ_identifications']
        read_only_fields = ['id', 'kakaoId', 'thumbnail_image']

    def update(self, instance, validated_data):
        univ_identification_set = self.context['request'].FILES
        if 'univ_identification' in univ_identification_set:
            instance.univ_identification.all().delete()

            for univ_identification_data in univ_identification_set.getlist('univ_identification'):
                UserUnivIdentification.objects.create(user=instance, univ_identification=univ_identification_data)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['univ_identifications'] = UserUnivIdentificationSerializer(instance.univ_identification.all(), many=True).data
        return representation