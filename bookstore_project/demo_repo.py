import os
import django
from datetime import date
from decimal import Decimal

# Налаштування Django для standalone скрипта
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore_project.settings")  
django.setup()

from store.repositories.repo_manager import RepoManager

def main():
    repo = RepoManager()

    author1 = repo.authors.create(
        first_name="Agatha", last_name="Christie", pseudonym=None,
        birth_date=date(1890, 9, 15), death_date=date(1976, 1, 12), country="UK"
    )

    print("=== All authors ===")
    for a in repo.authors.get_all():
        print(a)

    print("\n=== Alive authors ===")
    for a in repo.authors.get_alive_authors():
        print(a)

    pub1 = repo.publishers.create(name="Penguin", email="contact@penguin.com", phone="1234567890", address="London, UK")
    pub2 = repo.publishers.create(name="Random House", email="info@randomhouse.com", phone="0987654321", address="New York, USA")

    print("\n=== All publishers ===")
    for p in repo.publishers.get_all():
        print(p)

    book1 = repo.books.create(name="Murder on the Orient Express", isbn="9780062693662", price=Decimal("15.00"), publisher=pub2)
    book2 = repo.books.create(name="New Age Book", isbn="1234567890123", price=Decimal("20.00"), publisher=pub2)

    print("\n=== All books ===")
    for b in repo.books.get_all():
        print(b)

if __name__ == "__main__":
    main()