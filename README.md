# Flask REST API Demo

This project demonstrates a simple REST API built with Python's Flask framework. The API performs CRUD (Create, Read, Update, Delete) operations on student data, which can be tested locally. It can also be deployed to Azure App Service for cloud hosting if needed.

## Features

- Retrieve all students
- Retrieve a specific student by ID
- Create a new student (ID is automatically generated)
- Update an existing student
- Delete a student

## Prerequisites

Before you can run or deploy this app, you need to have the following installed:

- Python 3.x
- pip (Python package manager)
- Flask (`pip install Flask`)
- gunicorn (`pip install gunicorn`) – optional for production deployment

## Project Structure

- `app.py`: Main Flask application 
- `requirements.txt`: List of Python dependencies 
- `test-api.http`: File to test the REST API using the REST Client extension in Visual Studio Code
- `README.md`: Documentation

## Running Locally

To run the Flask API on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/ngugi-james/RESTfulAPI.git
   
2. Navigate to the project directory:
   ```bash
   cd RESTfulAPI
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python app.py
5. The API will be running at http://127.0.0.1:5000
6. Use **test-api.http** to test the REST API using the REST Client extension in Visual Studio Code.
