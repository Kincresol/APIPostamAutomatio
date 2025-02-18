import uuid

import pytest

from Utils.client_api import APIClient
from conftest import load_user_data


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_post_users(api_client, load_user_data):
    # user_data = {
    #     "name": "jashwanth",
    #     "username": "My Test User",
    #     "email": "test001@gmail.com"
    # }
    user_data = load_user_data["new_user"]
    unique_email  = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email

    response = api_client.post("users", user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'jashwanth'
    id = response.json()['id']
    responseget = api_client.get("users/10")
    print(responseget.json())
    assert responseget.json()['name'] == 'Clementina DuBuque'


def test_put_users(api_client):
    user_data = {
        "name": "jashwanth Naik",
        "username": "My Test User",
        "email": "test001@gmail.com"
    }
    response = api_client.put("users/1", user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'jashwanth Naik'


def test_delete_users(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200