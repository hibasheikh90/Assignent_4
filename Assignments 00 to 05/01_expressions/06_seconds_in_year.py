# Useful constants to help make the math easier and cleaner!
days_per_year: int = 365  
hours_per_day: int = 24  
min_per_hour: int = 60  
sec_per_min: int = 60  

def main():
    """
    Calculates the total number of seconds in a year 
    using predefined constants and prints the result.
    """
    # Calculate the total number of seconds in a year
    seconds_in_year: int = days_per_year * hours_per_day * min_per_hour * sec_per_min  

    # Print the result in a user-friendly format
    print(f"There are {seconds_in_year} seconds in a year!")  

if __name__ == '__main__':
    main()
