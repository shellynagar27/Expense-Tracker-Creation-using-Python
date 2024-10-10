# Expense Management System

## Project Description

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.</br>
With help of this tracker you can add, update (delete or replace) your expenses on daily basis and can analyze them by category and month to get complete overview of the spending.

## Features
- Add/Update - for adding and updating data
- Analytics by Category - for visualizing spending by category
- Analytics by Month - for visualizing spending by month


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions
To use this project, you first need to install the required dependencies. Follow these steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```

## Contact
- Name- Shelly Nagar
- linkedin - https://www.linkedin.com/in/shellynagar/
- GitHub - shellynagar27