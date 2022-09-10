import math
#Get data
file = open("runs_data.txt", "r")
content = file.readlines();

arr = []
for line in content:
    arr.append(float(line))
    
print("H0: los numeros generados son aleatorios.")
print("H1: los numeros generados no son aleatorios. \n")

#Get run
run = []
curr = arr[0]

for i in range(0, len(arr) - 1):
    next = arr[i + 1]
    if(curr < next):
        run.append("+")
    else:
        run.append("-")
    curr = next

print("Signos generados:")
print(run, "\n")

#Count runs
def contarRachas(data, size):
    count = 0
    tmp = []
    curr = data[0]

    tmp.append(curr)
    print("Rachas:")
    for i in range(0, size - 1):
        next = data[i + 1]
        if(curr == next):
            tmp.append(next)
            
        else:
            print(tmp)
            tmp = []
            tmp.append(next)
            count += 1
        curr = next
    if(len(tmp) > 0):
        print(tmp)
    print("\n")
    return count + 1
    
n = len(run)
racha = contarRachas(run, n)
print("Total de signos:", n)
print("Total de rachas:", racha, "\n")

#Get statistics
miu = (2*n - 1)/3
sigma = math.sqrt((16*n - 29)/90)
zscore = (racha - miu)/sigma

print("Miu:", round(miu, 4))
print("Sigma:", round(sigma, 5))
print("Zscore:", round(zscore, 4), "\n")

if(zscore > 1.96):
    print("Como", round(zscore, 4), "es mayor a 1.96, H0 es rechazada")
else:
    print("Como", round(zscore, 4), "es menor a 1.96, H0 no es rechazada")