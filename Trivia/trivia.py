import random



# Dictionary storing questions (keys) and their correct answers (values)
questions = {
    "Who is the father of computer?" :	"Charles Babbage",
	"Who is the brain of computer?"	: "CPU",
	"What is the full form of CPU?":	"Central processing unit",
	"How many arrow keys are there in a keyboard?":	"4",
	"Which device that displays picture on its screen?"	: "Monitor",
	"What is the shortcut key of refreshing the computer?" :	"F5",
    "What is the full form of LCD?"	: "Liquid Crystal Display",
    }




def trivia_game():
    # Extract all question keys from the dictionary
    question_list = list(questions.keys())
    total_questions = 5
    
    # Randomly select a subset of questions
    question = random.sample(question_list, total_questions)
    
    score = 0 # Initialize player score
    
    #  Loop through each question with an index for numbering
    for index, ques in enumerate(question):
        print(f"{index + 1}. {ques}")
        user_answer = input("Enter your answer : ").lower().strip()
        correct_answer = questions[ques].lower() # this will store the answer for the questions in this variable

# Check if the user’s answer matches the correct one
        if user_answer == correct_answer :
            print("The Answer is correct\n")
            score += 1 
        else:
            print(f"Your Answer is wrong the correct answer is {correct_answer}\n")
   
    # Display the final score
    print(f"your score is {score}/{total_questions}")

if __name__=="__main__":

    trivia_game()
