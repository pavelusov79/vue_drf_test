from django_filters import rest_framework as filters

from equipment.models import EquipmentType, Equipment


class TypeFilter(filters.FilterSet):
    """Фильтр для модели EquipmentType по полю тип оборудования"""
    type_equipment = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = EquipmentType
        fields = ['type_equipment']


class EquipmentFilter(filters.FilterSet):
    """Фильтр для оборудования по полю серийный номер"""
    serial_number = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Equipment
        fields = ['serial_number']
