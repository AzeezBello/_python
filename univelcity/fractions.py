

def solve_fraction():
        
    # print('Enter the values for the first fraction')
    # frac1 = input()

    # print('Enter the values for the first fraction')
    # frac2 = input()
    
    print('Enter the values for the first numerator')
    num1 = int(input())

    print('Enter the values for  the first denominator')
    deno1 = int(input())
    


    print('Enter the values for the second numerator')
    num2 = int(input())

    print('Enter the values for the second denominator')
    deno2 = int(input())

    numerator1 = deno2 * num1
    numerator2 = deno1 * num2
    numerator = numerator1 + numerator2
    denominator = deno1 * deno2
    val = (f'{numerator} / {denominator}')

    return val

def breakdown(val):
    val = val.split('/')
    numerator = int(val[0])
    denominator = int(val[1])

    i = 0
    while i < 2:

        for j in range(2,10):

            if numerator % j != 0 and denominator % j != 0:
                pass
            elif((numerator % j == 0)) and (denominator % j == 0):
                numerator = numerator / j
                denominator = denominator / j

        i +=1
    print(f'Your answer is : {int(numerator)} / {int(denominator)}')

    
breakdown(solve_fraction())
