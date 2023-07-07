from rest_framework import serializers

from outsourcing.models import Outsourcing


class OutsourcingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outsourcing
        fields = ['uuid',
                  'portfolio',
                  'field',
                  'title',
                  'original_file_provided',
                  'commercial_use_allowed',
                  'additional_modification_allowed',
                  'reprocessing_allowed',
                  'work_date',
                  'price',
                  'editable_count',
                  'price_change_allowed',
                  'outsourcing_method',
                  'promotion_text',
                  'created_at']
        read_only_fields = [
            'uuid',
            'portfolio',
            'created_at',
            'updated_at'
        ]

