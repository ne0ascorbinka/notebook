from typing import List
from datetime import datetime

class Notebook:
    def __init__(self, notes: List['Note']) -> None:
        self.notes = notes

    def search(self, filter: str) -> List['Note'] :
        matched = list()
        for note in self.notes:
            if note.match(filter): matched.append(note)
        return matched
    
    def new_note(self, memo, tags='') -> None:
        self.notes.append(Note(memo, tags))
    
    def search_by_id(self, note_id) -> 'Note':
        for note in self.notes:
            if note.note_id == note_id:
                return note
    
    def modify_memo(self, note_id: int, memo) -> None:
        self.search_by_id(note_id).memo = memo
    
    def modify_tags(self, note_id: int, tags: str) -> None:
        self.search_by_id(note_id).tags = tags

class Note:

    last_id = 0

    def __init__(self, memo: str, tags='') -> None:
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.now()
        self.note_id = Note.last_id
        Note.last_id += 1

    def match(self, search_filder: str) -> bool:
        return search_filder in self.memo or search_filder in self.tags

if __name__ == '__main__':
    ...
