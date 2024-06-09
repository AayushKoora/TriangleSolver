import math

def LawCosines(side1, side2, angle1):
    return math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(math.radians(angle1)))

def InvLawCosines(side1, side2, side3):
    # Calculate the expression inside acos
    expression = (side1**2 + side2**2 - side3**2) / (2 * side1 * side2)
    if expression < -1 or expression > 1:
        raise ValueError("Invalid input: cosine value is out of range")
    return math.acos(expression)

def LawSines(side1, angle1, angle2):
    return (math.sin(math.radians(angle2)) * side1) / math.sin(math.radians(angle1))

def main():
    sideA = float(input('Side A: '))
    sideB = float(input('Side B: '))
    sideC = float(input('Side C: '))
    angleA = float(input('Angle A: '))
    angleB = float(input('Angle B: '))
    angleC = float(input('Angle C: '))

    information = {'sideA': sideA, 'sideB': sideB, 'sideC': sideC, 'angleA': angleA, 'angleB': angleB, 'angleC': angleC}

    [print(f'Please Enter a Numerical Value for {key}') for key, value in information.items() if not isinstance(value, (int, float))]

    sides = sum(value != 0 for key, value in information.items() if 'side' in key)
    angles = sum(value != 0 for key, value in information.items() if 'angle' in key)

    if sides == 3:  # All sides are given (SSS)
        angleA = math.degrees(InvLawCosines(sideB, sideC, sideA))
        angleB = math.degrees(InvLawCosines(sideA, sideC, sideB))
        angleC = 180 - (angleA + angleB)

    elif sides == 2 and angles == 1:  # Two sides and one angle (SAS)
        if angleA and sideA and sideB:
            sideC = LawCosines(sideA, sideB, angleA)
            angleB = math.degrees(InvLawCosines(sideA, sideC, sideB))
            angleC = 180 - (angleA + angleB)
        elif angleB and sideA and sideB:
            sideC = LawCosines(sideA, sideB, angleB)
            angleA = math.degrees(InvLawCosines(sideB, sideC, sideA))
            angleC = 180 - (angleA + angleB)
        elif angleC and sideA and sideB:
            sideC = LawCosines(sideA, sideB, angleC)
            angleA = math.degrees(InvLawCosines(sideB, sideC, sideA))
            angleB = 180 - (angleA + angleC)

    elif sides == 1 and angles == 2:  # Two angles and one side (ASA or AAS)
        if angleA and angleB and sideA:
            angleC = 180 - (angleA + angleB)
            sideB = LawSines(sideA, angleA, angleB)
            sideC = LawSines(sideA, angleA, angleC)
        elif angleA and angleB and sideB:
            angleC = 180 - (angleA + angleB)
            sideA = LawSines(sideB, angleB, angleA)
            sideC = LawSines(sideB, angleB, angleC)
        elif angleA and angleB and sideC:
            angleC = 180 - (angleA + angleB)
            sideA = LawSines(sideC, angleC, angleA)
            sideB = LawSines(sideC, angleC, angleB)

    else:
        print('Insufficient Information')

    # Round the results to 2 decimal places
    sideA = round(sideA, 2)
    sideB = round(sideB, 2)
    sideC = round(sideC, 2)
    angleA = round(angleA, 2)
    angleB = round(angleB, 2)
    angleC = round(angleC, 2)

    print(f'Side A: {sideA}, Side B: {sideB}, Side C: {sideC}, Angle A: {angleA}, Angle B: {angleB}, Angle C: {angleC}')

main()
