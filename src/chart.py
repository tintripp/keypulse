import json
import os
import sys

from .note import Note

class Chart:
    @staticmethod
    def load(songname):
        filepath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "songs", songname, "chart.json")
        try:
            with open(filepath, "r") as file:
                chart_json = json.load(file)

        except Exception:
            print("idk bro it isnt working", filepath)
            return None
        
        # turn json into list of Note objects
        notes = []

        for note in chart_json['notes']:
            notes.append(Note(note["char"],note["x"],note["y"],note["time"],note["lifespan"]))

        return notes
    
    @staticmethod
    def print(notes):
        for note in notes:
            print(note.x, note.y, note.char, note.time, note.lifespan)