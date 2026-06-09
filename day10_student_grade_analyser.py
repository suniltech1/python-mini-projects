 #Day9 assignment: Student Grade Analyser

#TASK 1: 
def letter_grade(score):
    if score < 0 or score> 100:
        raise ValueError ("Invalid score! Score must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >=80:
        return "B"
    elif score >=70:
        return "C"
    elif score >=60:
        return "D"
    else:
        return "F"
    
    
#TASK 2:
def analyse(students):
    results = {}

    for name, score in students.items():
       results = {}
    for name, score in students.items():
        grade = letter_grade(score)        
        results[name] = {"score": score, "grade": grade}
    return results


#TASK 3:
#
def summary(results):
    
# Calculate average, highest, lowest scores and grade counts
    scores = [data["score"] for data in results.values()]
    average = sum(scores) / len(scores)

    
    highest = max(results, key=lambda k: results[k]["score"])
    lowest = min(results, key=lambda k: results[k]["score"])

    counts = {}
    for data in results.values():
        grade = data["grade"]
        counts[grade] = counts.get(grade, 0) + 1

   
    for grade in ["A", "B", "C", "D", "F"]:
        counts.setdefault(grade, 0)

# Print summary
    print("Student Results:")
    for name in sorted(results):
        score = results[name]["score"]
        grade = results[name]["grade"]
        print(f"{name:<7}: {score:>3} → {grade}")

    print()
    print(f"Class Average : {average:.2f}")
    print(f"Highest Score : {highest} ({results[highest]['score']})")
    print(f"Lowest Score  : {lowest} ({results[lowest]['score']})")
    print(
        f"Grade Counts  : "
        f"A={counts['A']}  "
        f"B={counts['B']}  "
        f"C={counts['C']}  "
        f"D={counts['D']}  "
        f"F={counts['F']}"
    )


# Task 4
#exceptions are handled in the main block to catch any invalid scores in the input data.
try:
    students = {
        "Alice": 92,
        "Bob": 78,
        "Carol": 85,
        "Dave": 61,
        "Eve": 55,
        "Frank": 99
    }

    results = analyse(students)
    summary(results)

except ValueError as e:
    print(f"Error: {e}")