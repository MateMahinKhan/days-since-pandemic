from datetime import date


# Start of pandemic 11 March 2020
# End of pandemic 4 May, 2023


d0 = date(2020, 3, 11)
d1 = date(2023, 5, 4)
delta = d1 - d0


print('Pandemic lasted ' + str(delta.days) + ' Days')