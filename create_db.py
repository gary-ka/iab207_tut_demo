from travel import db, create_app

app = create_app()
ctx = app.app_context()
ctx.push()
# add this line if ever need to reset the database
# db.drop_all() 
try:
    db.create_all()
except Exception as e:
    print("Error creating database tables:", str(e))