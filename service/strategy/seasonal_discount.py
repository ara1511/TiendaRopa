from service.strategy.discount_strategy import DiscountStrategy

class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9
