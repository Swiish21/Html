def main():
    candidates = ["mike", "kevin", "mercy"]
    votes = {candidate: 0 for candidate in candidates}

    print("Welcome to our voting program!")
    print("here are the candidates:")
    for candidate in candidates:
        print(candidate)
    
    while True:
        vote = input("Please input the name of the candidate you want to vote for (or type 'done' to finish): ")
        if vote.lower() == 'done':
            break
        elif vote in votes:
            votes[vote] += 1
            print("Thank you for your vote!")
        else:
            print("Invalid candidate. Please try again.")

    print("\nVoting Results: ")
    for candidate, num_votes in votes.items():
        print(f"{candidate}: {num_votes} votes")

if __name__ == "__main__":
    main()
    