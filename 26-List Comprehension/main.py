
# numbers = [1, 2, 3, 4]
# add_1_numbers = [n+1 for n in numbers]
# print(add_1_numbers)

# name = "Angela"
# letters = [letter for letter in name]
# print(letters)

numbers = range(1,5)
double = [number*2 for number in numbers]
print(double)

student_score = {
    "Amir" : 32,
    "Ali" : 95,
    "Bun" : 75
}
student_score_df = pandas.DATAFRAME(student_score)
