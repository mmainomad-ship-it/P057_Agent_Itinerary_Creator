import ollama  # Import the interface for the local Ollama instance

# STEP 1: Configuration
# We define the model name here. Ensure you have run `ollama pull llama3` previously.
MODEL_NAME = "llama3"

# STEP 2: User Inputs
# Collect key constraints from the user to guide the generation
destination = input("Where are you traveling? ")
num_days = int(input("How many days is the trip? "))
budget = input("What is your budget (e.g., mid-range, luxury)? ")


# STEP 3: Function Definitions
# Define the function to generate the overall theme and list of attractions
def generate_theme_and_attractions(destination, budget):
    pass  # Body to be added in Step 4


# Define the function to generate a specific day's plan using context from previous steps
def generate_daily_plan(day, destination, budget, attractions, previous_day_plan):
    pass  # Body to be added in Step 4
    # STEP 4.1: Theme Generation Logic
    # Construct a prompt to get the high-level plan
    prompt = f"Create a travel theme and a list of 5-7 top attractions for a {budget} trip to {destination}. Return ONLY the theme and the list."

    # Call the local model via Ollama
    response = ollama.chat(
        model=MODEL_NAME, messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]
    # STEP 4.2: Daily Plan Logic with State Awareness
    # We include previous_day_plan in the prompt so the model remembers context
    prompt = f"Plan Day {day} in {destination} ({budget}). Focus on these attractions: {attractions}. Previous context: {previous_day_plan}. Create a detailed schedule."

    response = ollama.chat(
        model=MODEL_NAME, messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# STEP 5: Execution Loop
print("\n--- Generatating Itinerary... ---")

# First, get the high-level theme
theme_data = generate_theme_and_attractions(destination, budget)
print(f"\n[Theme & Overview]:\n{theme_data}\n")

# Initialize state variable
previous_day_plan = "Start of trip"

# Loop through each day
for day in range(1, num_days + 1):
    print(f"--- Planning Day {day} ---")
    # Pass 'previous_day_plan' to maintain continuity
    daily_plan = generate_daily_plan(
        day, destination, budget, theme_data, previous_day_plan
    )
    print(daily_plan + "\n")
    previous_day_plan = daily_plan  # Update history for the next loop
