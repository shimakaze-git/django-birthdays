# from django.core.exceptions import FieldError
from django.db.models.fields import DateField

# from django.db.models.fields import DateField, PositiveSmallIntegerField
# from django.db.models.signals import pre_save


def pre_save_listener(instance, **kwargs):
    print("pre_save_listener instance", instance)
    field_obj = instance._meta.birthday_field

    birthday = getattr(instance, field_obj.name)
    if not birthday:
        return
    setattr(instance, field_obj.doy_name, birthday.timetuple().tm_yday)


class BirthdayField(DateField):
    """BirthdayField

    Args:
        DateField ([type]): [description]
    """
