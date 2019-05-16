# import time

# then = time.time()

def get_value(val,adder):
    val = str(val)
    adder = str(adder)
    if val[0]==val[1]==val[2] == adder[len(adder)-1]:
        resp = '{0} + {0} + {0} = {1}'.format(adder,val)
#        print(adder)
#        print(resp)
        return True
    else:
        return False


for i in range(100,999):
#     print(i)
        if get_value(i*3,i):
                print('Ans ===>',end='')
                print(i)
                break

# now = time.time()
# my_tot = (now - then)*1000
# print('{0:8f} ms'.format(my_tot))












# import string
# import time

# then = time.time()
# x = string.digits 

# def checkLastDigit(x):
#     if (x * 3) % 10 == x:
#         return (x * 3)//10

# def checkNext(rem, num, x):
#     if (num * 3 + rem) % 10 == x:
#         return (num * 3 + rem)//10

# def check1st(rem, num, x):
#     if rem + num * 3 == x:
#         return True
# def other():
#         for i in x:    
#                 if checkLastDigit(int(i)):
#                         store = i
#                         for a in x:
#                                 if checkNext(checkLastDigit(int(i)), int(a), int(i)):
#                                         store = a + store
#                                         for b in x:
#                                                 if check1st(checkNext(checkLastDigit(int(i)), int(a), int(i)), int(b), int(i)):
#                                                         store = b + store
#                                                         # print('''
#                                                         # \t{0} {1} {2}
#                                                         # +\t{0} {1} {2}
#                                                         # +\t{0} {1} {2}
#                                                         #  \t______
#                                                         #  \t{2} {2} {2}
#                                                         #  \t______
#                                                         # '''.format(store[0], store[1], store[2]))
# then = [0]
# def check(checks,func, i = 0):
#         checks -= 1
#         if i == 0:
#                 import time
#                 then[0] = time.time()

#         if checks == 0:
#                 import time
#                 now = time.time()
#                 tot = (now - then[0])*1000
#                 print (tot)
#                 return 
#         i += 1
#         func()
#         check(checks,func, i)


        
# # now = time.time()
# # tot = (now - then)*1000
# # print('ufode ==> {0:5f} ms'.format(tot))
# # print('attah ==> {0:8f} ms'.format(my_tot))

# (check(500,attah))
# (check(500,other))