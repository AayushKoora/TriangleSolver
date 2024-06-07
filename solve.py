import math


sideA = 42
sideB = 43
sideC = 41
# angleA =
# angleB =
# angleC =




def Solve():
    if sideA and sideB and sideC != 0:
        angleA = math.acos((sideA**2-sideB**2-sideC**2)/(-2*sideB*sideC))
        angleB = math.acos((sideB**2-sideA**2-sideC**2)/(-2*sideA*sideC))
        angleC = math.acos((sideC**2-sideB**2-sideA**2)/(-2*sideB*sideA))
    elif (sideA and sideB and angleA or angleB or angleC) :
    #elif (sideB and sideC and angleA or angleB or angleC):
    #elif (sideA and sideC and angleA or angleB or angleC):
      pass


#Solve()