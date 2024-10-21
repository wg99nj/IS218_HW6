# tests/conftest.py

import pytest
from faker import Faker # type: ignore

# Initialize Faker
fake = Faker()

def pytest_addoption(parser):
    """Add a command line option to pytest"""
    parser.addoption("--num_records", action="store", default=10, type=int, 
                     help="Number of random test records to generate")

@pytest.fixture(scope='session')
def num_records(request):
    """Fixture to get the number of records from the command line"""
    return request.config.getoption("--num_records")

@pytest.fixture
def fake_data():
    """Fixture that generates fake data using Faker"""
    a = fake.random_number(digits=2)   # Generate a random 2-digit number
    b = fake.random_number(digits=2)   # Generate another random 2-digit number
    return a, b

@pytest.fixture
def generate_test_cases(num_records):
    """Generate a list of test cases based on the --num_records argument"""
    test_cases = []
    for _ in range(num_records):
        a = fake.random_number(digits=2)  # Random 2-digit number
        b = fake.random_number(digits=2)  # Random 2-digit number
        test_cases.append((a, b))
    return test_cases
