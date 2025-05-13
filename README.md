# HI-741
## Clinical Data Warehouse UI Project

### Description

This program provides a simple and easy-to-use user interface (UI) for interacting with a clinical data warehouse. The UI allows users to perform various operations related to patient data, including adding, retrieving, and removing patient information, viewing clinical notes, counting patient visits, and generating key statistics. The program implements role-based access control, where users with different roles (e.g., admin, clinician, nurse, management) can perform different sets of tasks based on their assigned permissions.

### Requirements

To run this program, you need to have Python 3.x installed along with the required libraries. You can replicate the required environment using Anaconda or any other Python environment management tool.

#### Install Packages

1. **Create a virtual environment** (if you're using Anaconda):

   ```bash
   conda create --name clinical_data_warehouse python=3.8
   conda activate clinical_data_warehouse

## Install the required packages using the requirements.txt file:

This program uses the following packages:

tkinter (for the graphical user interface)

pandas (for data manipulation)

matplotlib (for generating statistics and visualizations)


You can view and install these packages by using the requirements.txt file provided.

## requirements.txt file:

```txt
tkinter
pandas
matplotlib
```
## How to Run the Program
To run the program, follow these steps:
### Clone the repository 

```bash
git clone <repository_url>
```
### Navigate to the project directory:

```bash
cd clinical_data_warehouse
```
### Run the main program:

```bash
python src/main.py
```

# Program Description
The Clinical Data Warehouse UI Project is a Python-based application designed to provide a user-friendly interface for managing clinical data in a healthcare setting. The main features of the program include the ability to:

Add, retrieve, and remove patient information: Users can manage patient data, including personal details and clinical information.

View and manage clinical notes: Clinicians can add, update, or view clinical notes associated with a patient’s visits.

Track patient visits: The program allows users to count and monitor patient visits over time.

Generate key statistics: The system offers statistical summaries and visualizations to help healthcare professionals analyze patient data.

Role-based access control: The program supports multiple user roles (e.g., admin, clinician, nurse, management), with each role having different permissions for performing specific tasks.

This program uses Tkinter for building the graphical user interface (GUI), Pandas for data manipulation, and Matplotlib for generating charts and statistical visualizations. It is structured to handle clinical data in an organized way, ensuring that users can interact with the system efficiently while maintaining privacy and security through role-based access.




