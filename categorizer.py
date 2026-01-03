import ollama
import os

model = "llama3.2:latest"

# Paths to input and output files
input_file = "./data/grocery_list.txt"
output_file = "./data/categorized_grocery_list.txt"

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"Input file: '{input_file}' not found!")
    exit(1)

# Read the uncategorized gorocery items form the input file
with open(input_file, "r") as f:
    items = f.read().strip()

# Prepare the prompt form the model
prompt = f"""
You are an assistant that categorizes and sorts groceries.
Here's a list of grocery items:
{items}
Please:
1. Categorize this items into appropriate categories such as Produce, Dairy, Meat, Bakery, Beverages
2. Sort the items alphabetically within each category
3. Present the categoroized list in a clear and organized manner, using bullet points or numbering
"""

# set the prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response","")
    print("----------------CATEGORIZED LIST--------------------\n")
    print(generated_text)
    # write the organized list to the output file
    with open(output_file, "w") as f:
        f.write(generated_text.strip())
    print(f"Categorized list has benn saved to {output_file}.")
except Exception as e:
    print("An error has occured", str(e))
