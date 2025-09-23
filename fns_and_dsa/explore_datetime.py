from datetime import datetime, timedelta

def display_current_datetime():
    
    now = datetime.now()
    current_date = now.strftime('%Y-%m-%d %H:%M:%S')
    
    print(current_date)
display_current_datetime()

prompt = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    
    now = datetime.now()
    days = timedelta(days=prompt)
    future_date = now + days

    print(future_date.strftime('%Y-%m-%d'))
calculate_future_date() 
    

