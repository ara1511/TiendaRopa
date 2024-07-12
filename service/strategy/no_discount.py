from service.strategy.discount_strategy import DiscountStrategy

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price
