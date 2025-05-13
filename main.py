from patientRecordManager import PatientRecordManager
from validator import Validator
from user import User
from admin import Admin
from manager import Manager
from healthProfessional import HealthProfessional
import argparse

# File names for CSVs (Corrected to your project filenames)
USER_CREDENTIALS_FILE_NAME = "Credentials.csv"
PATIENT_NOTES_FILE_NAME = "Notes.csv"
PATIENT_DATA_FILE_NAME = "Patient_data.csv"

# Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Patient Record System")
    parser.add_argument('-username', type=str, required=True, help="Username of the user")
    parser.add_argument('-password', type=str, required=True, help="Password of the user")
    return parser.parse_args()

# Main entry point
def main():
    # Parse username and password from command-line arguments
    args = parse_args()
    print(f"Attempting to login with username: {args.username} and password: {args.password}")

    # Validate credentials
    credential_validator = Validator(USER_CREDENTIALS_FILE_NAME)

    if credential_validator.validate_credentials(args.username, args.password):
        # Fetch the role for the user
        cur_role = credential_validator.get_user_role(args.username)
        print(f"User validation successful! Role: {cur_role}")

        # Create a PatientRecordManager instance
        patient_record_manager = PatientRecordManager(PATIENT_DATA_FILE_NAME, PATIENT_NOTES_FILE_NAME)

        # Determine which type of user based on their role
        if cur_role == "admin":
            cur_user = Admin(cur_role, patient_record_manager)
        elif cur_role in ["clinician", "nurse"]:
            cur_user = HealthProfessional(cur_role, patient_record_manager)
        elif cur_role == "management":
            cur_user = Manager(cur_role, patient_record_manager)
        else:
            print(f"Invalid role type: {cur_role}")
            return

        # Perform the action associated with the role
        cur_user.do_action()

    else:
        print("Invalid Username or Password!")

if __name__ == "__main__":
    main()
