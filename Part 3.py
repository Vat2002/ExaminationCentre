# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200765
# Date: 29/04/2021


tot = 0
students_count = progress_count = trailer_count = exclude_count = retriever_count  = 0 #all counters variables assigned 0

def range_check():
    while True:
        try:
            range_arr = [0, 20, 40, 60, 80, 100, 120]#list is used to store the values to check if the marks are in range

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


def counter_outcomes(pass_mark, fail_mark): #incrementing the counters if the condition is statisfied
    global progress_count, trailer_count, exclude_count, retriever_count, students_count


    if pass_mark == 120:
        print('progress')
        progress_count = progress_count + 1
    elif pass_mark == 100:
        print('progress(module trailer)')
        trailer_count = trailer_count + 1 
    elif fail_mark in (80, 100, 120):
        print('exclude')
        exclude_count = exclude_count + 1 
    else:
        print('do not progress(module retriever)')
        retriever_count = retriever_count + 1
    students_count = students_count + 1


def staff_check():
    letter = 'y'
    while letter != 'q' :
        while True:
             letter = input('enter letter q to quit and letter y to proceed:')
             if letter == 'y':
                pass_mark,defer_mark, fail_mark = range_check()
                counter_outcomes(pass_mark, fail_mark)
             else:
                print('quit')

                break



def histogram():
    print('-------------------------------------------------')
    print('progress',progress_count,':', '*' * progress_count)
    print('progress(module trailer)',trailer_count,':', '*' * trailer_count)
    print('exclude',exclude_count,':','*' * exclude_count)
    print('donotprogress(module retriever)',retriever_count,':', '*' * retriever_count)
    print(str(students_count),'outcomes in total')
    print('-------------------------------------------------')

#calling all the functions
pass_mark, defer_mark, fail_mark = range_check()
output_mark(pass_mark, fail_mark)
counter_outcomes(pass_mark, fail_mark)
staff_check()
histogram()