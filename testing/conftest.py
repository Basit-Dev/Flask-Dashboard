import os, sys, pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Force test mode
os.environ["FLASK_ENV"] = "test"

from app import app as flask_app, db, User

@pytest.fixture(scope="function")
def client():
    flask_app.config.update(TESTING=True)

    with flask_app.app_context():
        db.create_all()
        db.session.add_all([
            User(name="Alice Brown", email="alice@example.com", phone="07123456789", department="Sales"),
            User(name="Bob Green",   email="bob@example.com",   phone="07987654321", department="Support"),
        ])
        db.session.commit()

        with flask_app.test_client() as c:
            yield c

        db.session.remove()
        db.drop_all()