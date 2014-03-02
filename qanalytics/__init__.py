from flask import Flask
from .auth import login_manager
from .data import db
from .analytics.views import analytics
from .users.views import users

app = Flask(__name__)
app.config.from_object('config')

@app.context_processor
def provide_constants():
  return {"constants": {"QANALYTICSAPP": 2}}

db.init_app(app)

login_manager.init_app(app)

app.register_blueprint(analytics)
app.register_blueprint(users)