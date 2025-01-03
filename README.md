# Techforing Django Project

## Local Installation

Follow these steps to set up the Django project on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/shakibuljoy/techforing.git
    cd techforing
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

### Additional Information

- To deactivate the virtual environment, simply run `deactivate`.
- For any issues, please refer to the Django documentation or contact the project maintainers.

Enjoy developing with Techforing!
