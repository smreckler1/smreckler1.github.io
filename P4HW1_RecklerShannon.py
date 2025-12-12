#Title: Shannon Reckler
#Date: 11/9/2025
#Assignment Name: P4 HW 1
#A brief description of the project: Assignment assess student ability to edit and enhance exiting program

num_scores = int(input("How many scores would you like to enter? "))

score_list = []

for i in range(1, num_scores + 1):
    while True:
        try:
            score = float(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:
                score_list.append(score)
                break  
            else:
                print("INVALID Score entered!!!! \nScore should be between 0 and 100")
                prompt = f"Enter score #{i}again: "
        except ValueError:
            print("INVALID Score entered!!!! \nScore should be between 0 and 100")
            prompt = f"Enter score #{i}again: "

lowest_score = min(score_list)

modified_list = score_list.copy()
modified_list.remove(lowest_score)

average_score = sum(modified_list) / len(modified_list)

if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("\n-------------- Results --------------")
print(f"Lowest score: {lowest_score:.1f}")
print(f"Modified List: {modified_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade: {letter_grade}")
print("-------------------------------------")   