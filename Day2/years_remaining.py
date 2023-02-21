# https://waitbutwhy.com/2014/05/life-weeks.html

# Instructions I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we
# actually have. https://waitbutwhy.com/2014/05/life-weeks.html Create a program using maths and f-Strings that tells
# us how many days, weeks, months we have left if we live until 90 years old. It will take your current age as the
# input and output a message with our time left in this format: You have x days, y weeks, and z months left. Where x,
# y and z are replaced with the actual calculated numbers. Warning your output should match the Example Output format
# exactly, even the positions of the commas and full stops.

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# Try copying the example output into your code and replacing the relevant parts so that
# the sentence is formated the same way.

age = int(input('Whats your age? '))

years = 90 - age
months = (90 * 12) - (age * 12)
weeks = (90 * 52) - (age * 52)
days = (90 * 365) - (age * 365)

print(f"You have {days} days left, {weeks} weeks left, {months} months left, and {years} years left, enjoy your life")