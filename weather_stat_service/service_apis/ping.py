from ticket_service.utils.resource import BaseResource


class Ping(BaseResource):
    def get(self):
        return {"Success:": True}
    get.authenticated = False