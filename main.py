print("Loan Calculator")

print("$1000 over 10 years at 5% APR")

result = int(1000)
apr = 0.05

for i in range (10):
  result = result * (1 + apr)
  print("Year", i+1, "is", round(result, 2))