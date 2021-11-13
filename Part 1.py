# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20200765
# Date: 29/04/2021


#prompting the marks
pass_mark = int(input('enter your pass marks:')) #using int function to get to integer values
defer_mark = int(input('enter  your defer marks : '))
fail_mark = int(input('enter your fail marks :'))

if pass_mark == 120:
    print('progress')
elif pass_mark == 100:
    print('progress(module trailer)')
elif fail_mark in (80, 100, 120):
    print('exclude')
else:
    print('do not progress(module retriever)')
