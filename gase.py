import random

words = ['robert','berort','mishraji','mijirash','rajit','arijit','krushna','rushank','tanaya','yatana','shraddha',
        'ddhashra','namita','manita','netra','terna','ashish','shisha','abhishek','shakeabi','vishal','shalvi']

score=0
while True:
    for wr in range(3):
        lett = list(random.choice(words))
        print("Gase Correct Word By given Word :=>","".join(lett))
        user = input("enter correct word or '(quit)':")
        if user == 'quit':
            break

        if user != "".join(lett):
            valid = True
            for letter in user:
                if letter in lett:
                    lett.remove(letter)
                else:
                    valid = False
                    break

            if valid and user in words:
                score= score + len(user)
                print(f"correct and your score is {score}")
            else:
                print("Wrong Word Enter By You")
            if user != "".join(lett):
                break
        else:
            print("You enter same name which we provided...")
    else:
         score=score-len(user)
         print(f"we have reductate your {len(user)}score because you enter same word 3 times your total score is {score}")
print("Thank You for Playing...")
