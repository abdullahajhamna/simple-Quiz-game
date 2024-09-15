class Start:
    def __init__(self):
        self.name = ''
        self.age = ''

    def start(self):
        self.name = input('Enter your name: ').lower()  # Input name
        self.age = input('Enter your age: ')  # Input age and convert to integer
        print('Ok, we now know who you are...')
        print('---Sign in successfully ---\n')

class Question(Start):
    def __init__(self):
        super().__init__()  # Call the constructor of Start to initialize name and age
        # List of questions, options, and correct answers
        self.question_list = [
            {
                "question": "What is the name of the paper company featured in *The Office*?",
                "options": "A) Scranton Paper Co.\nB) Dunder Mifflin\nC) Wernham Hogg\nD) Sabre Paper Co.",
                "answer": "B"
            },
            {
                "question": "Who is the regional manager at the beginning of the series?",
                "options": "A) Michael Scott\nB) Jim Halpert\nC) Dwight Schrute\nD) Andy Bernard",
                "answer": "A"
            },
            {
                "question": "Which branch of Dunder Mifflin does the show primarily take place in?",
                "options": "A) Utica\nB) Scranton\nC) Nashua\nD) Stamford",
                "answer": "B"
            },
            {
                "question": "What is the name of the receptionist when the series begins?",
                "options": "A) Karen Filippelli\nB) Pam Beesly\nC) Erin Hannon\nD) Kelly Kapoor",
                "answer": "B"
            },
            {
                "question": "Who eventually becomes the assistant regional manager after many promotions and demotions?",
                "options": "A) Jim Halpert\nB) Stanley Hudson\nC) Ryan Howard\nD) Dwight Schrute",
                "answer": "D"
            },
            {
                "question": "Which character has a beet farm?",
                "options": "A) Andy Bernard\nB) Michael Scott\nC) Dwight Schrute\nD) Creed Bratton",
                "answer": "C"
            },
            {
                "question": "What is the name of Michael Scott's movie project?",
                "options": "A) Threat Level Midnight\nB) Agent Michael Scarn\nC) The Last Dundie\nD) Scarn’s Revenge",
                "answer": "A"
            },
            {
                "question": "Who does Jim Halpert marry?",
                "options": "A) Karen Filippelli\nB) Erin Hannon\nC) Pam Beesly\nD) Angela Martin",
                "answer": "C"
            },
            {
                "question": "Which character is known for his strange and mysterious behavior, often making bizarre comments?",
                "options": "A) Creed Bratton\nB) Toby Flenderson\nC) Kevin Malone\nD) Ryan Howard",
                "answer": "A"
            },
            {
                "question": "What is the name of the Scranton branch's HR representative?",
                "options": "A) Oscar Martinez\nB) Toby Flenderson\nC) Meredith Palmer\nD) Phyllis Vance",
                "answer": "B"
            }
        ]
        
        self.score = 0  

    def questions(self):
        # Loop through the questions
        for q in self.question_list:
            print(q["question"])  # Display the question
            print(q["options"])  # Display the options
            user_answer = input("Your answer (A, B, C, or D): ").upper()
            # Check for valid input
            if user_answer not in ['A', 'B', 'C', 'D']:
                print("Invalid Input! Please enter A, B, C, or D.\n")
                continue  # Skip to the next iteration, don't count this answer

            # Check if the answer is correct
            if user_answer == q["answer"]:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.\n")

        # Final score
        print(f"Quiz finished! Your score: {self.score}/{len(self.question_list)}")
        if self.score < 5:
            print(f'You are a loser {self.name}.')
        else:
            print(f'Congratulations {self.name}, you passed!')

