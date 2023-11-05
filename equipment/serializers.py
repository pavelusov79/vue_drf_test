import re

from rest_framework.serializers import ModelSerializer, ValidationError, StringRelatedField
from equipment.models import EquipmentType, Equipment


class TypeSerializer(ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):

    class Meta:
        model = Equipment
        fields = '__all__'

    def validate(self, data):
        mask = data['fk_type'].mask_equipment
        if not re.match(mask, data['serial_number']):
            raise ValidationError(
                'Серийный номер не соответствует данном типу оборудования.'
            )
        return data


