import Lab_2_exercise_3

print("Test_Lab2")

def test_get_user_input():
    inputnum = []
    usr_str = [1,2,3]
    test_arr = [1,2,3]

    inputnum = Lab_2_exercise_3.sort_temperature(Lab_2_exercise_3.get_user_input())

    assert (inputnum == test_arr)

def test_calc_average():
    avg = []
    usr_str = [2]
    test_arr = [2]

    avg = Lab_2_exercise_3.sort_temperature(Lab_2_exercise_3.calc_average_temperature())

    assert (avg == test_arr)

