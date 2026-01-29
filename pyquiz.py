def run_quiz():
    questions = [   
        {
            'question': "Who is the founder of python programming language?",
            'options': ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
            'answer': "A"
        },
        {
            'question': "Which type of Programming does Python support?",
            'options': ["A. Object-Oriented Programming", "B. Procedural Programming", "C. Functional Programming", "D. All of the above"],
            'answer': "D"
        },
        {
            'question': "Which of the following is the correct extension of the Python file?",
            'options': ["A. .python", "B. .pl", "C. .py", "D. .p"],
            'answer': "C"
        },
        {
            'question': "Which keyword is used for function in Python language?",
            'options': ["A. Function", "B. Def", "C. Fun", "D. Define"],
            'answer': "B"
        },
        {
            'question': "Which of the following is not a core data type in Python?",
            'options': ["A. Lists", "B. Dictionary", "C. Tuples", "D. Class"],
            'answer': "D"
        },
        {
            'question': "Which of the following character is used to give single-line comments in Python?",
            'options': ["A. //", "B. #", "C. <!--", "D. /*"],
            'answer': "B"
        },
        {
            'question': "Which of the following functions can help us to find the version of python that we are currently working on?",
            'options': ["A. sys.version()", "B. sys.version", "C. sys.version[]", "D. sys.version()"],
            'answer': "B"
        },
        {
            'question': "Which of the following is the floor division operator in Python?",          
            'options': ["A. /", "B. //", "C. %", "D. **"],
            'answer': "B"
        },
        { 
            'question': "Which of the following functions is a built-in function in python?",                 
            'options': ["A. factorial()", "B. print()", "C. seed()", "D. sqrt()"],
            'answer': "B"  
        },  
        {   
            'question': "Which of the following statements is used to create an empty set in Python?",
            'options': ["A. {}", "B. set()", "C. []", "D. ()"], 
            'answer': "B"     
        },
        {
            'question': "What will be the output of the following code snippet?\nprint(type([]) is list)",
            'options': ["A. True", "B. False", "C. TypeError", "D. None of the above"],
            'answer': "A"
        },
        {
            'question': "Which of the following is used to define a block of code in Python language?",
            'options': ["A. Indentation", "B. Key", "C. Brackets", "D. None of these"],
            'answer': "A"   
        },
        {   
            'question': " Which of the following is not a keyword in Python language?",
            'options': ["A. eval", "B. assert", "C. nonlocal", "D. pass"],
            'answer': "A"
        },
        {
            'question':  "Which of the following data types is immutable in Python?",
            'options': ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
            'answer': "D"
        },
        {
            'question': "What is the output of the following code snippet?\nprint(len(\"Hello, World!\"))",
            'options': ["A. 10", "B. 12", "C. 13", "D. 14"],
            'answer': "C"        
        },
        {
            'question':"Which method is used to add an element at the end of a list in Python?",
            'options': ["A. add()", "B. append()", "C. insert()", "D. extend()"],
            'answer': "A"  
        }, 
        {
            'question':"What will be the output of the following code snippet?\nprint(2 ** 3 ** 2)",
            'options': ["A. 64", "B. 512", "C. 256", "D. 1024"],
            'answer': "B"
        },
        {   
            'question':"Which of the following functions is used to read a file in Python?",
            'options': ["A. open('file.txt', 'r')", "B. open('file.txt', 'w')", "C. open('file.txt', 'a')", "D. open('file.txt', 'x')"],
            'answer': "A"
        },
        {
            'question':"what is data type of None in python?",
            'options': ["A. int", "B. str", "C. NoneType", "D. float"],
            'answer': "C"
        },
        {
            'question':"what is list used for in python?",
            'options': ["A. To store multiple items in a single variable", "B. To perform mathematical calculations", "C. To define functions", "D. To handle exceptions"],
            'answer': "A"
        }
    ]

    score = 0

    for index, q in enumerate(questions):
        print(f"Q{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)

        user_answer = input("Your answer(A/B/C/D): ")
        if user_answer.strip().upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1

    print(f"Your final score is {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()