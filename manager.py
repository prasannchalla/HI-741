import pandas as pd
import matplotlib.pyplot as plt
from user import User
from datetime import datetime

class Manager(User):
    def __init__(self, role, patient_record_manager):
        super().__init__(role, patient_record_manager)

    def do_action(self):
        print(f"Current role: {self._role}")
        self.__do_generate_stat_reports_action()

    def __do_generate_stat_reports_action(self):
        df = pd.read_csv(self._patient_record_manager.patient_file_name, parse_dates=['Visit_time'])

        # Ensure Visit_time is in datetime format
        df['Visit_time'] = pd.to_datetime(df['Visit_time'], errors='coerce')

        # Extract month for grouping
        df['Visit_month'] = df['Visit_time'].dt.to_period('M').astype(str)

        # Create age group labels and bins
        bins = [0, 18, 35, 50, 65, 100]
        labels = ['0-18', '19-35', '36-50', '51-65', '66+']
        df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

        # Plotting trends for gender, race, ethnicity, and age group
        self.__plot_graph(df, 'Gender', 'Gender')
        self.__plot_graph(df, 'Race', 'Race')
        self.__plot_graph(df, 'Ethnicity', 'Ethnicity')
        self.__plot_graph(df, 'age_group', 'Age Group')

    # Function to plot graph
    def __plot_graph(self, df, group_by_col, title):
        trend = df.groupby(['Visit_month', group_by_col])['Patient_ID'].nunique().unstack().fillna(0)
        trend.plot(kind='line', marker='o', figsize=(12, 6))
        plt.title(f"Temporal Trend of Patient Visits by {title}")
        plt.xlabel("Month")
        plt.ylabel("Number of Unique Patients")
        plt.xticks(rotation=45)
        plt.legend(title=title)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    # View note for a specific patient on a given visit date
    def view_note_for_patient(self, patient_id, visit_date):
        # Load dataset
        df = pd.read_csv(self._patient_record_manager.patient_file_name, parse_dates=['Visit_time'])
        
        try:
            visit_date = datetime.strptime(visit_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        
        patient_data = df[(df['Patient_ID'] == patient_id) & (df['Visit_time'].dt.date == visit_date)]
        
        if patient_data.empty:
            print(f"No note found for Patient {patient_id} on {visit_date}.")
        else:
            # Print the notes or further data as required
            print(f"Found notes for Patient {patient_id} on {visit_date}:")
            print(patient_data[['Visit_time', 'Visit_notes']])

    # Count visits for a given date
    def count_visits_for_date(self, visit_date):
        # Load dataset
        df = pd.read_csv(self._patient_record_manager.patient_file_name, parse_dates=['Visit_time'])

        try:
            visit_date = datetime.strptime(visit_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        # Filter dataset for the given date
        visits_on_date = df[df['Visit_time'].dt.date == visit_date]
        
        total_visits = visits_on_date.shape[0]
        print(f"Total number of visits on {visit_date}: {total_visits}")
