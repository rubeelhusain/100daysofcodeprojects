#tip calculator and then bill splitter
print("Welcome to Tip Calculator")
bill=int(input("Enter the bill Amount\n$"))
tipper=int(input("Enter Tip percentage\n"))
peep= int(input("Enter total people splitting the bill\n"))
print("Amount to be paid by each person\n$",round((bill+(bill*tipper/100))/peep,2))