# Kordebalet67
# This program is for vizualisation addictive row
# of natural numbers and their sum of divisors.
# Also, prime numbers signed as red dots and
# simple numbers colored as green dots
# ===================================================================================================
import matplotlib.pyplot as plt
import math as m
import plotly.express as px
import pandas as pd


# Function for calculation sum of divisors
def sum_dividers(number: int) -> int: 
    dividers_sum = 1
    for div in range(2,number):
        if number % div == 0:
            dividers_sum += div
            
    return dividers_sum

# Function to make from lists of natural numbers (x)
# and sums of divisors (y) lists of prime numbers (x_prime) 
# and their sums of divisors (y_prime)
def is_prime(x: list, y: list) -> list:
    x_prime = []
    y_prime = []
    for i in range(0, len(x)):
        if x[i] == y[i]:
            x_prime.append(x[i])
            y_prime.append(y[i])
    
    return x_prime, y_prime

# Function to make from lists of natural numbers (x)
# and sums of divisors (y) lists of simple numbers (x_simple) 
# and their sums of divisors (y_simple)
def is_simple(x: list, y: list):
    x_simple = []
    y_simple = []
    for i in range(0, len(x)):
        if y[i] == 1:
            x_simple.append(x[i])
            y_simple.append(y[i])
    
    return x_simple, y_simple

# Function for generating list of natural numbers from 1 
# to user input and calculating the list of sums
def natural_generation(input: int) -> list:
    x = list(range(0, input, 1))
    y = [sum_dividers(item) for item in x]

    return x, y

# Visualisation function
def build_graphic(x: list, y: list, x_prime: list, y_prime: list, x_simple: list, y_simple: list):

    # making dataset for prime numbers
    # -----------------------------------------------------------------------------------------------
    prime = ["is prime" for i in range (0, len(x_prime))] 
    data_prime = {'x_prime': x_prime, 'y_prime': y_prime, 'is_prime': prime}
    df_prime = pd.DataFrame(data = data_prime)
    # building the dots on graphic
    fig = px.scatter(df_prime, x="x_prime", y="y_prime", hover_data=["is_prime"])
    # -----------------------------------------------------------------------------------------------

    # making dataset for simple numbers
    # -----------------------------------------------------------------------------------------------
    simple = ["is simple" for i in range (0, len(x_simple))]
    data_simple = {'x_simple': x_simple, 'y_simple': y_simple, 'is_simple': simple}
    df_simple = pd.DataFrame(data = data_simple)
    # building the another dots on graphic
    fig = px.scatter(df_simple, x="x_simple", y="y_simple", hover_data=["is_simple"])
    # -----------------------------------------------------------------------------------------------

    # settings of graphic screen
    # -----------------------------------------------------------------------------------------------
    fig = plt.figure(figsize=(36, 12))
    #fig_prime.patch.set_facecolor('grey')
    ax = fig.add_subplot()                  # making a subplot to customize our graphic
    ax.patch.set_facecolor('grey')          # set background color of graphic
    ax.patch.set_alpha(0.5)                 # set background color transparency
    plt.grid(which='major')                 # enable major grid
    plt.grid(which='minor', linestyle=':')  # enable minor grid                   
    # --------------------------------------
    # adding our data on graphic
    plt.plot(x, y, 'ok', label='Standart')                # standart number signed with balck dots
    plt.plot(x_prime, y_prime, 'or', label='Prime')       # prime number signed with red dots
    plt.plot(x_simple, y_simple, 'og', label='Simple')    # simple number signed with green dots
    # -----------------------------------------------------------------------------------------------
    # --------------------------------------
    # adding some custom things on graphic
    plt.title('Types of numbers', fontsize = 40)    # adding title on our graphic
    plt.xlabel('Natural numbers', fontsize = 30)    # adding subscription to X axis
    plt.ylabel('Sum of divisors of number',         
               fontsize = 30)                       # adding subscription to Y axis
    plt.semilogy()                                  # enable logarithmic scale
    plt.legend (title='Types of numbers', 
                fontsize = 20, title_fontsize = 24) # adding legend on our graphic

    # show the result
    plt.show()