# import the math module 
import math 
def runs_statistic_test(data,n,r,za):
  # r = number of runs
  #  Zr = cantidad de rayas menos el valor espeado de rachas entre variancia
  #   Zr = (r - ur)/or
  ur = (2*n-1)/3
  or2 = (16*n-29)/90
  oR = math.sqrt(or2)
  zr = (r-ur)/oR
  print("Miu = ",ur)
  print("Sigma = ",oR)
  print("Zscore = ",zr)
  #  se rechaza hipotesis nula cuando el absoluto |zr| > za/2 mas grande a el valor de prueba o de tabla que es fijo
  #  H0 lso numeros aparecen de manera aleatoria
  #  H1 los numeros no aparecen de manera aleatorias
  print("H0: Appearance of numbers is random")
  print("H1: Appearance of numbers is not random")
  if abs(zr) < abs(za):
    print("Since |",zr,"| < |",za,"| H0 is not rejected\nThe appearance of numbers is random")
  else:
    print("Since |",zr,"| > |",za,"| H1 is not rejected\nThe appearance of numbers is not random")
def runs_test(data):
  signs = []
  count = 0
  runs = 0
  oldSign = False
  for number in data:
      if not count == 0:
        sign = (number - oldNumber) > 0
        if sign == True:
          signs.append('+')
        else:
          signs.append('-')
        if not sign == oldSign:
          runs +=1
        oldSign = sign
      oldNumber = number
      count += 1
  print("Generated signs:")
  for sign in signs:
    print(sign,end = ' ')
  print("\nTotal: ",len(signs))
  print("Total Runs: ",runs)
  runs_statistic_test(data,len(signs),runs,1.96)
# Main function 
f = open("runs_data.txt", "r")
data = []
lines = f.readlines()
for line in lines:
    data.append(float(line.strip()))
runs_test(data)