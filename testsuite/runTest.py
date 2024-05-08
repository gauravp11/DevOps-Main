import pytest

# Define the order of test modules to run
test_modules = [
    "test_homepage.py",
    "test_partnerpage.py",
    "test_taskpage.py",
    "test_themespage.py",
    "test_userpage.py",
    "test_ticketpage.py"
]

if __name__ == "__main__":
    # Run the tests in the specified order
    for module in test_modules:
        pytest.main([f"../Tests/{module}"])
