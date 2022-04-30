def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average_temperature(num_list)
    print("The mean value of all temperature readings is : ", avg)
    calc_min_max_temperature(num_list)
    sort_temperature(num_list)
    print(sort_temperature(num_list))
    calc_median_temperature(num_list)


def display_main_menu():
    print("Enter some temperature readings seperated by commas (e.g. 5, 67, 32)");


def get_user_input():
    usr_str=input()
    str_list=usr_str.split(",")
    float_list=[]
    for usr_str in str_list:
        float_list.append(float(usr_str))
    print(float_list)
    return float_list


def calc_average_temperature(float_list):
    average=sum(float_list)/len(float_list)
    return float(average)


def calc_min_max_temperature(float_list):
    mintemperature = min(float_list)
    maxtemperture = max(float_list)
    print("Minimum temperature is : ",mintemperature)
    print("Maximum temperature is : ",maxtemperture)


def sort_temperature(float_list):
    float_list.sort()
    return float_list


def calc_median_temperature(float_list):
    temptotal=len(float_list)
    if temptotal%2==0:
        median1 = float_list[temptotal//2]
        median2 = float_list[temptotal//2-1]
        median=(median1+median2)/2
    else:
        median = float_list[temptotal//2]

    print("The median temperature is : " + str(median))


if __name__ == "__main__":
    main()