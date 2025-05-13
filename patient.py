# patient.py

class Visit:
    def __init__(self, visit_id):
        self.visit_id = visit_id
        self.notes = []

    def add_note_text(self, note_text):
        """Add a note to the visit."""
        self.notes.append(note_text)

    def to_dict(self):
        """Convert the Visit to a dictionary."""
        return {
            "visit_id": self.visit_id,
            "notes": self.notes
        }

class Patient:
    def __init__(self, id):
        self.patient_id = id
        self.visits = {}

    def add_note_text_to_visit_id(self, visit_id, note_text):
        """Add a note to a visit with the given visit_id."""
        # Check if the visit_id exists in the dictionary
        visit = self.visits.get(visit_id)
        if visit:
            visit.add_note_text(note_text)
        else:
            print(f"Visit with ID {visit_id} not found.")

    def add_visit(self, visit_id):
        """Adds a new visit to the patient's visits."""
        # Check if the visit_id already exists
        if visit_id in self.visits:
            print(f"Visit with ID {visit_id} already exists.")
        else:
            # Create a new Visit object and add it
            self.visits[visit_id] = Visit(visit_id)

    def remove_visit(self, visit_id):
        """Remove a visit by visit_id."""
        if visit_id in self.visits:
            del self.visits[visit_id]
        else:
            print(f"Visit with ID {visit_id} not found.")

    def get_visit(self, visit_id):
        """Retrieve a specific visit by visit_id."""
        return self.visits.get(visit_id)

    def to_dict(self):
        """Returns a dictionary representation of the patient."""
        return {
            "patient_id": self.patient_id,
            "visits": [v.to_dict() for v in self.visits.values()]
        }
