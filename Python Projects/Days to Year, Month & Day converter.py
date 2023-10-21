#Days to Year, Month & Day converter

days = int(input('Enter value in days :')) # this will take input as days
month = days//30 # this will store before decimal value of month
year = month//12 # this will store before decimaln value of year
month = month-(year*12) # this will reduce the whole month value to remaining month value
days = days-((year*360)+(month*30)) # this will reduce the whole days valu to remaining days value
print (days,'days =',year,'year',month,'month',days,'days') # this will print the required output