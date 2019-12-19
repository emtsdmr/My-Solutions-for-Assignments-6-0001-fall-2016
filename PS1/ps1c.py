# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

current_saving=0
month=0
r=0.04
low=0
high=10000
annual_salary=float(input("Enter your annual salary: "))
total_cost=1000000
semi_annual_raise=0.07

down_payment=total_cost*0.25
step=0
portion_saved=0
while abs(down_payment - current_saving)>=100:
    current_saving=0
    monthly_salary=annual_salary/12
    guess=(low+high)//2
    portion_saved=guess/10000
   
    for i in range(1,37):
        monthly_saving=monthly_salary*portion_saved
        current_saving=current_saving+(current_saving*r/12)+monthly_saving
        if i%6==0:
            monthly_salary=monthly_salary*(semi_annual_raise+1)
    if down_payment > current_saving:
        low=guess
    else:
        high=guess
    if portion_saved==0.9999 and down_payment > current_saving:
        print("It is not possible to pay the down payment in three years.")
        break
    step +=1

print("Best savings rate: ",portion_saved,current_saving)
print("Steps in BS: ",step)


