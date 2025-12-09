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
    # Construct a prompt to get the high-level plan
    prompt = f"Create a travel theme and a list of 5-7 top attractions for a {budget} trip to {destination}. Return ONLY the theme and the list."

    # Call the local model via Ollama
    response = ollama.chat(
        model=MODEL_NAME, messages=[{"role": "user", "content": prompt}]
    )

    # CRITICAL: This line must be indented exactly like this
    return response["message"]["content"]


# Define the function to generate a specific day's plan using context from previous steps
def generate_daily_plan(day, destination, budget, attractions, previous_day_plan):
    # Refined prompt to force a schedule format
    prompt = f"""
    Context: {attractions}
    Previous Day: {previous_day_plan}
    Task: Create a detailed itinerary for Day {day} in {destination}.
    Format:
    - Morning: [Activity]
    - Afternoon: [Activity]
    - Evening: [Activity]
    Constraint: Do NOT repeat activities from the Previous Day.
    """

    response = ollama.chat(
        model=MODEL_NAME, messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# STEP 5: Execution & File Save
output_filename = f"Itinerary_{destination}_{num_days}_Days.txt"

with open(output_filename, "w", encoding="utf-8") as file:
    # Helper function to print to screen AND write to file
    def save_and_print(text):
        print(text)
        file.write(text + "\n")

    save_and_print(f"--- Generating Itinerary for {destination} ---")

    # Generate Theme
    theme_data = generate_theme_and_attractions(destination, budget)
    save_and_print(f"\n[Theme & Overview]:\n{theme_data}\n")

    previous_day_plan = "Start of trip"

    # Loop through days
    for day in range(1, num_days + 1):
        save_and_print(f"--- Planning Day {day} ---")
        daily_plan = generate_daily_plan(
            day, destination, budget, theme_data, previous_day_plan
        )
        save_and_print(daily_plan + "\n")
        previous_day_plan = daily_plan  # Update context

    print(f"\n✅ Itinerary successfully saved to: {output_filename}")
