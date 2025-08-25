from app import db, User

# ---- Route paths ----
HOME_PATH = "/"
USERS_PATH = "/users"
ADD_PATH = "/add"
UPDATE_PATH = "/update/{id}"
DELETE_PATH = "/delete/{id}"
# ---------------------

def test_home_200(client):
    # Check homepage loads
    response = client.get(HOME_PATH)
    assert response.status_code == 200


def test_users_page_200(client):
    # Check users page loads and seeded users are shown
    response = client.get(USERS_PATH)
    assert response.status_code == 200
    page_text = response.get_data(as_text=True)
    assert "Alice Brown" in page_text
    assert "Bob Green" in page_text


def test_users_search_query(client):
    # Searching for "Alice" should hide "Bob"
    response = client.get(f"{USERS_PATH}?query=Alice")
    assert response.status_code == 200
    page_text = response.get_data(as_text=True)
    assert "Alice Brown" in page_text
    assert "Bob Green" not in page_text


def test_add_user_get_form(client):
    # Add user page should load
    response = client.get(ADD_PATH)
    assert response.status_code == 200


def test_add_user_post_success(client):
    # Adding a new user should increase total count
    start_count = db.session.query(User).count()

    new_user = {
        "name": "Charlie Black",
        "email": "charlie@example.com",
        "phone": "07000000000",
        "department": "HR",
    }
    response = client.post(ADD_PATH, data=new_user, follow_redirects=True)
    assert response.status_code == 200

    end_count = db.session.query(User).count()
    assert end_count == start_count + 1
    assert db.session.query(User).filter_by(email="charlie@example.com").first()


def test_add_user_duplicate_email_shows_error(client):
    # Trying to add Alice again should show error and not add a new user
    duplicate_user = {
        "name": "Alice Clone",
        "email": "alice@example.com",
        "phone": "07111111111",
        "department": "Sales",
    }
    response = client.post(ADD_PATH, data=duplicate_user, follow_redirects=True)

    total_users = db.session.query(User).count()
    assert total_users >= 2  # We know at least Alice and Bob exist

    page_text = response.get_data(as_text=True)
    assert "already exists" in page_text.lower() or "duplicate" in page_text.lower()


def test_add_user_duplicate_email_case_insensitive(client):
    # Emails with different case should be treated as duplicates
    assert db.session.query(User).filter_by(email="alice@example.com").first()

    duplicate_user = {
        "name": "Alice Case Test",
        "email": "ALICE@EXAMPLE.COM",  # uppercase version of alice@example.com
        "phone": "07111111111",
        "department": "Sales",
    }
    response = client.post(ADD_PATH, data=duplicate_user, follow_redirects=True)

    page_text = response.get_data(as_text=True)
    assert "already exists" in page_text.lower() or "duplicate" in page_text.lower()

    user_count = db.session.query(User).filter(User.email.ilike("alice@example.com")).count()
    assert user_count == 1  # Only original Alice exists


def test_update_user_get_form(client):
    # Update page for Alice should load
    alice = db.session.query(User).filter_by(email="alice@example.com").first()
    response = client.get(UPDATE_PATH.format(id=alice.id))
    assert response.status_code == 200


def test_update_user_post_success(client):
    # Updating Alice's details should save changes
    alice = db.session.query(User).filter_by(email="alice@example.com").first()
    updated_data = {
        "name": "Alice Updated",
        "email": "alice.updated@example.com",
        "phone": "07123456789",
        "department": "Sales",
    }
    response = client.post(UPDATE_PATH.format(id=alice.id), data=updated_data, follow_redirects=True)
    assert response.status_code == 200

    db.session.refresh(alice)
    assert alice.name == "Alice Updated"
    assert alice.email == "alice.updated@example.com"


def test_update_user_duplicate_email_blocked(client):
    # Alice can't change email to Bob's email
    bob = db.session.query(User).filter_by(email="bob@example.com").first()
    alice = db.session.query(User).filter(User.email.like("alice%")).first()

    duplicate_data = {
        "name": alice.name,
        "email": "bob@example.com",
        "phone": alice.phone,
        "department": alice.department,
    }
    response = client.post(UPDATE_PATH.format(id=alice.id), data=duplicate_data, follow_redirects=True)

    page_text = response.get_data(as_text=True)
    assert "already exists" in page_text.lower() or "duplicate" in page_text.lower()

    db.session.refresh(alice)
    assert alice.email != "bob@example.com"


def test_delete_user_flow(client):
    # Adding and then deleting a user should remove them
    temp_user = User(
        name="Temp User",
        email="temp@example.com",
        phone="07099999999",
        department="Temp"
    )
    db.session.add(temp_user)
    db.session.commit()

    user_id = temp_user.id
    response = client.post(DELETE_PATH.format(id=user_id), follow_redirects=True)
    assert response.status_code == 200
    assert db.session.get(User, user_id) is None