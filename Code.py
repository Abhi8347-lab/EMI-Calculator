p=float(input('Enter the principle or loan amount:$'))
if not p>0:
    print('Amount not valid')
else:
    print(f'the amount is ${p}')
r=float(input('Enter the annual rate of interest:%'))
if not r>0:
    print('interest not valid')
else:
    print(f'the interest is %{r}')
n=float(input('Enter number of monthly payments:'))
if not n>0:
    print('time of payment not valid')
else:
    print(f'the umber of monthly payments are {n}')
R=r/(12*100)
EMI=(p*R*(1+R)**n)/((1+R)**n-1)
u=round((p*R*(1+R)**n)/((1+R)**n-1))
print(f'The EMI you have to pay is ${EMI} approximately= {u} ')
total=EMI*n
o=round(EMI*n)
print(f'Total payment=${total} approximately= {o}')
ti=total-p
t=round(total-p)
print(f'Total interest = {ti} approximately= {t}')
