import ollama

# list all of the installed models
response = ollama.list()
#print(response)

# Chat example
res = ollama.generate(
    model= "llama3.2:latest",
    prompt="Why is the sky blue?"
)

print(ollama.show("llama3.2:latest"))

