'''Testing the Faker test data generation'''
# pylint: disable=comparison-with-callable, unused-import
from decimal import Decimal
import pytest
from faker import Faker
from app.calculator.arithematic import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    '''Generates test data to run on the tests'''
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    # Generate test data
    for _ in range(num_records):
        int1 = Decimal(fake.random_number(digits=2))
        int2 = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]
        # Ensure int2 is not zero for divide operation to prevent division by zero in expected calculation
        if operation_func == divide:
            int2 = Decimal('1') if int2 == Decimal('0') else int2
        try:
            if operation_func == divide and int2 == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(int1, int2)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield int1, int2, operation_name, expected

def pytest_addoption(parser):
    '''Allows the user to input --num_records=#'''
    parser.addoption("--num_records", action="store", default=9, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    '''Gathers the appropriate tests based on the parameters'''
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"int1", "int2", "operation", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation_name and operation for broad compatibility
        # Ensure 'operation_name' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("int1, int2, operation, expected", parameters)
