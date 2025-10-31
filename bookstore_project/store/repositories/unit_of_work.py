from store.repositories.author_repo import AuthorRepo
from store.repositories.book_repo import BookRepo
from store.repositories.client_repo import ClientRepo
from store.repositories.publisher_repo import PublisherRepo
from store.repositories.employee_repo import EmployeeRepo
from store.repositories.position_repo import PositionRepo
from store.repositories.purchase_repo import PurchaseRepo
from store.repositories.purchase_detail_repo import PurchaseDetailRepo
from store.repositories.genre_repo import GenreRepo
from store.repositories.store_repo import StoreRepo


class UnitOfWork:
    def __init__(self):
        self.authors = AuthorRepo()
        self.books = BookRepo()
        self.clients = ClientRepo()
        self.publishers = PublisherRepo()
        self.employees = EmployeeRepo()
        self.positions = PositionRepo()
        self.purchases = PurchaseRepo()
        self.purchase_details = PurchaseDetailRepo()
        self.genres = GenreRepo()
        self.stores = StoreRepo()

    def clear_all(self):
        self.purchase_details.model.objects.all().delete()
        self.purchases.model.objects.all().delete()
        self.books.model.objects.all().delete()
        self.authors.model.objects.all().delete()
        self.clients.model.objects.all().delete()
        self.employees.model.objects.all().delete()
        self.genres.model.objects.all().delete()
        self.positions.model.objects.all().delete()
        self.publishers.model.objects.all().delete()
        self.stores.model.objects.all().delete()
