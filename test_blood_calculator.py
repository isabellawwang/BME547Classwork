def test_check_HDL():
    from blood_calculator import check_HDL
    answer = check_HDL(85)
    expected = "Normal"
    assert answer == expected