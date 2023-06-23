import pytest
import random
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs, make_m2m=True)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs, make_m2m=True)
    return factory



@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/{courses[0].id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == courses[0].name
        
@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name
        
@pytest.mark.django_db
def test_get_courses_by_id(client, course_factory):
    courses = course_factory(_quantity=10)
    id = random.randint(1, 10)
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/?id={id}')
    assert response.status_code == 200
    data = response.json()
    for el in data:
        assert el['id'] == id
        
@pytest.mark.django_db
def test_get_courses_by_name(client, course_factory):
    courses = course_factory(_quantity=10)
    name = courses[random.randint(1, 10)].name
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/?name={name}')
    assert response.status_code == 200
    data = response.json()
    for el in data:
        assert el['name'] == name
        
@pytest.mark.django_db
def test_post_courses(client):
    name = 'Test_name_course'
    response = client.post('http://127.0.0.1:8000/api/v1/courses/', data={'name': name})
    assert response.status_code == 201
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/?name={name}')
    assert response.status_code == 200
    data = response.json()
    for el in data:
        assert el['name'] == name
        
@pytest.mark.django_db
def test_patch_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    id = random.randint(1, 10)
    name = 'Test_name_course'
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/{id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] != name
    response = client.patch(f'http://127.0.0.1:8000/api/v1/courses/{id}/', data={'name': name})
    assert response.status_code == 200
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/{id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == name
        
@pytest.mark.django_db
def test_delete_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    id = random.randint(1, 10)
    response = client.delete(f'http://127.0.0.1:8000/api/v1/courses/{id}/')
    assert response.status_code == 204
    response = client.get(f'http://127.0.0.1:8000/api/v1/courses/{id}/')
    assert response.status_code == 404