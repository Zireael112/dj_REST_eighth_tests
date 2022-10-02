import pytest
from tests.conftest import courses_factory, client, students_factory


@pytest.mark.django_db
def test_get_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    url = f'http://127.0.0.1:8000/api/v1/courses/{course[0].id}/'
    response = client.get(url)
    assert response.data['name'] == course[0].name


@pytest.mark.django_db
def test_get_list_courses(client, courses_factory):
    courses = courses_factory(_quantity=10)
    url = f'http://127.0.0.1:8000/api/v1/courses/'
    response = client.get(url)
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_filter_id(client, courses_factory):
    courses = courses_factory(_quantity=10)
    url = f'http://127.0.0.1:8000/api/v1/courses/'
    response = client.get(url, {'id': courses[0].id})
    assert response.data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_filter_name(client, courses_factory):
    courses = courses_factory(_quantity=10)
    url = f'http://127.0.0.1:8000/api/v1/courses/'
    response = client.get(url, {'name': courses[0].name})
    assert response.data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    url = f'http://127.0.0.1:8000/api/v1/courses/'
    response = client.post(url, data={'name': 'Python_course', })
    assert response.data['name'] == 'Python_course'


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    data = {'name': 'Python'}
    url = f'http://127.0.0.1:8000/api/v1/courses/{course[0].id}/'
    response = client.patch(url, data=data)
    assert response.data['name'] == data['name']


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    url = f'http://127.0.0.1:8000/api/v1/courses/{course[0].id}/'
    response = client.delete(url)
    assert response.status_code == 204


# def test_example():
#     assert False, "Just test example"
