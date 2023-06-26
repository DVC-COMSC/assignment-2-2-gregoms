def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    print(f"Welcome to Celsius to Fahrenheit Converter!")

    celcius = float(input("Please enter the temperature in celsius: "))

    fahrenheit = ((9/5) * celcius) + 32

    print(f"The temperature in fahrenheit is: \t {fahrenheit:.2f}")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
