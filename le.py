from sympy import *
import sys
import numpy as np
import matplotlib.pyplot as plt





while true:
    
    Calculus = input('미분할건가요?적분할건가요?아니면 멈추나요?(입력예:미분, 적분, 멈춰): ')
    if Calculus == '미분':
       fx = input('미분할 함수식을 입력하세요(입력예:x**2): ')
       var = input('그냥 미분에 기준이되는 변수를 입력하세요: ')

       var = Symbol(var)
       
       
       plot(fx, Derivative(fx, var).doit())
       
       print('result:f(x) = {0}'.format(Derivative(fx, var).doit()))
       
    elif Calculus == '적분':
        var = input('적분변수를 입력하세요: ')
        fx = input('피적분 함수를 입력하세요(입력예:x**2+1): ')
        a, b = input('적분 구간을 입력하세요(입력예:0 1): ').split()

        var = Symbol(var)

        intvl = [a, b]
        
        plot(fx, Integral(fx, var).doit())

        print('result1: {0}'.format(Integral(fx, var).doit()))
        print('result2: {0}'.format(Integral(fx, (var, intvl[0], intvl[1])).doit()))
        

    elif Calculus == '멈춰':
        print('작동을 정지합니다')
        break
    
    else:
        print('저가 물어본건 그게 아닌데요?')
        continue

    

        

