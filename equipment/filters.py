from django_filters import rest_framework as filters

from equipment.models import EquipmentType, Equipment


class TypeFilter(filters.FilterSet):
    type_equipment = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = EquipmentType
        fields = ['type_equipment']


class EquipmentFilter(filters.FilterSet):
    grade = filters.CharFilter(lookup_expr='icontains')
    serial_number = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Equipment
        fields = ['grade', 'serial_number']
