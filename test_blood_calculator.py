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


@pytest.mark.parametrize("test_value, expected_output",
                         [(100, "Normal"),
                          (140, "Borderline High"),
                          (189, "High"),
                          (200, "Very High")])
def test_check_LDL(test_value, expected_output):
    from blood_calculator import check_LDL
    answer = check_LDL(test_value)
    expected = expected_output
    assert answer == expected


@pytest.mark.parametrize("test_value, expected_output",
                         [(199, "Normal"),
                          (239, "Borderline High"),
                          (240, "High")])
def test_check_total_chol(test_value, expected_output):
    from blood_calculator import check_total_chol
    answer = check_total_chol(test_value)
    expected = expected_output
    assert answer == expected
