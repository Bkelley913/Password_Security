# Define the length of the password
password_length = 6

# Initialize the counter and permutations variables
counter = 1
permutations = 1

# Calculate the number of permutations for the given password length
while counter <= password_length:
  permutations = permutations * counter
  counter += 1

# Print the possible combinations of a password with the given length
print(f"The possible combination of a {password_length}-character password is: {permutations}")

# Define the number of attempts and calculate the maximum number of times the account might be locked
attempts = 5
max_lock = permutations / attempts
max_lock = int(max_lock)

# Print the maximum number of times the account might be locked
print(f"The maximum number of times the account might be locked is {max_lock} times.")

# Initialize the locks and total_lock_time variables
locks = 0
total_lock_time = 0

# Define the lock time multiplier
lock_time_multiplier = 5

# Iterate through the range of max_lock to simulate locking the account
for i in range(max_lock):
  locks += 1
  total_lock_time += locks * lock_time_multiplier
  print(f"Your account is locked for {lock_time_multiplier*locks} minutes")

  # Print the total lock time assuming the hacker only got the password right with the last possible combination
print(f"Assuming the hacker only got the password right with the last possible combination, your account would have been locked for {total_lock_time} minutes in total.")
