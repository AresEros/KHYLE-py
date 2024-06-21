'''def say_hi(name):
    print ("hello " + name )
say_hi('mike')
say_hi('victor')
say_hi('khyle')'''

def raise_to_power (base_num, pow_num):
    reault = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))