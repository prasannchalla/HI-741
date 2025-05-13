from datetime import datetime
from dateutil import parser  # Import for flexible date parsing

class Visit:
    def __init__(self, visit_id, visit_time, visit_department, race, gender, ethnicity, age, insurance, zipcode, chief_complaint, note_id, note_type):
        self.visit_id = visit_id
        self.visit_time = self.__parse_date(visit_time)  # Ensure visit_time is parsed as a datetime object
        self.visit_department = visit_department
        self.race = race
        self.gender = gender
        self.ethnicity = ethnicity
        self.age = age
        self.insurance = insurance
        self.zipcode = zipcode
        self.chief_complaint = chief_complaint
        self.note_id = note_id
        self.note_type = note_type
        self.note_text = ""  # Initialize note_text as an empty string. Can be set later.

    def __parse_date(self, date_str):
        """
        Parse the visit time into a datetime object using dateutil.parser to handle flexible date formats.
        """
        try:
            return parser.parse(date_str)  # Parse the date into a datetime object
        except ValueError:
            print(f"Invalid date format for {date_str}. Returning None.")
            return None  # Return None if the date is invalid

    def add_note_text(self, note_text):
        """
        Set the note text for this visit.
        """
        self.note_text = note_text

    def to_dict(self):
        """
        Convert the Visit object to a dictionary format for easy representation and storage.
        """
        return {
            "visit_id": self.visit_id,
            "visit_time": self.visit_time.isoformat() if self.visit_time else None,  # Ensure ISO format for datetime
            "visit_department": self.visit_department,
            "race": self.race,
            "gender": self.gender,
            "ethnicity": self.ethnicity,
            "age": self.age,
            "insurance": self.insurance,
            "zipcode": self.zipcode,
            "chief_complaint": self.chief_complaint,
            "note_id": self.note_id,
            "note_type": self.note_type,
            "note_text": self.note_text  # Include note_text in the dict
        }

    def __str__(self):
        """
        A string representation of the Visit object for easier debugging and display.
        """
        return f"Visit ID: {self.visit_id}, Time: {self.visit_time}, Department: {self.visit_department}, Patient Age: {self.age}, Chief Complaint: {self.chief_complaint}, Note: {self.note_text}"

# Example usage:
visit = Visit("V123", "2025-05-13 14:30", "Cardiology", "Asian", "Male", "Hispanic", 30, "Private", "12345", "Chest Pain", "N1", "General")
print(visit.to_dict())  # Print dictionary representation
visit.add_note_text("Patient has a history of hypertension.")  # Add a note text
print(visit)  # Print string representation
