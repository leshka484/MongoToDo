from app.crud import create_note, delete_note, get_note, get_notes, update_note
from app.models import Note, NoteUpdate
from tests.conftest import collection_test


def test_create_note():
    note_data = Note(title="test", content="test")
    note = create_note(note_data, collection_test)

    assert note is not None
    assert note["title"] == "test"
    assert note["content"] == "test"
    assert "id" in note


def test_get_note(test_note):
    note = get_note(test_note["id"], collection_test)
    assert note is not None
    assert note["title"] == "test"
    assert note["content"] == "test"


def test_get_notes():
    collection_test.insert_many(
        [
            {"title": "Note 1", "content": "Content 1"},
            {"title": "Note 2", "content": "Content 2"},
        ]
    )
    notes = get_notes(collection_test)
    assert len(notes) == 2
    titles = {note["title"] for note in notes}
    assert titles == {"Note 1", "Note 2"}
    contents = {note["content"] for note in notes}
    assert contents == {"Content 1", "Content 2"}


def test_update_note(test_note):
    note_data = NoteUpdate(title="updated", content="updated")
    updated = update_note(test_note["id"], note_data, collection_test)
    assert updated is not None
    assert updated["id"] == test_note["id"]
    assert updated["title"] == "updated"
    assert updated["content"] == "updated"


def test_delete_note(test_note):
    deleted_count = delete_note(test_note["id"], collection_test)
    assert deleted_count == 1

    deleted_note = get_note(test_note["id"], collection_test)
    assert deleted_note is None
