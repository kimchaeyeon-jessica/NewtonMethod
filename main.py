from sympy import Symbol, sympify, diff
x=Symbol('x') 
y=Symbol('y') 
tol=0.000000000001  #허용 오차 범위 
equa=sympify(input('해 찾으려는 방정식:')) 
dequa=diff(equa) 
x0=float(input('초기 추측값 x:')) 

for i in range(1, 100):
    f=equa.subs(x,x0)
    df=dequa.subs(x,x0)
    temp_x = x0 - f/df
    keunseo=abs(temp_x - x0)
    if keunseo < tol: 
        print(temp_x, i) 
        break 
    else: 
        x0=temp_x