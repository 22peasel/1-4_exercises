#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)   
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")
    
    

def process_scores(scores):
    # calculate average score
    score_total = 0
    for score in scores:
        score_total += score 
    scores = sorted(scores)
    low = scores[0]
    high = scores[len(scores) - 1]
    if len(scores) % 2 == 0:
        median = (scores[(len(scores) // 2) - 1] + scores[(len(scores) // 2)]) / 2 
    else:
        median = len(scores) // 2
    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", score_total / len(scores))
    print("Low score:         ", low)
    print("High Score:        ", high)
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

