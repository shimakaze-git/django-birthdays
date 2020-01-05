from django.db.models.fields import DateField


class BirthdayField(DateField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
