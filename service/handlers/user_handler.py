from service.handlers import Handler
from domain.user import User

class UserHandler(Handler):
    def handle(self, request):
        if isinstance(request, User):
            return f"User {request.name} handled."
        else:
            return super().handle(request)
