#-------------------------------------------------------------------------------
#Program:       Designing a Program From a Desciption - Salesman's Salery
#Programmer:    Amber Murphy
#Date:          05/30/2013
#Abstract:      This program will compute the amount telephone solicitors
#               will be paid each week. The hourly, commission, and witholding rates
#               are stored using global constants.  
#               The program displays the sales amount, hours worked, hourly pay amount,
#               commission amount, gross pay, witholding amount, and net pay.
#-------------------------------------------------------------------------------

#Define the global constants
HOURLY_PAY_RATE = 7.50
COMMISSION_RATE = 0.05
WITHOLDING_RATE = 0.25

#Define the main function
def main():
    #Call the display message function.
    display_message()
    
    #Input the sales amount and hours worked from the user
    sales_amount = float(input('Please enter the sales amount: '))
    hours_worked = float(input('Please enter the total number of hours worked: '))
    
    #Calculations for display
    hourly_pay_amount = hours_worked * HOURLY_PAY_RATE
    commission_amount = sales_amount * COMMISSION_RATE
    gross_pay =  hourly_pay_amount + commission_amount
    witholding_amount = gross_pay * WITHOLDING_RATE
    net_pay = gross_pay - witholding_amount
    
    
    #Call the display results function passing the 7 values for printing
    display_results(sales_amount, hours_worked, hourly_pay_amount, commission_amount, gross_pay, witholding_amount, net_pay)
    
#Define the display message function
def display_message():
    print('This program calculates the salesperson\'s pay')
    print('Seven values are displayed:')
    print('hourly pay, commission, gross pay, witholding, and net pay,')
    print(' and the two original inputs: sales amount and hours worked.')
    print()
    
#Define the display results function
def display_results(sales_amount, hours_worked, hourly_pay_amount, commission_amount, gross_pay, witholding_amount, net_pay):
    
    #Print the 7 values received formatted as currency.
    print('The sales amount is $', format(sales_amount, ',.2f'), sep='')
    print('The hours worked selected are ', hours_worked)
    print('The hourly pay amount is $', format(hourly_pay_amount, ',.2f'), sep='')
    print('The commission amount is $', format(commission_amount, ',.2f'), sep='')
    print('The gross pay is $', format(gross_pay, ',.2f'), sep='')
    print('The witholding amount is $', format(witholding_amount, ',.2f'), sep='')
    print('The net pay amount due is $', format(net_pay, ',.2f'), sep='')
    
#call the main function
main()
