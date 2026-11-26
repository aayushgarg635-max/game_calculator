import random
secret_number = random.randint(1,100)

for i in range(1,8):
    guess = int(input("Enter your number: "))

    if  guess == secret_number:
            print("correct guess")
            break
    elif guess > secret_number:
       print("lower number please")
       remaining = 7 - i
    elif guess < secret_number:
        print("higher number please")
        remaining = 7 -i 
    print("Remaining chances:",remaining)

else:
    print("Game over")
    print("secret_number:",secret_number)
      
    
print("Thank You")