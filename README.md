# Expense Management System

## Project Description

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.</br>
With help of this tracker you can add, update (delete or replace) your expenses on daily basis and can analyze them by category and month to get complete overview of the spending.

## Features
- Add/Update - for adding and updating data ![Adding-ezgif com-optimize](https://github.com/user-attachments/assets/78b78e59-daa7-40a0-ba4a-bbab1ab49119) ![Viewing-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/f60e34c7-4277-4855-bac3-1ecdf95812a3)


- Analytics by Category - for visualizing spending by category![AnalyticsbyCategory-MadewithClipchamp1-ezgif com-gif-to-mp4-converter](https://github.com/user-attachments/assets/e6b1e542-af28-4966-a239-dd279ef40bb8)
 
- Analytics by Month - for visualizing spending by month ![Screenshot 2024-10-10 021726](https://github.com/user-attachments/assets/20125b81-96e4-49a1-a580-984a24c38917)



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
   git clone https://github.com/shellynagar27/Expense-Tracker-Creation-using-Python.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Make changes to get_db_cursor function in db_helper.py file available in backend folder:**:   
   ```commandline
    host='Enter host name as per your systsm MySQL'
    password ='Enter MySQL password'
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
