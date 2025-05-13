import csv

class Validator:
    def __init__(self, filename):
        self.__credentials = {}
        self.__user_roles = {}
        self.__load_credentials_data(filename)

    def validate_credentials(self, username, password):
        """
        Validates the given username and password.
        Returns True if valid, otherwise False.
        """
        # Check if username exists and password matches
        return self.__credentials.get(username) == password

    def get_user_role(self, username):
        """
        Retrieves the role of the user based on the provided username.
        Returns the role, or None if not found.
        """
        return self.__user_roles.get(username)

    def __load_credentials_data(self, filename):
        """
        Loads the credentials data from a CSV file into the internal dictionaries.
        """
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                data = csv.DictReader(csvfile)
                
                # Check that the necessary columns exist in the CSV
                for row in data:
                    username = row.get('username')
                    password = row.get('password')
                    role = row.get('role')
                    
                    # Only add valid data to the dictionaries
                    if username and password and role:
                        self.__credentials[username] = password
                        self.__user_roles[username] = role
                    else:
                        print(f"Warning: Invalid row in CSV (missing username, password, or role): {row}")

        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except csv.Error as e:
            print(f"Error: There was an issue reading the CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
