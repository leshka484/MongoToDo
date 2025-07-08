from typing import Annotated

from fastapi import APIRouter, Depends, Path

import app.crud as crud
from app.database import get_note_collection
from app.models import Note, NoteUpdate

router = APIRouter()


@router.get("/notes")
def read_notes(note_collection: Annotated[str, Depends(get_note_collection)]):
    return crud.get_notes(note_collection)


@router.get("/notes/{note_id}")
def read_note(
    note_id: Annotated[str, Path()],
    note_collection: Annotated[str, Depends(get_note_collection)],
):
    return crud.get_note(note_id=note_id, note_collection=note_collection)


@router.post("/notes")
def add_note(
    note: Note,
    note_collection: Annotated[str, Depends(get_note_collection)],
):
    return crud.create_note(note_data=note, note_collection=note_collection)


@router.put("/notes/{note_id}")
def edit_note(
    note_id: Annotated[str, Path()],
    note: NoteUpdate,
    note_collection: Annotated[str, Depends(get_note_collection)],
):
    return crud.update_note(
        note_id=note_id, note_data=note, note_collection=note_collection
    )


@router.delete("/notes/{note_id}")
def remove_note(
    note_id: Annotated[str, Path()],
    note_collection: Annotated[str, Depends(get_note_collection)],
):
    return crud.delete_note(note_id=note_id, note_collection=note_collection)
