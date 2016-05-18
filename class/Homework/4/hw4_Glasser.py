#Task 1

def count_change(amount, coins):
    if amount == 0:
        return 1
    elif amount < 0 or coins == []:
        return 0
    else:
        return count_change(amount - coins[0], coins) + \
               count_change(amount, coins[1:])
print(count_change(15, [5, 10, 25]))
print(count_change(6, [1, 5, 10, 25]))
print(count_change(6, [1, 2, 5]))

def possible_changes(amount, coins):
    if amount == 0:
        return str(amount)
    elif amount < 0 or coins == []:
        return None
    else:
        return count_change(amount - coins[0], coins) + \
               count_change(amount, coins[1:])
print("\n")
print(possible_changes(15, [5, 10, 25]))
# print(count_change(6, [1, 5, 10, 25]))
# print(count_change(6, [1, 2, 5]))