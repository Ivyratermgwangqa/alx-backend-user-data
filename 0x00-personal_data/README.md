# 0x00. Personal data

## Description
This project demonstrates how to handle sensitive personal data securely in a backend system. It includes logging with PII obfuscation, secure password handling, and database connectivity.

## Requirements
- Python 3.7
- Ubuntu 18.04 LTS
- MySQL server
- bcrypt package
- mysql-connector-python package

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-backend-user-data.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-backend-user-data/0x00-personal_data
   ```
3. Install required packages:
   ```bash
   pip install mysql-connector-python bcrypt
   ```

## Usage
1. Ensure your MySQL server is running and set up the required database and table as described in the project tasks.
2. Set the environment variables for database credentials:
   ```bash
   export PERSONAL_DATA_DB_USERNAME='your_username'
   export PERSONAL_DATA_DB_PASSWORD='your_password'
   export PERSONAL_DATA_DB_HOST='your_host'
   export PERSONAL_DATA_DB_NAME='your_database'
   ```
3. Run the main script to read and filter data:
   ```bash
   ./filtered_logger.py
   ```

## Functions
### `filtered_logger.py`
- `filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str`
- `RedactingFormatter`
- `get_logger() -> logging.Logger`
- `get_db() -> connection.MySQLConnection`
- `main()`

### `encrypt_password.py`
- `hash_password(password: str) -> bytes`
- `is_valid(hashed_password: bytes, password: str) -> bool`

## Authors
- Your Name <ivyratermgwangqa@gmail.com>
```
