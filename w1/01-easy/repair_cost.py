# Total repair cost
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, representing the vehicle repair costs in dollars
# from several suppliers following a motor accident, and the deposit
# paid for the work:

panel_beating = 1500
mechanics = 895
spray_painting = 500
tyres = 560

deposit = 200

# Write an expression to calculate the total cost outstanding
# after the deposit has been paid, and the repairs completed.
# Then print an appropriate message to screen including the
# amount owing.

# Use the following problem solving strategy:
# 1. Calculate the sum of all the costs
# 2. Deduct the amount of the deposit already paid
# 3. Display the result

total_cost = panel_beating + mechanics + spray_painting + tyres
cost_outstanding = total_cost - deposit

print(f"The total cost for services delivered is ${total_cost}.")
print(f"With your deposit deducted, ${cost_outstanding} is owed.")