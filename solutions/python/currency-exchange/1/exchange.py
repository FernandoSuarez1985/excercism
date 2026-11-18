
def exchange_money (budget, exchange_rate):
    
    return float(budget/exchange_rate)

print (exchange_money(127.5 , 1.2))

def get_change(budget, exchanging_value):
    
    return float(budget - exchanging_value)

print(get_change (127.5 , 120)) 

def get_value_of_bills(denomination, number_of_bills):
    
    return int(denomination * number_of_bills)

print(get_value_of_bills(5, 128))

def get_number_of_bills(amount, denomination):
    
    return int (amount // denomination)

print(get_number_of_bills(127.5, 5))

def get_leftover_of_bills(amount,  denomination):
    
    return amount % denomination

print(get_leftover_of_bills (127.5 , 20))

def exchangeable_value(budget, exchange_rate, spread, denomination):
    
    new_rate = exchange_rate + (exchange_rate * (spread/100))
    total_new_currency = exchange_money (budget, new_rate)
    
    bill_new_currency = int(total_new_currency / denomination)
    maximum_value_new_currency = bill_new_currency * denomination
    
    return maximum_value_new_currency

print(exchangeable_value(127.25, 1.20, 10, 20))
