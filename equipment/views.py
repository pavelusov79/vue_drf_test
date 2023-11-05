from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from equipment.serializers import TypeSerializer, EquipmentSerializer
from equipment.models import EquipmentType, Equipment
from equipment.filters import TypeFilter, EquipmentFilter


class TypeViewSet(ModelViewSet):
    """ModelVieSet для модели EquipmentType (Тип оборудования)"""
    queryset = EquipmentType.objects.all()
    serializer_class = TypeSerializer
    filterset_class = TypeFilter


class EquipmentViewSet(ModelViewSet):
    """ModelVieSet для модели Equipment (Оборудование)"""
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filterset_class = EquipmentFilter

    def create(self, request, *args, **kwargs):
        """Возможность добавления сразу нескольких объектов"""
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
