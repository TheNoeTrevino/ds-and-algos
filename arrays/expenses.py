# --------------- Section 1 --------------- #
monthly_expenditures = [
    2200,
    2350,
    2600,
    2130,
    2190,
]

all_answers = []
# 1. In Feb, how many dollars you spent extra compare to January?
answer_1 = monthly_expenditures[1] - monthly_expenditures[0]
all_answers.append(answer_1)

# 2. Find out your total expense in first quarter (first three months) of the year.
answer_2 = 0
for month in monthly_expenditures[:3]:
    answer_2 += month

# 3. Find out if you spent exactly 2000 dollars in any month
if monthly_expenditures.count(2000) > 0:
    answer_3 = True
else:
    answer_3 = False

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expenditures.append(1980)

answer_4 = monthly_expenditures[5]

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
monthly_expenditures[3] -= 200
if monthly_expenditures[3] == 1930:
    answer_5 = "Corrected"
else:
    answer_5 = "Incorrect"

# based on this
print("\nSection 1\n")
print(f'Answer to question 1:\n {answer_1} dollars more')
print(f'Answer to question 2:\n Total expenses in the first quarter: {answer_2}')
print(f'Answer to question 3:\n Did we ever spend exactly 2000 in a month? {answer_3}')
print(f'Answer to question 4:\n {answer_4}')
print(f'Answer to question 5:\n {answer_5}')

# --------------- Section 2 --------------- #

heros = [ 
    'spider man',
    'thor',
    'hulk',
    'iron man',
    'captain america',
]
# 1. Length of the list
answer_1 = len(heros) == 5

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
answer_2 = heros.__contains__('black panther')
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
answer_3 = (heros[3] == 'black panther' and heros[2] == 'hulk')
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros.remove('hulk')
heros.remove('thor')
heros.append('doctor strange')

answer_4 = heros.__contains__('doctor strange') and not (heros.__contains__('hulk') and heros.__contains__('thor'))

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()

print("\nSection 2\n")
print(f'Answer to question 1:\n {answer_1}')
print(f'Answer to question 2:\n {answer_2}')
print(f'Answer to question 3:\n {answer_3}')
print(f'Answer to question 4:\n {answer_4}')
print(f'Answer to question 5:\n {heros}')

print("\nSection 3\n")
input_number = int(input('input a number please: '))
for number in range(0, input_number):
    if number % 2 == 0:
        print(number)
    else:
        pass

