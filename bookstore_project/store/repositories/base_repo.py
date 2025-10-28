from abc import ABC, abstractmethod
from django.db.models import Model


class BaseRepo(ABC):
    def __init__(self, model: Model):
        self.model = model

    def get_all(self):  # вичитика всіх даних
        return self.model.objects.all()

    def get_by_id(self, _id):  # пошук по ID
        try:
            return self.model.objects.get(pk=_id)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):  # створення нового екземпляру
        return self.model.objects.create(**kwargs)
