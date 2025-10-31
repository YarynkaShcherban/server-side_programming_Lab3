from store.repositories.concrete_repos import *


# єдина точка доступу
class RepoManager:
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