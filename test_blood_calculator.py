import pytest

@pytest.mark.parametrize("test_value, expected_output",
    [(85, "Normal"),
        (40, "Borderline Low"),
        (39, "Low")])
def test_check_HDL(test_value, expected_output):
    from blood_calculator import check_HDL
    answer = check_HDL(test_value)
    expected = expected_output
    assert answer == expected

# Homework: do something similar for the check_LDL function and the check_total function!

# Starting with the next assignment, all code should follow PEP8 styleguide and have pytest