
limit = 1000

is_prime = [True] * (limit + 1)

for num_to_check in range(2, limit+1):
    if is_prime[num_to_check]:
        print(num_to_check, end=' ')
        for i in range(num_to_check, limit+1, num_to_check):
            is_prime[i] = False
print('\n')
