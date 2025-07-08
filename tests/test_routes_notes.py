from app.models import Note, NoteUpdate


def test_get_notes(client, test_note):
    response = client.get("/notes")
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "test"


def test_get_note(client, test_note):
    response = client.get(f"/notes/{test_note['id']}")
    received_json = response.json()
    assert  received_json["title"] == "test"
    assert received_json["content"] == "test"
    assert received_json["id"] == test_note["id"]

def test_add_note(client):
    note_data = Note(title = "test_add", content = "test_add")
    response = client.post("/notes", json=note_data.model_dump())
    
    received_json = response.json()
    
    assert received_json["title"] == "test_add"
    assert received_json["content"] == "test_add"
    
def test_edit_note(client, test_note):
    note_data = NoteUpdate(title = "test_edit", content = "test_edit")
    
    response = client.put(f"/notes/{test_note['id']}", json=note_data.model_dump())
    received_json = response.json()
    assert received_json["title"] == "test_edit"
    assert received_json["content"] == "test_edit"

def test_delete_note(client, test_note):
    response = client.delete(f"/notes/{test_note['id']}")
    assert response.status_code == 200
    deleted_count = response.json()
    assert deleted_count == 1
