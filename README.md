# Django_Project_Manager
###This is a project management tool that allows teams to collaborate on projects built using Django REST API

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.12 or latest version (I have used 3.12.6 so recomended this version )
- Django 5.1.3
- pip 24.3.1
- Virtualenv (optional but recommended for managing dependencies)
- Postman (for API testing)

## Setting Up the Project Locally

### 1. Clone the repository

Clone the project repository to your local machine:

        git clone <repository-url> which is : https://github.com/Farzana201361-Nipa/Django_Project_Manager

Command to do that: 
        git clone <https://github.com/Farzana201361-Nipa/Django_Project_Manager>

Inside project directory: cd <project_manager>

As the repo already consist virtual environment you just need to activate it. 

    To activate:

        On Windows: venv\Scripts\activate

        On macOS/Linux: source myenv/bin/activate

Or you can also remove mine:

        rm -rf myenv 

And create your own: 

        python3 -m venv myenv 

### 1. Install all the dependencies inside virtual environment to avoid conflicts with other projects:
    pip install django
    Upgrade pip if necessary: pip install --upgrade pip 
    check if django is installed or not: python -m django --version
    **Try to run this: python manage.py runserver or python3 manage.py runserver
    python manage.py createsuperuser (If you want to see the changes in Django admin)
    python manage.py makemigrations(if needed)
    python manage.py migrate(if needed)
    pip install djangorestframework
    pip show djangorestframework
    pip install djangorestframework-simplejwt
    python manage.py runserver

###                               *****Explore the project*****




API Documentation
You can access the API documentation for the project via tools like Postman or Swagger. I have used Postman.
You can find the documentation inside the project repo.

User Endpoints:

    Register User (POST /api/users/register/)
    Login User (POST /api/users/login/)
    Get User Details (GET /api/users/{id}/)
    Update User (PUT/PATCH /api/users/{id}/)
    Delete User (DELETE /api/users/{id}/)
    
Projects Endpoints:

    List Projects (GET /api/projects/)
    Create Project (POST /api/projects/)
    Retrieve Project (GET /api/projects/{id}/)
    Update Project (PUT/PATCH /api/projects/{id}/)
    Delete Project (DELETE /api/projects/{id}/)

Task Endpoints:

    List Tasks (GET /api/projects/{project_id}/tasks/)
    Create Task (POST /api/projects/{project_id}/tasks/)
    Retrieve Task (GET /api/tasks/{id}/)
    Update Task (PUT/PATCH /api/tasks/{id}/)
    Delete Task (DELETE /api/tasks/{id}/)

Comment Endpoints:

    List Comments (GET /api/tasks/{task_id}/comments/)
    Create Comment (POST /api/tasks/{task_id}/comments/)
    Retrieve Comment (GET /api/comments/{id}/)
    Update Comment (PUT/PATCH /api/comments/{id}/)
    Delete Comment (DELETE /api/comments/{id}/)

For detailed API documentation, use Postman or Swagger.


                                            Contributing
If you want to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

To Do:
    Add more unit tests.
    Improve API documentation.
    Optimize database queries.