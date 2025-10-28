from base_repo import BaseRepo
from store.models import *


class AuthorRepo(BaseRepo):
    def __init__(self):
        super().__init__(Author)


class BookRepo(BaseRepo):
    def __init__(self):
        super().__init__(Book)


class ClientRepo(BaseRepo):
    def __init__(self):
        super().__init__(Client)


class PublisherRepo(BaseRepo):
    def __init__(self):
        super().__init__(Publisher)


class EmployeeRepo(BaseRepo):
    def __init__(self):
        super().__init__(Employee)


class PositionRepo(BaseRepo):
    def __init__(self):
        super().__init__(Position)


class PurchaseRepo(BaseRepo):
    def __init__(self):
        super().__init__(Purchase)


class PurchaseDetailRepo(BaseRepo):
    def __init__(self):
        super().__init__(PurchaseDetail)


class GenreRepo(BaseRepo):
    def __init__(self):
        super().__init__(Genre)


class StoreRepo(BaseRepo):
    def __init__(self):
        super().__init__(Store)
