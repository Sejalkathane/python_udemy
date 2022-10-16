stock_prices=[('APPLE',200),('GOOGLE',400),('MICROSOFT',100)]
for item in stock_prices:
    print(item)

print('...........................')

for ticker,prices in stock_prices:
    print(ticker)

print('...........................')

for ticker,prices in stock_prices:
    print(prices+(0.1*prices))


work_hours=[('sejal',100),('prasanna',300),('gitainjali',900)]

def employee_check(work_hours):
    current_max=0
    employee_of_month=''

    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_of_month=employee
        else:
            pass

    return(employee_of_month,current_max)

print('...........................')
# print(employee_check(work_hours))

result=employee_check(work_hours)
print(result)

name,hours=employee_check(work_hours)
print(name)

name,hours=employee_check(work_hours)
print(hours)