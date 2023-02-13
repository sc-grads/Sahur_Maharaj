visits = {'Monday': 5000,
          'Tuesday': 3000,
          'Wednesday': 4000,
          'Thursday': 4500,
          'Friday': 5000,
          'Saturday': 2000,
          'Sunday': 1500
          }

## YOUR CODE STARTS HERE
# 1
total_visits = 0
for k, v in visits.items():
    total_visits += v
print(f'Total website visits are: {total_visits}')

# 2
percentage = {k: (v / total_visits) * 100 for k, v in visits.items()}
print(percentage)
