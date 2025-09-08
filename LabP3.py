import random
def calculate_probability(fav_outxomes,total_outcomes):
    return fav_outxomes/total_outcomes if total_outcomes!=0 else 0

def get_sample_space(choice):
    if choice == "1":
        
        return [str(i) for i in range(1, 7)], "Dice roll (1-6)"
    elif choice == "2":
        return ["Heads", "Tails"], "Coin toss"
    elif choice == "3":
        # Deck of cards simplified to suits
        return ["Hearts", "Diamonds", "Clubs", "Spades"], "Card suits"
    elif choice == "4":
        return ["0", "1"], "Binary outcomes (0,1)"
    elif choice == "5":
        raw = input("Enter your custom sample space (comma-separated): ")
        custom_space = [item.strip() for item in raw.split(',') if item.strip()]
        return custom_space, "Custom sample space"
    else:
        return None, None
def main():
    print("Multi-sample Probability Calculation")

    print("Choose a sample space:")
    print("  1) Dice roll (1-6)")
    print("  2) Coin toss (Heads, Tails)")
    print("  3) Card suits (Hearts, Diamonds, Clubs, Spades)")
    print("  4) Binary outcomes (0,1)")
    print("  5) Enter custom sample space")
    
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        sample_space, description = get_sample_space(choice)
        if sample_space:
            break
        print("Invalid choice, please try again.")

    total_outcomes = len(sample_space)
    print(f"\nSample Space Selected: {description}")
    print(f"Sample Space (S): {sample_space}")
    print(f"Total outcomes (n(S)): {total_outcomes}\n")

    num_events = int(input("How many events do you want to define? "))
    events = {}

    for i in range(1, num_events + 1):
        event_name = input(f"\nEnter name for Event #{i} (e.g., A, B, Even): ").strip()
        raw_event = input(f"Enter the outcomes for Event {event_name} (comma-separated): ")
        event_outcomes = [item.strip() for item in raw_event.split(',') if item.strip() in sample_space]
        if not event_outcomes:
            print(f"Warning: No valid outcomes matched the sample space for event {event_name}.")
        events[event_name] = event_outcomes

    print("\nEvent Probabilities:")
    for name, outcomes in events.items():
        favorable = len(outcomes)
        probability = calculate_probability(favorable, total_outcomes)
        print(f"  Event {name}: {outcomes}")
        print(f"   n(E_{name}) = {favorable}, P(E_{name}) = {favorable}/{total_outcomes} = {probability:.2f}")

    simulate = input("\nDo you want to simulate these events? (yes/no): ").strip().lower()
    if simulate in ['yes', 'y']:
        trials = int(input("Number of trials to simulate: "))
        print("\nResults:")
        for name, outcomes in events.items():
            count = 0
            for _ in range(trials):
                outcome = random.choice(sample_space)
                if outcome in outcomes:
                    count += 1
            estimated_prob = count / trials
            print(f"  Event {name}: Estimated P ≈ {estimated_prob:.2f} over {trials} trials")

if __name__ == "__main__":
    main()
