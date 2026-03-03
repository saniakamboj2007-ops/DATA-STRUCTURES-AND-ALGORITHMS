# aert_toolkit.py
# Algorithmic Efficiency & Recursion Toolkit (AERT)

# ---------------------------
# Part A: Stack ADT
# ---------------------------

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -----------------------------------
# Part B (i): Factorial (Recursive)
# -----------------------------------

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ------------------------------------------
# Part B (ii): Fibonacci (Recursive)
# ------------------------------------------

naive_calls = 0
memo_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ---------------------------
# Part C: Tower of Hanoi
# ---------------------------

def tower_of_hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary, stack)
    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)
    tower_of_hanoi(n - 1, auxiliary, source, destination, stack)


# ---------------------------
# Part D: Recursive Binary Search
# ---------------------------

def binary_search(arr, key, low, high, stack):
    if low > high:
        return -1
    mid = (low + high) // 2
    stack.push(mid)
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1, stack)
    else:
        return binary_search(arr, key, mid + 1, high, stack)


# ---------------------------
# Main Function
# ---------------------------

def main():
    print("===== FACTORIAL =====")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) =", factorial(n))

    print("\n===== FIBONACCI =====")
    for n in [5, 10, 20, 30]:
        global naive_calls, memo_calls
        naive_calls = 0
        memo_calls = 0
        print(f"\nFibonacci({n})")
        print("Naive Result:", fib_naive(n), "Calls:", naive_calls)
        print("Memo Result:", fib_memo(n, {}), "Calls:", memo_calls)

    print("\n===== TOWER OF HANOI (N=3) =====")
    stack = StackADT()
    tower_of_hanoi(3, "A", "B", "C", stack)

    print("\n===== BINARY SEARCH =====")
    arr = [1, 3, 5, 7, 9, 11, 13]
    keys = [7, 1, 13, 2]

    for key in keys:
        stack = StackADT()
        result = binary_search(arr, key, 0, len(arr) - 1, stack)
        print(f"Search {key}: Index =", result, "| Mid indices visited:", stack.stack)

    empty_arr = []
    stack = StackADT()
    print("Search in empty array:", binary_search(empty_arr, 5, 0, -1, stack))


if __name__ == "__main__":
    main()