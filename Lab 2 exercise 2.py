def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()

def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")

def get_user_input():
    usr_str=input()
    str_list=usr_str.split(",")
    float_list=[]
    for num in str_list:
        float_list.append(float(num))
    print(float_list)

if __name__== "__main__":
    main()