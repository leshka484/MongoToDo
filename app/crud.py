from typing import Annotated

from bson import ObjectId
from fastapi import Depends
from pymongo.collection import Collection

from app.database import get_note_collection

NoteCollectionDep = Annotated[Collection, Depends(get_note_collection)]


def serialize_note(note) -> dict:
    return {"id": str(note["_id"]), "title": note["title"], "content": note["content"]}


def get_notes(note_collection: NoteCollectionDep):
    return [serialize_note(note) for note in note_collection.find()]


def get_note(note_id: str, note_collection: NoteCollectionDep):
    note = note_collection.find_one({"_id": ObjectId(note_id)})
    return serialize_note(note) if note else None


def create_note(note_data, note_collection: NoteCollectionDep):
    note = note_collection.insert_one(note_data.model_dump())
    return get_note(note.inserted_id, note_collection)


def update_note(note_id: str, note_data, note_collection: NoteCollectionDep):
    note_collection.update_one(
        {"_id": ObjectId(note_id)}, {"$set": note_data.model_dump(exclude_unset=True)}
    )
    return get_note(note_id, note_collection)


def delete_note(note_id: str, note_collection: NoteCollectionDep):
    return note_collection.delete_one({"_id": ObjectId(note_id)}).deleted_count
