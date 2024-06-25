def get_starting_number():
    while True:
        try:
            num = int(input("How many bottles of beer on the wall? "))
            if num >= 1:
                return num
            else:
                print("Please enter an integer 1 or greater.")
        except ValueError:
            print("Please enter a valid integer.")

def sing(starting_bottles):
    bottles = starting_bottles
    while bottles > 0:
        if bottles == 1:
            print(f"1 bottle of beer on the wall, 1 bottle of beer!")
            print("Take one down, pass it around, no more bottles of beer on the wall!\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer!")
            print(f"Take one down, pass it around, {bottles-1} {'bottle' if bottles-1 == 1 else 'bottles'} of beer on the wall!\n")
        bottles -= 1

if __name__ == "__main__":
    starting_bottles = get_starting_number()
    sing(starting_bottles)