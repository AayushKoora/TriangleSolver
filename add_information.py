def AddInformation():
        sideA = input('Input Side A: ')
        sideB = input('Input Side B: ')
        sideC = input('Input Side C: ')
        angleA = input('Input Angle A: ')
        angleB = input('Input Angle B: ')
        angleC = input('Input Angle C: ')






        information = (sideA, sideB, sideC, angleA, angleB, angleC)          


        for x in information:
                if not x.isdigit():
                        print(f'Please Enter a Numerical Value for {x}')  
                continue
       
AddInformation()
