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







