from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    # return HttpResponse('<h1>Welcome nigga</h1>')
    return render(request, 'PaySlipCalculation/HomePage.html')

def calculate(request):
    if request.GET['name'] == "" or request.GET['salary'] == "" or request.GET['leave'] == "" or request.GET['overtime'] == "" or request.GET['position'] == "blank":
        content = {'msg': 'Please enter all the fields !'}
        return render(request, 'PaySlipCalculation/HomePage.html', content)

    salary = int(request.GET['salary'])
    leave = float(request.GET['leave'])
    overtime = int(request.GET['overtime'])
    position = str(request.GET['position'])

    if position == "Jr":
        desig = 'Junior Analyst'
        overtimehourly = 100
    elif position == "Sr":
        desig = 'Senior Analyst'
        overtimehourly = 300
    elif position == "Hr":
        desig = 'Human Resource'
        overtimehourly = 400
    elif position == "Mn":
        desig = 'Manager'
        overtimehourly = 500

    overtimevalue = overtimehourly * overtime
    dailysalary = salary / 28
    deducted = int(leave * dailysalary)
    result = int(salary - deducted)
    result = result + overtimevalue

    content = {'net': 'Net Salary: $ ' + str(result), 'deducted': 'Deductions: $ ' + str(deducted), 'overtimepay': '(Overtime hourly rate for ' + desig + ' is $' + str(overtimehourly) + ')','info': '[For queries, Please contact tenthinten@gmail.com]'}
    return render(request, 'PaySlipCalculation/HomePage.html', content)

def reset(request):
    content = {'msg': ''}
    return render(request, 'PaySlipCalculation/HomePage.html', content)
