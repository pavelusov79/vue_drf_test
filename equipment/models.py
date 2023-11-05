from django.db import models


class EquipmentType(models.Model):
    """Модель Тип оборудования"""
    type_equipment = models.CharField(verbose_name='тип оборудования', max_length=16)
    mask_equipment = models.CharField(verbose_name='маска серийного номера', max_length=80)

    class Meta:
        verbose_name_plural = 'Тип оборудования'

    def __str__(self):
        return self.type_equipment


class Equipment(models.Model):
    """Модель Оборудование, связанная по ключу с моделью EquipmentType (Тип оборудования)"""
    serial_number = models.CharField(verbose_name='серийный номер', max_length=10, unique=True)
    text = models.CharField(verbose_name='примечание', max_length=512)
    fk_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='equipment')

    class Meta:
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.serial_number


