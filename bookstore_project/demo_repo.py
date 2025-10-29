import os
import django
from datetime import date
from decimal import Decimal

# Налаштування Django для standalone скрипта
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_project.settings")
django.setup()


def main():
    from store.repositories.repo_manager import RepoManager
    repo = RepoManager()

    store1 = repo.stores.create(
        name="The Book Loft",
        city="Columbus",
        address="631 South Third St.",
        phone="1234567891",
        email="info@bookloft.com")

    position1 = repo.positions.create(
        role="Store Manager",
        salary=Decimal("2500.00"))

    position2 = repo.positions.create(
        role="Sales Assistant",
        salary=Decimal("1200.00"))

    position3 = repo.positions.create(
        role="Inventory Specialist",
        salary=Decimal("1800.00"))

    position4 = repo.positions.create(
        role="Customer Support",
        salary=Decimal("1500.00"))

    employee1 = repo.employees.create(
        first_name="John",
        last_name="Doe",
        birth_date=date(1985, 4, 12),
        phone="+1-614-555-1234",
        email="john.doe@example.com",
        position=position1,
        store=store1
    )

    employee2 = repo.employees.create(
        first_name="Emily",
        last_name="Smith",
        birth_date=date(1990, 7, 22),
        phone="+1-212-555-5678",
        email="emily.smith@example.com",
        position=position2,
        store=store1
    )

    employee3 = repo.employees.create(
        first_name="Michael",
        last_name="Johnson",
        birth_date=date(1988, 2, 5),
        phone="+44-20-555-7890",
        email="michael.johnson@example.co.uk",
        position=position3,
        store=store1
    )

    employee4 = repo.employees.create(
        first_name="Sophie",
        last_name="Brown",
        birth_date=date(1995, 11, 30),
        phone="+1-503-555-3456",
        email="sophie.brown@example.com",
        position=position4,
        store=store1
    )

    author1 = repo.authors.create(
        first_name="Agatha", last_name="Christie", pseudonym=None,
        birth_date=date(1890, 9, 15), death_date=date(1976, 1, 12), country="UK"
    )

    author2 = repo.authors.create(
        first_name="Haruki", last_name="Murakami", pseudonym=None,
        birth_date=date(1949, 1, 12), death_date=None, country="Japan"
    )

    author3 = repo.authors.create(
        first_name="George", last_name="Orwell", pseudonym=None,
        birth_date=date(1903, 6, 25), death_date=date(1950, 1, 21), country="UK"
    )

    author4 = repo.authors.create(
        first_name="Ernest", last_name="Hemingway", pseudonym=None,
        birth_date=date(1899, 7, 21), death_date=date(1976, 7, 2), country="USA"
    )

    pub1 = repo.publishers.create(
        name="Penguin", email="contact@penguin.com", phone="1234567890", address="London, UK")

    pub2 = repo.publishers.create(
        name="Random House", email="info@randomhouse.com", phone="0987654321", address="New York, USA")

    pub3 = repo.publishers.create(
        name="Knopf Publishing Group", email="info@knopf.com", phone="0979812044", address="New York, USA")

    book1 = repo.books.create(name="Murder on the Orient Express",
                              isbn="9780062693662", price=Decimal("15.00"), publisher=pub2)

    book2 = repo.books.create(
        name="New Age Book", isbn="1234567890123", price=Decimal("20.00"), publisher=pub2)

    book3 = repo.books.create(
        name="Kafka on the Shore", isbn="9781400079278", price=Decimal("18.50"), publisher=pub3)

    book4 = repo.books.create(
        name="1984",
        isbn="9780451524935", price=Decimal("14.00"), publisher=pub3)

    book5 = repo.books.create(
        name="The Old Man and the Sea",
        isbn="9780684801223", price=Decimal("13.50"), publisher=pub2)

    client1 = repo.clients.create(
        first_name="Yaryna", last_name="Panychevska", email="pa.yaryna@gmail.com", phone="0979812088")

    client2 = repo.clients.create(
        first_name="Yaryna", last_name="Shcherban", email="yaryna.shcherban@gmail.com", phone="0979812099"
    )

    genre1 = repo.genres.create(name="Fiction")
    genre2 = repo.genres.create(name="Mystery")
    genre3 = repo.genres.create(name="Classic")
    genre4 = repo.genres.create(name="Adventure")
    genre5 = repo.genres.create(name="Dystopian")
    genre6 = repo.genres.create(name="Fantasy")
    genre7 = repo.genres.create(name="Self-Help")

    author1.book.add(book1)
    author1.book.add(book2)
    author2.book.add(book3)
    author3.book.add(book4)
    author4.book.add(book5)

    genre1.book.add(book1, book2, book3, book4, book5)
    genre2.book.add(book1)
    genre3.book.add(book4, book5)
    genre4.book.add(book1, book3, book5)
    genre5.book.add(book4)
    genre6.book.add(book3)
    genre7.book.add(book2)

    # purchase1 = repo.purchases.create(
    #     client=client1, employee=employee2, store=store1, total_amount=Decimal("29.00"))

    # purchase_detail1 = repo.purchase_details.create(
    #     purchase=purchase1, book=book1, quantity=1, price_at_purchase=book1.price)

    # purchase_detail1_2 = repo.purchase_details.create(
    #     purchase=purchase1, book=book4, quantity=1, price_at_purchase=book4.price)

    # purchase2 = repo.purchases.create(
    #     client=client2, employee=employee2, store=store1, total_amount=Decimal("33.50"))

    # purchase_detail2 = repo.purchase_details.create(
    #     purchase=purchase2, book=book2, quantity=1, price_at_purchase=book2.price)

    # purchase_detail2_1 = repo.purchase_details.create(
    #     purchase=purchase2, book=book5, quantity=1,
    #     price_at_purchase=book5.price)

    print("\n=== All books ===")
    for b in repo.books.get_all():
        print(b)

    print("\n=== Genres for each book ===")
    for book in repo.books.get_all():
        genres = repo.genres.get_genres_for_book(book)
        genre_names = [g.name for g in genres]
        print(f"{book.name}: {', '.join(genre_names)}")

    print("\n=== All authors ===")
    for a in repo.authors.get_all():
        print(a)

    print("\n=== Alive authors ===")
    for a in repo.authors.get_alive_authors():
        print(a)

    print("\n=== All publishers ===")
    for p in repo.publishers.get_all():
        print(p)

    print("\n=== All Clients ===")
    for c in repo.clients.get_all():
        print(c)

    print(f"\n Getting client with id={client1.client_id}")
    print(repo.clients.get_by_id(1))

    print("\n Finding client by phone")
    print(repo.clients.find_by_phone("0979812099"))

    print(f"\n=== All Employees in a store {store1.name}:===")
    employees_in_store = repo.employees.filter_by(store_id=store1.store_id)

    for e in employees_in_store:
        print(f"{e.first_name} {e.last_name} - {e.position.role}")

    # print("\n=== All purchases made by each client ===")
    # purchases = repo.purchases.get_by_client(client1.client_id)
    # for p in purchases:
    #     total = repo.purchase_details.get_total_sum_by_purchase(p.purchase_id)
    #     print(f"{client1} bought purchase #{p.purchase_id} for {total}")

    # purchases = repo.purchases.get_by_client(client2.client_id)
    # for p in purchases:
    #     total = repo.purchase_details.get_total_sum_by_purchase(p.purchase_id)
    #     print(f"{client2} bought purchase #{p.purchase_id} for {total}")


if __name__ == "__main__":
    main()
