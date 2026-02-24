import ollama 

#print response
response= ollama.list()
print(response)

#chat example
res=ollama.chat(
    model="jerry",
    messages=[
        {
            "role":"user",
            "content":"why is the sky blue"
        },
    ],
    stream=True,
)
# print(res["messages"]["content"])


#generate
res=ollama.generate(
model="llama3:8b",
prompt="Why is Sky Blue?",
)

#show 
print(ollama.show("llama3:8b"))

