import pytest
import requests
from http import HTTPStatus
from app.models.User import User
from app.models.UserList import UserList

email = "george.bluth@reqres.in"
first_name = "George"
last_name = "Bluth"
avatar = "https://reqres.in/img/faces/1-image.jpg"

first_update_email = "janet.weaver@reqres.in"
first_update_first_name = "Janet"
first_update_last_name = "Weaver"
first_update_avatar = "https://reqres.in/img/faces/2-image.jpg"

second_update_email = "emma.wong@reqres.in"
second_update_first_name = "Emma"
second_update_last_name = "Wong"
second_update_avatar = "https://reqres.in/img/faces/3-image.jpg"


@pytest.fixture(scope="module")
def get_user_id():
    return {}


def test_user_create(app_url, get_user_id):
    body = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "avatar": avatar
    }
    response = requests.post(f"{app_url}/api/users/", json=body)
    assert response.status_code == HTTPStatus.CREATED
    response_body = response.json()
    User.model_validate(response_body)
    get_user_id['user_id'] = response_body['id']

    assert response_body['email'] == email, 'Invalid user email'
    assert response_body['first_name'] == first_name, 'Invalid first name'
    assert response_body['last_name'] == last_name, 'Invalid last name'
    assert response_body['avatar'] == avatar, 'Invalid user avatar'


def test_get_user_create(app_url, get_user_id):
    response = requests.get(f"{app_url}/api/users/{get_user_id.get('user_id')}")
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    User.model_validate(response_body)

    assert response_body['email'] == email, 'Invalid user email'
    assert response_body['first_name'] == first_name, 'Invalid first name'
    assert response_body['last_name'] == last_name, 'Invalid last name'
    assert response_body['avatar'] == avatar, 'Invalid user avatar'


def test_search_user_create_in_list(app_url, get_user_id):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    UserList.model_validate(response_body)

    for item in response_body:
        if item['id'] == get_user_id.get('user_id'):
            assert item['email'] == email, 'Invalid user email'
            assert item['first_name'] == first_name, 'Invalid first name'
            assert item['last_name'] == last_name, 'Invalid last name'
            assert item['avatar'] == avatar, 'Invalid user avatar'
            return True

    print('The created user was not found in the user list')
    assert False


def test_user_update_email(app_url, get_user_id):
    body = {
        "email": first_update_email
    }
    response = requests.patch(f"{app_url}/api/users/{get_user_id.get('user_id')}", json=body)
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    User.model_validate(response_body)
    assert response_body['email'] == first_update_email, 'Invalid user email'


def test_user_update_first_name(app_url, get_user_id):
    body = {
        "first_name": first_update_first_name
    }
    response = requests.patch(f"{app_url}/api/users/{get_user_id.get('user_id')}", json=body)
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    User.model_validate(response_body)
    assert response_body['first_name'] == first_update_first_name, 'Invalid user first name'


def test_user_update_last_name(app_url, get_user_id):
    body = {
        "last_name": first_update_last_name
    }
    response = requests.patch(f"{app_url}/api/users/{get_user_id.get('user_id')}", json=body)
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    User.model_validate(response_body)
    assert response_body['last_name'] == first_update_last_name, 'Invalid user last name'


def test_user_update_avatar(app_url, get_user_id):
    body = {
        "avatar": first_update_avatar
    }
    response = requests.patch(f"{app_url}/api/users/{get_user_id.get('user_id')}", json=body)
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    User.model_validate(response_body)
    assert response_body['avatar'] == first_update_avatar, 'Invalid user avatar'


def test_user_update_all(app_url, get_user_id):
    body = {
        "email": second_update_email,
        "first_name": second_update_first_name,
        "last_name": second_update_last_name,
        "avatar": second_update_avatar
    }
    response = requests.patch(f"{app_url}/api/users/{get_user_id.get('user_id')}", json=body)
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    User.model_validate(response_body)
    assert response_body['email'] == second_update_email, 'Invalid user email'
    assert response_body['first_name'] == second_update_first_name, 'Invalid user first name'
    assert response_body['last_name'] == second_update_last_name, 'Invalid user last name'
    assert response_body['avatar'] == second_update_avatar, 'Invalid user avatar'


def test_get_user_update(app_url, get_user_id):
    response = requests.get(f"{app_url}/api/users/{get_user_id.get('user_id')}")
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    User.model_validate(response_body)

    assert response_body['email'] == second_update_email, 'Invalid user email'
    assert response_body['first_name'] == second_update_first_name, 'Invalid first name'
    assert response_body['last_name'] == second_update_last_name, 'Invalid last name'
    assert response_body['avatar'] == second_update_avatar, 'Invalid user avatar'


def test_search_user_update_in_list(app_url, get_user_id):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    UserList.model_validate(response_body)

    for item in response_body:
        if item['id'] == get_user_id.get('user_id'):
            assert item['email'] == second_update_email, 'Invalid user email'
            assert item['first_name'] == second_update_first_name, 'Invalid first name'
            assert item['last_name'] == second_update_last_name, 'Invalid last name'
            assert item['avatar'] == second_update_avatar, 'Invalid user avatar'
            return True

    print('The updated user was not found in the user list')
    assert False


def test_user_delete(app_url, get_user_id):
    response = requests.delete(f"{app_url}/api/users/{get_user_id.get('user_id')}")
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    assert response_body['message'] == "User deleted"


def test_get_user_delete(app_url, get_user_id):
    response = requests.get(f"{app_url}/api/users/{get_user_id.get('user_id')}")
    assert response.status_code == HTTPStatus.NOT_FOUND
    response_body = response.json()

    assert response_body['detail'] == "User not found"


def test_search_user_delete_in_list(app_url, get_user_id):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    response_body = response.json()
    UserList.model_validate(response_body)
    if response_body:
        for item in response_body:
            if item['id'] != get_user_id.get('user_id'):
                return True

        print('Deleted user found in user list')
        assert False


def test_user_delete_not_found(app_url, get_user_id):
    response = requests.delete(f"{app_url}/api/users/{get_user_id.get('user_id')}")
    assert response.status_code == HTTPStatus.NOT_FOUND
    response_body = response.json()

    assert response_body['detail'] == "User not found"


def test_user_update_not_found(app_url, get_user_id):
    body = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "avatar": avatar
    }
    response = requests.patch(f"{app_url}/api/users/{get_user_id.get('user_id')}", json=body)
    assert response.status_code == HTTPStatus.NOT_FOUND
    response_body = response.json()

    assert response_body['detail'] == "User not found"


@pytest.mark.parametrize("user_id", [0, -1, "rty"])
def test_user_delete_invalid_user_id(app_url, user_id):
    response = requests.delete(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.parametrize("user_id", [0, -1, "rty"])
def test_user_update_invalid_user_id(app_url, user_id):
    body = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "avatar": avatar
    }
    response = requests.patch(f"{app_url}/api/users/{user_id}", json=body)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_user_create_invalid_body(app_url):
    body = {}
    response = requests.post(f"{app_url}/api/users/", json=body)
    assert response.status_code == HTTPStatus.BAD_REQUEST





