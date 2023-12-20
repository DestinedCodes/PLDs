#!/usr/bin/python3


print(
    """Exception Chaser
    Aim: Generate as many exceptions as possible
    Rules:
        - You have 15 trials
        - Each exception can be generated only once
        - You get 1 point for each new exception
        - You lose 1 point if you don't generate a valid exception
        - You win if you get 10 points
        - You don't lose, you can always try again
    """
)

errors = []
score = 0
trials_left = 15

while trials_left > 0 and score < 10:
    trials_left -= 1
    command = input("\n>>> ")

    try:
        exec(command)
        if score != 0:
            score -= 1
        print(f"Score: {score}/5 | Trials left: {trials_left}")
    except Exception as e:
        exception_name = e.__class__.__name__
        if exception_name not in errors:
            errors.append(exception_name)
            score += 1

        print(f"Score: {score}/5 | Trials left: {trials_left}")
        print(f"Exception: {exception_name}")
    continue

if score == 5:
    print(f"\nYou win! | Final score: {score}/10")
else:
    print(f"\nFinal score: {score}/10, you can always try again!")

print("Exceptions generated:")
for error in errors:
    print(f"    - {error}")
