from user import User
from visit import Visit
from datetime import datetime
from validator import Validator  

class HealthProfessional(User):
    def __init__(self, role, patient_record_manager):
        super().__init__(role, patient_record_manager)

    def do_action(self):
        print(f"Current role: {self._role}")

        actions = {
            "Add_patient": self.__do_add_patient_action,
            "Remove_patient": self.__do_remove_patient_action,
            "Retrieve_patient": self.__do_retrieve_patient_action,
            "Count_visits": self.__do_count_visits_action,
            "View_note": self.__do_view_note_action,
            "Stop": self.__stop_action
        }

        while True:
            action = input("Please enter desired action (Add_patient, Remove_patient, Retrieve_patient, Count_visits, View_note, Stop): ")

            if action in actions:
                actions[action]()
            else:
                print("Invalid action, try again!")

    def __stop_action(self):
        print("Stopping the action loop.")
        exit()

    # Add new patient and record visit details
    def __do_add_patient_action(self):
        patient_id = input("Please enter Patient_Id: ")
        patient_data = input("Please enter additional patient data (gender, race, ethnicity, age, etc.): ")
        if self._patient_record_manager.add_patient(patient_id, patient_data):
            print(f"Patient added with patient id: {patient_id}")
        else:
            print("Failed to add patient. Please check the input data.")

    # Remove a patient from records
    def __do_remove_patient_action(self):
        patient_id = input("Please enter Patient_Id: ")
        if self._patient_record_manager.remove_patient(patient_id):
            print(f"Patient record for patient id: {patient_id} removed successfully")
        else:
            print(f"No records exist for patient id: {patient_id}")

    # Retrieve specific patient attribute
    def __do_retrieve_patient_action(self):
        patient_id = input("Please enter Patient_Id: ")
        patient_data = self._patient_record_manager.get_patient(patient_id)
        
        if not patient_data:
            print(f"No records exist for patient id: {patient_id}")
        else:
            attribute = input("Please enter required data (gender, race, ethnicity, zipcode, insurance, age, visit_time, visit_department, chief_complaint): ")
            attribute_value = self._patient_record_manager.get_patient_data_for_attribute(patient_id, attribute)
            if attribute_value is not None:
                print(f"Requested data for {attribute}: {attribute_value}")
            else:
                print(f"No data found for the attribute: {attribute}")

    # Count visits on a given date
    def __do_count_visits_action(self):
        visit_time = input("Enter visit date (YYYY-MM-DD): ")
        try:
            visit_date = datetime.strptime(visit_time, "%Y-%m-%d").date()
            count = self._patient_record_manager.get_count_of_patient_visits_for_date(visit_date)
            print(f"Total number of visits on {visit_date}: {count}")
        except ValueError:
            print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")

    # View clinical note on a given date
    def __do_view_note_action(self):
        patient_id = input("Please enter Patient_Id: ")
        patient_data = self._patient_record_manager.get_patient(patient_id)
        
        if not patient_data:
            print(f"No records exist for patient id: {patient_id}")
        else:
            visit_time = input("Enter visit date (YYYY-MM-DD): ")
            try:
                visit_date = datetime.strptime(visit_time, "%Y-%m-%d").date()
                cur_note = self._patient_record_manager.get_note_of_patient_visit_for_date(patient_id, visit_date)
                if cur_note:
                    print(f"Requested note: {cur_note}")
                else:
                    print(f"No note found for given date: {visit_date}")
            except ValueError:
                print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")
