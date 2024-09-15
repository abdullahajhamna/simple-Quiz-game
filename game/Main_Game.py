from game import documentation
from game import countdown
from questions import Start 
from questions import Question

def main():
    # Create an instance of the Start class with parentheses
    s = Start()  # This line is crucial; it must include parentheses
    # Call the start method on the instance
    s.start()  # This will now correctly invoke the method on the instance
    documentation()
    countdown()
    # Instantiate the Question class
    quiz = Question()  # Create an instance of Question
    # Call the questions method on the instance
    quiz.questions()  # Now this works correctly, as it's called on an instance

if __name__ == "__main__":
    main()

