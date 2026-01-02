import ollama

# create a new model with modelfile
modelfile = """
    FROM llama3.2:latest
    SYSTEM You are very smart assistant who knows everything about the oceans
    PARAMETER temperature 0.1
"""

# create a new Modelfile
ollama.create(
    model="knowitall",
    from_="llama3.2:latest",
    files={
        "Modelfile": modelfile
    }
)

# generate something
res = ollama.generate(model="knowitall", prompt="why is ocean so salty?")
print(res["response"])

# delete model
ollama.delete("knowitall")
