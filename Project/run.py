from app import app, db
from app.routes import app as app1

# Create the Flask application context
with app.app_context():
    # Create the database tables
    db.create_all()

if __name__ == '__main__':
    app1.run(debug=True)
