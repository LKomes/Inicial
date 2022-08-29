def is_leap(year):
    leap = False
    if (year%4==0):
        if year%100==0 and year%400!=0:
            leap = False
        else:
            leap = True
    if year<1900 or year>1000001:
        leap = False
    # Write your logic here
    
    return leap

year = int(raw_input())
print is_leap(year)
