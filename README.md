# Incubyte Assessment

## Overview
This project is an automation testing suite designed to verify the signup and login functionality. It includes test scripts, dependencies, and test results.

## Features
- Automated testing for signup and login functionalities.
- Uses Python for scripting.
- Test results are stored in an Excel file (`test_results.xlsx`).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd IncubyteAssesment
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the test script with:
```bash
python test_signup_login.py
```
For your convenience, the `test_signup_login.py` file has been placed outside the `tests` directory so that you can easily run it.

## Environment Variables
Ensure that your `.env` file contains the necessary configuration for the tests to run properly. The `.env` file has been uploaded to the Git repository for your reference.

## Results
Test results are stored in `test_results.xlsx`.

## Contributing
If you would like to contribute, please submit a pull request with detailed explanations of your changes.
