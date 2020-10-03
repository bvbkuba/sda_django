from django.db.models import Model, CharField, IntegerField, DateField, DateTimeField, BooleanField, TextField, FloatField, ForeignKey, DO_NOTHING, Q
from datetime import datetime

from django.db.models.constraints import CheckConstraint


class Technology(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Course(Model):

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(max_atendees_count__gte=5) & Q(
                    max_atendees_count__lte=10),
                name='max_atendees_count_between_5_and_10'
            )
        ]

    title = CharField(max_length=128)
    technology_id = ForeignKey(Technology, on_delete=DO_NOTHING)
    description = TextField(blank=True, null=True)
    starts = DateField(default = datetime.now)
    finished = DateField(blank=True, null=True)
    max_atendees_count = IntegerField()
    price = FloatField(default=10.00)
    remote = BooleanField()
    test = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
