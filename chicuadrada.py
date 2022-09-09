import math
#Get data
file = open("chi_data.txt", "r")
content = file.readlines();

arr = []
for line in content:
    arr.append(round(float(line), 4))
    
arr.sort()

#Set intervals
intervals = []
curr = [0.0, 0.1]
total = float(len(arr))
chiCuadrada = 0
valorCritico = 16.91

def checkInterval(data, x, y):
    tmp = []
    for d in data:
        if d >= x and d < y:
            tmp.append(d)
    return len(tmp)

#Check frequency
for i in range(10):
    obs = float(checkInterval(arr, round(curr[0], 4), round(curr[1], 4)))
    exp = float(total/10.0)
    chi = round((math.pow((obs-exp), 2))/exp, 4)
    intervals.append({
        "interval": "["+str(round(curr[0], 4))+" - "+str(round(curr[1], 4))+")",
        "observed": obs,
        "expected": exp,
        "chiFormula": chi
    })
    curr[0] += 0.1
    curr[1] += 0.1
    chiCuadrada += chi

print("H0: los numeros generados no son diferentes de una distribucion uniforme.")
print("H1: los numeros generados son diferentes de una distribucion uniforme. \n")

for j in intervals:
    print(j)
print("")
print("Chi cuadrada: "+str(round(chiCuadrada, 4)))
print("Number of data: "+str(total)+"\n")

if(chiCuadrada > valorCritico):
    print("Como "+str(round(chiCuadrada, 4))+" > "+str(valorCritico)+", H0 es rechazada")
else:
    print("Como "+str(round(chiCuadrada, 4))+" < "+str(valorCritico)+", H0 es aceptada")
