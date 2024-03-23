counter = 0  # Global variable

def increment_counter():
    counter += 1  # Bug: This attempts to modify the global variable without declaring it

def main():
    increment_counter()
    print(f"Counter: {counter}")

if __name__ == "__main__":
    main()
