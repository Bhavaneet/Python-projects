def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)

def main():
    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            raise ValueError("The number of disks must be a positive integer.")
        print(f"Solving Tower of Hanoi for {n} disks:")
        tower_of_hanoi(n, 'A', 'B', 'C')
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()