#Task 1

# def count_change(amount, coins):
#     if amount == 0:
#         return 1
#     elif amount < 0 or coins == []:
#         return 0
#     else:
#         return count_change(amount - coins[0], coins) + \
#                count_change(amount, coins[1:])
# print(count_change(15, [5, 10, 25]))
# print(count_change(6, [1, 5, 10, 25]))
# print(count_change(6, [1, 2, 5]))

def possible_changes(amount, coins):

    result = [ ]

    def rec_helper(amt, denom,cs):
        if amt == 0:
            result.append(denom)
        elif amt > 0 and len(cs) > 0:
            rec_helper(amt - cs[0], denom + [cs[0]], cs)
            rec_helper(amt,denom, cs[1:])
    rec_helper(amount, [], coins)

    return result
print(possible_changes(15, [5, 10, 15]))
print(possible_changes(6, [1, 5, 10, 25]))
print(possible_changes(6, [1, 2, 5]))
#     if amount == 0:
#         return str(amount)
#     elif amount < 0 or coins == []:
#         return None
#     else:
#         return count_change(amount - coins[0], coins) + \
#                count_change(amount, coins[1:])
# print("\n")
# print(possible_changes(15, [5, 10, 25]))
# # print(count_change(6, [1, 5, 10, 25]))
# # print(count_change(6, [1, 2, 5]))