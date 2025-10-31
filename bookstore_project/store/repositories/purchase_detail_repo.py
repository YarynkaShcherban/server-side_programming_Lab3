from store.repositories.base_repo import BaseRepo
from store.models import PurchaseDetail


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
