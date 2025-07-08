import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient

from app.crud import get_note
from app.database import get_note_collection
from app.main import app

test_client = MongoClient("mongodb://localhost:27017/")
test_db = test_client["test_note_db"]
collection_test = test_db["notes"]


def override_get_note_collection():
    return collection_test


@pytest.fixture
def client():
    app.dependency_overrides[get_note_collection] = override_get_note_collection
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
def clear_collection():
    collection_test.delete_many({})
    yield
    collection_test.delete_many({})


@pytest.fixture()
def test_note():
    note = collection_test.insert_one({"title": "test", "content": "test"})
    return get_note(note.inserted_id, collection_test)
