import django

django.setup()
from django.db import close_old_connections
from flask import Flask

close_old_connections()
from flask.ext import restful

app = Flask(__name__)

from weather_stat_service.service_apis.ping import Ping

api = restful.Api(app, prefix='/ticketservice/')

api.add_resource(Ping, 'ping/')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2004, debug=True)
