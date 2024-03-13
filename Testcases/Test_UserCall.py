from PetstoreAPI.UserCall import UserOperations
from Models.user import User


def test_add_user():
    """
    Test create user API
    """
    user_data = {
        "id": 12345,
        "username": "anu",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "phone": "1234567890"
    }
    user = User(**user_data)
    UserOperations.add_user(user)


def test_get_user():
    """
       Test get user API
    """
    UserOperations.get_user("anu")
