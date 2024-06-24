

'''
   Write a program that begins by reading a temperature from the degree Celsius.
   Then your progam should dispay the equivalent temperature in degrees Fehrenheit and
   degrees Kelvin.
   NB: The calculations needed to convert between different units of temperature can be
   found on the internet.
'''

# collect or read user's temperature value
TempC = int(input("What's the temperaature in ֯֯ C : "))

# Converting to Kelvin
TempK = 273 + TempC
print('Equivalent Temperature in Kelvin : ', float(TempK))

# Converting to Fehrenheit
TempF = (TempC * (9/5)) + 32
print('Equivalent Temperature in Fehrenheit : ', float(TempF))


