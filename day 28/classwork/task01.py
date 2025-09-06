#List და Tuple შორის განსხვავება:

#List → შეიძლება შეცვლა.

#Tuple → ვერ იცვლება.

the_year_people_were_born = (2025, 2024, 1780, 1790, 1589)
baby, child, *dead = the_year_people_were_born
print(baby, child, dead)
