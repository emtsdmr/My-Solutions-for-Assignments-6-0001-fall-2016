# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

current_saving=0
month=0
r=0.04

annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost=float(input("Enter the cost of your dream home: "))
semi_annual_raise=float(input("Enter the semiannual raise, as a decimal: "))
monthly_salary=annual_salary/12
down_payment=total_cost*0.25

while down_payment > current_saving:
    
    monthly_saving=monthly_salary*portion_saved
    current_saving=current_saving+(current_saving*r/12)+monthly_saving
    month +=1
    if month%6==0:
            monthly_salary=monthly_salary*(semi_annual_raise+1)
    #print(month,monthly_saving,current_saving)
print("Number of months: ",month)

