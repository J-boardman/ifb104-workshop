# Music download credits
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the cost in cents for downloading one
# music track, your original budget in dollars, and the number of tracks
# already downloaded:

track_cost = 120 # cost in cents for downloading one track
budget = 50 # dollars
num_downloaded = 15 # number of tracks already downloaded

# Write expressions to calculate how many more tracks you can afford
# to download and print that value to the screen.
#
# A problem solving strategy:
# 1. Calculate the amount spent so far by
#    multiplying the number downloaded by the track cost
# 2. Calculate the balance left by
#    deducting the amount spent so far from the budget
# 3. Divide the balance left by the track cost to a whole number
# 4. Print the number of tracks left
#
# Be careful to allow for the fact that one of the given values
# is expressed in cents and the other is in dollars, i.e., the
# units associated with the values are different.

amount_spent = track_cost * num_downloaded # cents
balance_left_cents = (budget * 100) - amount_spent
balance_left_dollars = budget - (amount_spent/100)
downloads_left = int(balance_left_cents / track_cost) # int() to easily/always round down since using monetary values

print(f"You have ${round(balance_left_dollars,2)} remaining.")
print(f"You can afford {downloads_left} more tracks.")
print(f"This will cost ${round(downloads_left * (track_cost/100), 2)}")
print(f"Your remaining balance will be: ${round(balance_left_dollars - (downloads_left * (track_cost/100)),2)}")
