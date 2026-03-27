# -------------------------------
# 1. PRINT NUMBERS
# -------------------------------

print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

print("\nNumbers from 20 to 30:")
for i in range(20, 31):
    print(i)

print("\nNumbers from 20 to 24:")
for i in range(20, 25):
    print(i)


# -------------------------------
# 2. GAME - BULLETS SYSTEM
# -------------------------------

print("\n--- Bullet Game ---")
bullets = 10

while bullets > 0:
    print(f"{bullets} bullets are left, you can shoot!!")
    bullets -= 1

print("Game Over")


# -------------------------------
# 3. GAME - MOVES SYSTEM
# -------------------------------

print("\n--- Moves Game ---")
moves = 32

while moves > 0:
    print(f"{moves} moves are left, you can play!!")

    # Winning condition (example)
    if moves == 25:
        print("You win the game!!!")
        break

    moves -= 1
else:
    print("Game Over")


# -------------------------------
# 4. STUDENT ATTENDANCE SYSTEM
# -------------------------------

print("\n--- Student Attendance ---")

data = {}

n = int(input("Enter no of students: "))

# Input names
for i in range(n):
    name = input("Enter the name: ")
    data[name] = False

# Update attendance
for name in data:
    status = int(input(f"Enter the {name} status (0-Absent,1-Present): "))
    if status == 1:
        data[name] = True

print("\nFinal Attendance:")
print(data)


# -------------------------------
# 5. STRING OPERATIONS
# -------------------------------

print("\n--- String Operations ---")

s = "python"

print(s)
print(s + " lang")
print(s * 5)
print("-" * 20)

# Indexing
print("Indexing:")
print(s[0], s[3], s[-1])

# Slicing
names = "manideep venkat tharun prudhvi bhuvan manoj"

print("\nSlicing:")
print(names[:8])
print(names[9:15])
print(names[::-1])  # reverse

# Membership
print("\nMembership:")
print("venkat" in names)
print("anju" not in names)

# Functions
print("\nFunctions:")
print(len(names))
print(max(names))
print(min(names))

# Replace & Split
print("\nReplace & Split:")
print(names.replace("tharun", "manideep"))
print(names.split())

# Alignment
s2 = "python programming"
print("\nAlignment:")
print(s2.center(30, '-'))
print(s2.ljust(30, '-'))
print(s2.rjust(30, '-'))

# Strip
s3 = "     python     "
print("\nStrip:")
print(s3.strip())
print(s3.lstrip())
print(s3.rstrip())
