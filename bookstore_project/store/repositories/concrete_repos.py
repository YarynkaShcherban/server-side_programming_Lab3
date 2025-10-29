from store.repositories.base_repo import BaseRepo
from store.models import *


class AuthorRepo(BaseRepo):
    def __init__(self):
        super().__init__(Author)

    def find_by_last_name(self, last_name):
        return self.model.objects.filter(last_name__icontains=last_name)

    def get_alive_authors(self):
        return self.model.objects.filter(death_date__isnull=True)

    def find_by_country(self, country):
        return self.model.objects.filter(country__iexact=country)


class BookRepo(BaseRepo):
    def __init__(self):
        super().__init__(Book)

    def find_by_name(self, name):
        return self.model.objects.filter(name__icontains=name)

    def get_books_by_publisher(self, publisher_id):
        return self.model.objects.filter(publisher_id=publisher_id)

    def get_books_cheaper_than(self, price):
        return self.model.objects.filter(price__lt=price)


# class AuthorBookRepo(BaseRepo):
#     def __init__(self):
#         super().__init__(AuthorBook)

#     def get_books_by_author(self, author_id):
#         return self.model.objects.filter(author_id=author_id)

#     def get_authors_by_book(self, book_id):
#         return self.model.objects.filter(book_id=book_id)


class ClientRepo(BaseRepo):
    def __init__(self):
        super().__init__(Client)

    def find_by_email(self, email):
        return self.model.objects.filter(email__iexact=email).first()

    def find_by_phone(self, phone):
        return self.model.objects.filter(phone__iexact=phone).first()


class PublisherRepo(BaseRepo):
    def __init__(self):
        super().__init__(Publisher)

    def find_by_email(self, email):
        return self.model.objects.filter(email__iexact=email)


class EmployeeRepo(BaseRepo):
    def __init__(self):
        super().__init__(Employee)

    def find_by_last_name(self, last_name):
        return self.model.objects.filter(last_name__icontains=last_name)

    def get_by_position(self, role):
        return self.model.objects.filter(position__role__icontains=role)

    def get_by_store(self, store_id):
        return self.model.objects.filter(store_id=store_id)


class PositionRepo(BaseRepo):
    def __init__(self):
        super().__init__(Position)

    def get_salary_range(self, min_salary, max_salary):
        return self.model.objects.filter(salary__gte=min_salary, salary__lte=max_salary)

    def find_by_role(self, role):
        return self.model.objects.filter(role__icontains=role)


class PurchaseRepo(BaseRepo):
    def __init__(self):
        super().__init__(Purchase)

    def get_by_client(self, client_id):
        return self.model.objects.filter(client_id=client_id)

    def get_by_employee(self, employee_id):
        return self.model.objects.filter(employee_id=employee_id)

    def get_by_store(self, store_id):
        return self.model.objects.filter(store_id=store_id)

    def get_by_date_range(self, start_date, end_date):
        return self.model.objects.filter(purchase_date__range=[start_date, end_date])


class PurchaseDetailRepo(BaseRepo):
    def __init__(self):
        super().__init__(PurchaseDetail)

    def get_by_purchase(self, purchase_id):
        return self.model.objects.filter(purchase_id=purchase_id)

    def get_total_sum_by_purchase(self, purchase_id):
        from django.db.models import F, Sum
        result = self.model.objects.filter(purchase_id=purchase_id).aggregate(
            total=Sum(F('quantity') * F('price_at_purchase'))
        )
        return result['total'] or 0


class GenreRepo(BaseRepo):
    def __init__(self):
        super().__init__(Genre)

    def find_by_name(self, name):
        return self.model.objects.filter(name__icontains=name)

    def get_genres_for_book(self, book):
        return self.model.objects.filter(book=book)


class StoreRepo(BaseRepo):
    def __init__(self):
        super().__init__(Store)

    def get_by_city(self, city):
        return self.model.objects.filter(city__icontains=city)

    def find_by_email(self, email):
        return self.model.objects.filter(email__iexact=email)