import sys
print(sys.executable)

from user import User 
from datetime import datetime

class Admin(User):
    def __init__(self, role, patient_record_manager):
        super().__init__(role, patient_record_manager)

    def do_action(self):
        """
        Admin action: Count the number of patient visits for a specific date.
        Tries to parse common date formats.
        """
        print(f"Current role: {self._role}")
        visit_date_input = input("Enter visit date (e.g., '2024-05-12', '12/05/2024', 'May 12, 2024'): ")

        visit_date = None
        possible_formats = [
            "%Y-%m-%d",
            "%d-%m-%Y",
            "%d/%m/%Y",
            "%m/%d/%Y",
            "%B %d, %Y",   
            "%d %B %Y",   
            "%d %b %Y"     
        ]

        for fmt in possible_formats:
            try:
                visit_date = datetime.strptime(visit_date_input, fmt).date()
                break
            except ValueError:
                continue

        if not visit_date:
            print("Invalid date! Please enter a valid date in one of the supported formats.")
            return

        # Get the count of visits for the given date
        count = self._patient_record_manager.get_count_of_patient_visits_for_date(str(visit_date))

        # Show the result
        if count is not None:
            print(f"Total number of visits on {visit_date}: {count}")
        else:
            print(f"No visits recorded on {visit_date}.")
