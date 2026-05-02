def myfunction(n):
    for i in range(0, n + 1):
        print("First Loop")

    j = 1
    while j <= n + 1:
        print("Second Loop", j)
        j = j * 2

    for i in range(0, 100):
        print("Third Loop")


print("Time Complexity Analysis:")
print("First loop: O(n)")
print("Second loop: O(log n)")
print("Third loop: O(1)")
print("Overall Time Complexity: O(n)")
