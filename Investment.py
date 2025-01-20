amount=float(input("enter the investment amount"))
interest=float(input("enter the interest"))/100
years=int(input("enter the number of years"))
final=amount
for years in range(1,years+1):
          final=final+(final*interest)
          print("year",years,"investment:",final)
print("total amount:",final)
