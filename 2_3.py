A = int(input("Enter value of A (0 or 1): "))
B = int(input("Enter value of B (0 or 1): "))
C = int(input("Enter value of C (0 or 1): "))

gate1 = A and B

gate2 = B or C

gate3 = B and C

gate4 = gate2 and gate3

Q = gate1 or gate4

print("\nCircuit Output:")
print("Q =", int(Q))
