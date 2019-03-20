def permute(A):
    if len(A) == 1:
        return A

    evens = [x for i, x in enumerate(A) if i % 2 == 0]
    odds = [x for i, x in enumerate(A) if i % 2 == 1]

    return permute(evens) + permute(odds)

print(permute([1, 2, 3, 4]))
print(permute([1, 2, 3, 4, 5, 6]))
print(permute(list(range(1, 21))))
