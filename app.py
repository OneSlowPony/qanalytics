from qanalytics import app, db

if __name__=="__main__":
  app.debug = True
  
  # Because we did not initialize Flask-SQLAlchemy with an application
  # it will use `current_app` instead.  Since we are not in an application
  # context right now, we will instead pass in the configured application
  # into our `create_all` call.
  db.create_all(app=app)
  # Need the host as 0.0.0.0 and port as 3000 for Nitrous.io preview
  app.run(host='0.0.0.0', port=3000)