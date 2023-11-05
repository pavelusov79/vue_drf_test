import re

from rest_framework.serializers import ModelSerializer, ValidationError
from equipment.models import EquipmentType, Equipment


class TypeSerializer(ModelSerializer):
    """Сериализатор для модели EquipmentType (Тип оборудования)"""
    class Meta:
        model = EquipmentType
        fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    """Сериализатор для модели Equipment (Оборудование)"""
    class Meta:
        model = Equipment
        fields = '__all__'

    def validate(self, data):
        """Валидация по маске типа оборудования"""
        mask = data['fk_type'].mask_equipment
        if not re.match(mask, data['serial_number']):
            raise ValidationError(
                'Серийный номер не соответствует данном типу оборудования.'
            )
        return data
