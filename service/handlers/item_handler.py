from service.handlers import Handler
from domain.item import Item

class ItemHandler(Handler):
    def handle(self, request):
        if isinstance(request, Item):
            return f"Item {request.name} handled."
        else:
            return super().handle(request)
