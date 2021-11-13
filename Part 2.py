# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200765
# Date: 29/04/2021

tot = 0


def range_check(): 
    while True:
        try:
            range_arr = [0, 20, 40, 60, 80, 100, 120] #list is used to store the values to check if the marks are in range 

            pass_mark = int(input('Enter your pass mark:'))
            if pass_mark not in range_arr:
                print('Value Out of Range')
            defer_mark = int(input('Enter your defer mark:'))
            if defer_mark not in range_arr:
                print('Value Out of Range')

            fail_mark = int(input('Enter your fail mark:'))
            if fail_mark not in range_arr:
                print('Value Out of Range')
        except ValueError:
            print('Integer Required')
            continue
        tot = pass_mark + defer_mark + fail_mark
        if tot != 120:
            print('invalid total')
        return pass_mark, defer_mark, fail_mark


def output_mark(pass_mark, fail_mark):
    if pass_mark == 120:
        print('progress')
    elif pass_mark == 100:
        print('progress(module trailer)')
    elif fail_mark in (80, 100, 120):
        print('exclude')
    else:
        print('do not progress(module retriever)')
#calling all the functions
range_check()
pass_mark, defer_mark, fail_mark = range_check()
output_mark(pass_mark, fail_mark)