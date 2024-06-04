# 0x01. Basic authentication

This project is a RESTful API built with Flask that supports basic authentication. It includes the following key features:
- Custom authentication handling
- Basic user model
- Modular code structure for easy maintenance and scalability

## Project Structure

The project is structured as follows:

```
.
├── api
│   └── v1
│       ├── __init__.py
│       ├── app.py
│       ├── auth
│       │   ├── __init__.py
│       │   ├── auth.py
│       │   └── basic_auth.py
│       └── views
│           ├── __init__.py
│           └── index.py
├── models
│   ├── __init__.py
│   ├── base.py
│   └── user.py
├── main_0.py
├── main_1.py
├── main_2.py
├── main_3.py
├── main_4.py
├── main_5.py
├── main_6.py
└── README.md
```

## Requirements

- Python 3.6+
- Flask
- Pycodestyle 2.5

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask-api-basic-auth.git
    cd flask-api-basic-auth
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install Flask pycodestyle
    ```

## Running the Application

1. Set the environment variables:
    ```bash
    export FLASK_APP=api.v1.app
    export AUTH_TYPE=basic_auth  # or 'auth'
    export API_HOST=0.0.0.0
    export API_PORT=5000
    ```

2. Run the Flask application:
    ```bash
    flask run
    ```

3. The API will be accessible at `http://0.0.0.0:5000`.

## API Endpoints

- `GET /api/v1/status` - Returns the status of the API.
- `GET /api/v1/unauthorized` - Triggers a 401 error.
- `GET /api/v1/forbidden` - Triggers a 403 error.

## Authentication

The API supports basic authentication. To use basic authentication, include an `Authorization` header in your requests:

```
Authorization: Basic <base64-encoded-credentials>
```

## Code Style

This project adheres to the `pycodestyle` guidelines (version 2.5). To check the code style, run:

```bash
pycodestyle <path_to_your_code>
```

## Documentation

- **Modules**: Each module contains detailed docstrings explaining its purpose and usage.
- **Classes**: Each class includes documentation for its methods and attributes.

## Testing

Main test scripts (`main_0.py`, `main_1.py`, etc.) are included in the root directory. Run these scripts to ensure the functionality of various components.

## License

This project is licensed under the ALX curriculum.

## Author

Lerato Mgwangqa

## Acknowledgments

- Flask documentation
- Python community

```
