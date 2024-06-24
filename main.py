from InquirerPy import prompt
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

print("\n", Fore.RED + Style.BRIGHT + '\t\t\t\t<========', 
      Fore.RED + Style.BRIGHT + Back.WHITE + ' CODE WITH AMINA NOOR', 
      Fore.RED + Style.BRIGHT + '========>\n')
print(Fore.GREEN + Style.BRIGHT + '\t\t\t\t\t<----------', 
      Fore.BLUE + Style.BRIGHT + 'Check Your MarkSheet', 
      Fore.GREEN + Style.BRIGHT + '---------->\n\n')

# Asking for name
name = prompt([
    {
        "type": "input",
        "name": "myName",
        "message": Fore.BLUE + Style.BRIGHT + "Please Enter Your Name..."
    }
])

# Asking for roll number
roll = prompt([
    {
        "type": "input",
        "name": "num1",
        "message": Fore.BLUE + Style.BRIGHT + "Please Enter your roll number... ",
        "validate": lambda val: val.isdigit() or "Please enter a valid number",
        "filter": lambda val: int(val)
    }
])
roll_num = roll["num1"]

# Checking roll number
if roll_num:
    marks = prompt([
        {
            "type": "input",
            "name": "typescript",
            "message": Fore.BLUE + Style.BRIGHT + "Please enter your typescript number:",
            "validate": lambda val: val.isdigit() or "Please enter a valid number",
            "filter": lambda val: int(val)
        },
        {
            "type": "input",
            "name": "python",
            "message": Fore.BLUE + Style.BRIGHT + "Please enter your python number:",
            "validate": lambda val: val.isdigit() or "Please enter a valid number",
            "filter": lambda val: int(val)
        },
        {
            "type": "input",
            "name": "java",
            "message": Fore.BLUE + Style.BRIGHT + "Please enter your java number:",
            "validate": lambda val: val.isdigit() or "Please enter a valid number",
            "filter": lambda val: int(val)
        },
    ])

    # Extract marks
    ts = marks["typescript"]
    pyth = marks["python"]
    java = marks["java"]

    # Calculate percentage
    total_marks = 300
    obtain_marks = ts + pyth + java
    percent = (obtain_marks / total_marks) * 100

    # Display results
    print(Fore.GRAY + f'\t\tName: {name["myName"]}')
    print(Fore.GREEN + f'Typescript marks = {ts} out of 100')
    print(Fore.YELLOW + f'Python marks = {pyth} out of 100')
    print(Fore.RED + f'Java marks = {java} out of 100')
    print(Fore.CYAN + f'Obtain Mark = {obtain_marks}\nTotal Marks = {total_marks}')
    print(Fore.MAGENTA + f'Percentage = {percent:.0f}%')

    # Assign grades function
    def assign_grades(score):
        if 100 >= score >= 90:
            print("Congratulations! Your Score is: A+")
        elif 90 > score >= 80:
            print("Congratulations! Your Score is: A")
        elif 80 > score >= 70:
            print("Congratulations! Your Score is: B+")
        elif 70 > score >= 60:
            print("Your Score is: B")
        elif 60 > score >= 50:
            print("Your Score is: C+")
        elif 50 > score >= 40:
            print("Your Score is: C")
        else:
            print("Your Score is: F")

    assign_grades(percent)
    print("\n", Fore.RED + Style.BRIGHT + '\t\t\t\t<======', 
          Fore.RED + Style.BRIGHT + Back.WHITE + 'Allah Hafiz', 
          Fore.RED + Style.BRIGHT + '=====>\n')

else:
    print(Fore.RED + "Invalid roll number")