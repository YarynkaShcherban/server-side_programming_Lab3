import os
import django
from datetime import date
from decimal import Decimal

# Налаштування Django для standalone скрипта
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_project.settings")
django.setup()


def main():
    from store.repositories.repo_manager import RepoManager
    from store.models import (
        Store,
        Position,
        Employee,
        Author,
        Publisher,
        Book,
        Client,
        Genre,
        Purchase,
        PurchaseDetail,
    )

    repo = RepoManager()

    print("Очистка бази даних...")
    PurchaseDetail.objects.all().delete()
    Purchase.objects.all().delete()
    Genre.objects.all().delete()
    Book.objects.all().delete()
    Publisher.objects.all().delete()
    Author.objects.all().delete()
    Employee.objects.all().delete()
    Position.objects.all().delete()
    Client.objects.all().delete()
    Store.objects.all().delete()
    print(" Усі таблиці очищено!\n")

    store1 = repo.stores.model.objects.create(
        name="The Book Loft",
        city="Columbus",
        address="631 South Third St.",
        phone="1234567891",
        email="info@bookloft.com",
    )

    position1 = repo.positions.model.objects.create(role="Store Manager", salary=Decimal("2500.00"))
    position2 = repo.positions.model.objects.create(role="Sales Assistant", salary=Decimal("1200.00"))
    position3 = repo.positions.model.objects.create(role="Inventory Specialist", salary=Decimal("1800.00"))
    position4 = repo.positions.model.objects.create(role="Customer Support", salary=Decimal("1500.00"))

    employee_data = [
        ("John", "Doe", date(1985, 4, 12), "+1-614-555-1234", "john.doe@example.com", position1),
        ("Emily", "Smith", date(1990, 7, 22), "+1-212-555-5678", "emily.smith@example.com", position2),
        ("Michael", "Johnson", date(1988, 2, 5), "+44-20-555-7890", "michael.johnson@example.co.uk", position3),
        ("Sophie", "Brown", date(1995, 11, 30), "+1-503-555-3456", "sophie.brown@example.com", position4),
    ]
    for fn, ln, bd, ph, em, pos in employee_data:
        repo.employees.model.objects.create(
            first_name=fn,
            last_name=ln,
            birth_date=bd,
            phone=ph,
            email=em,
            position=pos,
            store=store1,
        )

    authors_data = [
        ("Agatha", "Christie", None, date(1890, 9, 15), date(1976, 1, 12), "UK"),
        ("Haruki", "Murakami", None, date(1949, 1, 12), None, "Japan"),
        ("George", "Orwell", None, date(1903, 6, 25), date(1950, 1, 21), "UK"),
        ("Ernest", "Hemingway", None, date(1899, 7, 21), date(1976, 7, 2), "USA"),
    ]
    authors = []
    for fn, ln, ps, bd, dd, ctry in authors_data:
        authors.append(
            repo.authors.model.objects.create(
                first_name=fn,
                last_name=ln,
                pseudonym=ps,
                birth_date=bd,
                death_date=dd,
                country=ctry,
            )
        )

    publishers_data = [
        ("Penguin", "contact@penguin.com", "1234567890", "London, UK"),
        ("Random House", "info@randomhouse.com", "0987654321", "New York, USA"),
        ("Knopf Publishing Group", "info@knopf.com", "0979812044", "New York, USA"),
    ]
    publishers = []
    for name, email, phone, addr in publishers_data:
        publishers.append(
            repo.publishers.model.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=addr,
            )
        )

    books_data = [
        ("Murder on the Orient Express", "9780062693662", Decimal("15.00"), publishers[1]),
        ("New Age Book", "1234567890123", Decimal("20.00"), publishers[1]),
        ("Kafka on the Shore", "9781400079278", Decimal("18.50"), publishers[2]),
        ("1984", "9780451524935", Decimal("14.00"), publishers[2]),
        ("The Old Man and the Sea", "9780684801223", Decimal("13.50"), publishers[1]),
    ]
    books = []
    for name, isbn, price, pub in books_data:
        books.append(repo.books.model.objects.create(name=name, isbn=isbn, price=price, publisher=pub))

    clients_data = [
        ("Yaryna", "Panychevska", "pa.yaryna@gmail.com", "0979812088"),
        ("Yaryna", "Shcherban", "yaryna.shcherban@gmail.com", "0979812099"),
    ]
    clients = []
    for fn, ln, email, phone in clients_data:
        clients.append(repo.clients.model.objects.create(first_name=fn, last_name=ln, email=email, phone=phone))

    genres_names = ["Fiction", "Mystery", "Classic", "Adventure", "Dystopian", "Fantasy", "Self-Help"]
    genres = [repo.genres.model.objects.create(name=gname) for gname in genres_names]

    authors[0].book.add(books[0], books[1])
    authors[1].book.add(books[2])
    authors[2].book.add(books[3])
    authors[3].book.add(books[4])

    genres[0].book.add(*books)
    genres[1].book.add(books[0])
    genres[2].book.add(books[3], books[4])
    genres[3].book.add(books[0], books[2], books[4])
    genres[4].book.add(books[3])
    genres[5].book.add(books[2])
    genres[6].book.add(books[1])

    purchase1 = repo.purchases.model.objects.create(
        client=clients[0],
        store=store1,
        employee=repo.employees.model.objects.get(email="emily.smith@example.com"),
        total_amount=Decimal("29.00"),
    )

    repo.purchase_details.model.objects.create(
        purchase=purchase1, book=books[0], quantity=1, price_at_purchase=books[0].price
    )
    repo.purchase_details.model.objects.create(
        purchase=purchase1, book=books[3], quantity=1, price_at_purchase=books[3].price
    )


def demo_queries():
    from store.repositories.repo_manager import RepoManager
    repo = RepoManager()

    print("\n=== Демонстрація роботи репозиторіїв ===")

    print("\n Усі автори з Великобританії (UK):")
    for a in repo.authors.find_by_country("UK"):
        print(f"  - {a.first_name} {a.last_name}")

    print("\n Автори, які ще живі:")
    for a in repo.authors.get_alive_authors():
        print(f"  - {a.first_name} {a.last_name}")

    print("\n Книги, ціна яких нижча за 16.00:")
    for b in repo.books.get_books_cheaper_than(16.00):
        print(f"  - {b.name} ({b.price} $)")

    print("\n Книги, які видав Penguin:")
    publisher = repo.publishers.model.objects.get(name="Penguin")
    for b in repo.books.get_books_by_publisher(publisher.publisher_id):
        print(f"  - {b.name}")

    print("\n Усі працівники магазину:")
    for e in repo.employees.get_all():
        print(f"  - {e.first_name} {e.last_name}, {e.position.role}")

    print("\n Знайти працівників за посадою 'Sales Assistant':")
    for e in repo.employees.get_by_position("Sales Assistant"):
        print(f"  - {e.first_name} {e.last_name}")

    print("\n Посади з окладом від 1200 до 2000:")
    for p in repo.positions.get_salary_range(1200, 2000):
        print(f"  - {p.role} ({p.salary} $)")

    print("\n Всі покупки:")
    for purchase in repo.purchases.get_all():
        print(f"  - Покупка #{purchase.purchase_id}, клієнт: {purchase.client.first_name}, сума: {purchase.total_amount} $")


if __name__ == "__main__":
    main()
    demo_queries()