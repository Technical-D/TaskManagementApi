# TaskManagementApi

TaskManagementApi is a simple Django REST framework-based API for managing tasks. It allows users to create, read, update, and delete tasks with various statuses.
![image](https://github.com/Technical-D/TaskManagementApi/assets/101353705/7cae7f75-84d8-41a5-9185-2e48d1f67500)

## API Endpoints

### List and Create Tasks:

- `GET /tasks/`: Retrieve a list of all tasks.
- `POST /tasks/`: Create a new task.

### Retrieve, Update, and Delete Tasks:

- `GET /tasks/<task_id>/`: Retrieve details of a specific task.
- `PUT /tasks/<task_id>/`: Update details of a specific task.
- `DELETE /tasks/<task_id>/`: Delete a specific task.

## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.x
- Django 3.x
- Django REST framework

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Technical-D/TaskManagementApi.git
   ```

2. Navigate to the project directory:

    ```bash
    cd TaskManagementApi
    ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

 ### Usage
 1. Apply database migrations:

  ```bash
  python manage.py migrate
  ```

2. Create a superuser to access the Django admin interface:

  ```bash
  python manage.py createsuperuser
  ```
3. Run the development server:

  ```bash
  python manage.py runserver
  ```
4. Open your browser and visit http://127.0.0.1:8000/admin/ to log in with your superuser credentials and add tasks using the Django admin interface.

5. Use tools like cURL, Postman, or Python's requests library to make requests to the API endpoints listed above.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contributions
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

### Acknowledgments
This project was created as part of learning Django REST framework.
