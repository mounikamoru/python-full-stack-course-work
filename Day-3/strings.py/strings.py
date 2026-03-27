# 1. Print numbers 1 to 10
for i in range(1, 11):
    print(i)


# 2. Print numbers 20 to 30
for i in range(20, 31):
    print(i)


# 3. Bullets game countdown
bullets = 10

while bullets > 0:
    print(bullets, "bullets are left, you can shoot!!")
    bullets -= 1

print("Game Over")


# 4. Moves game (win condition)
moves = 32

while moves > 0:
    print(moves, "moves are left, you can play!!")
    
    if moves == 25:
        print("You win the game!!!")
        break
    
    moves -= 1


# 5. Student attendance dictionary
data = {}

n = int(input("Enter no of students: "))

for i in range(n):
    name = input("Enter the name: ")
    data[name] = False

for name in data:
    status = int(input(f"Enter the {name} status(0-Absent,1-Present): "))
    data[name] = True if status == 1 else False

print(data)


# 6. String operations
s = "python"

print(s + " lang")
print(s * 3)
print(s[0])
print(s[-1])


# 7. String slicing
names = "manideep venkat tharun prudhvi bhuvan manoj"

print(names[:8])
print(names[9:15])
print(names[::-1])


# 8. String functions
names = "manideep venkat tharun prudhvi bhuvan manoj"

print(names.split())
print(names.replace("tharun", "manideep"))
print(len(names))
print(max(names))
print(min(names))


# 9. String formatting
s = "python programming"

print(s.center(30, '-'))
print(s.ljust(30, '-'))
print(s.rjust(30, '-'))


# 10. Strip functions
s = "           python             "

print(s.strip())
print(s.lstrip())
print(s.rstrip())
