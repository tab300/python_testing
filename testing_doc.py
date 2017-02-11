# testing_doc.py

# Method to calculate simple interest

def simple_interest(principal, rate, time):
    return principal * rate * time /100

# Method to calculate the future value of compound interest

def fv_compound_interest(principal, rate, time):
    return principal + (principal * rate * time / 100)