# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200765
# Date: 29/04/2021

tot = 0
students_count = progress_count = trailer_count = exclude_count = retriever_count =  x = 0 #all counters variables assigned 0
listvalue = [[120,0,0],[100,0,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]] 
def range_check():
    while True:
        try:
            range_arr = [0, 20, 40, 60, 80, 100, 120] #list is used to store the values to check if the marks are in range

            pass_mark = int(input('Enter your pass mark: '))
            if pass_mark not in range_arr:
                print('Value Out of Range')
            defer_mark = int(input('Enter your defer mark: '))
            if defer_mark not in range_arr:
                print('Value Out of Range')

            fail_mark = int(input('Enter your fail mark: '))
            if fail_mark not in range_arr:
                print('Value Out of Range')
        except ValueError:
            print('Integer Required')
            continue
        tot = pass_mark + defer_mark + fail_mark
        if tot != 120:
            print('Invalid total')
        return pass_mark, defer_mark, fail_mark


def output_mark(pass_mark,defer_mark,fail_mark):
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



def histogram(progress_count,trailer_count,exclude_count,retriever_count,students_count):
    print('-----------------------------------------------------------------')
    print('progress',progress_count,':', '*' * progress_count)
    print('progress(module trailer)',trailer_count,':', '*' * trailer_count)
    print('exclude',exclude_count,':','*' * exclude_count)
    print('donotprogress(module retriever)',retriever_count,':', '*' * retriever_count)
    print(str(students_count),'outcomes in total')
    print('-----------------------------------------------------------------')


def verticalhistogram(progress_count,trailer_count,exclude_count,retriever_count):
    blank='   '
    counter=progress_count+trailer_count+exclude_count+retriever_count
    print('Progress:',str(progress_count),'','Trailing:',str(trailer_count),'','Retriever:',str(retriever_count),'','Excluded:',str(exclude_count))
    for x in range(counter):
        if progress_count > 0:
            print(blank,'*', end='')
            progress_count = progress_count - 1
        else:
            print(blank,' ', end='')
        if trailer_count > 0:
            print(blank,blank,'*', end='')
            trailer_count = trailer_count - 1
        else:
            print(blank,blank,' ', end='')
        if retriever_count > 0:
            print(blank,blank,blank,'*', end='')
            retriever_count = retriever_count - 1
        else:
            print(blank,blank, blank,' ',end='')
        if exclude_count > 0:
            print(blank, blank, blank, '*')
            exclude_count = exclude_count - 1
        else:
            print(blank)

def check_data(listvalue):
    for i in listvalue: #using a loop to check all in the lists
        pass_mark = i[0]
        defer_mark = i[1]
        fail_mark = i[2]
        counter_outcomes(pass_mark,fail_mark) 

check_data(listvalue)
histogram(progress_count,trailer_count,exclude_count,retriever_count,students_count)