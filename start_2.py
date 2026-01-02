import ollama

# list all of the installed models
response = ollama.list()
#print(response)

# Chat example
res = ollama.chat(
    model= "llama3.2:latest",
    messages=[
        {"role": "user", "content": "Why is the sky blue?"}
    ]
)

# print the response
#print(res)

# print only content
print(res["message"]["content"])
