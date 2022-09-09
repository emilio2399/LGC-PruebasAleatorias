
import numpy as np

def LGC (x,a,c,m,corridas):
    random_list = np.zeros(corridas)
    for i in range(corridas):
        subtotal= x*a+c
        pseudoaleatorio= subtotal % m
        random= pseudoaleatorio/ m
        random_list[i]=random
        x=pseudoaleatorio
    return random_list


x = LGC(6,32,3,80,10)
print(x)


