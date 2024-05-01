import google.generativeai as palm
palm.configure(api_key="")

model_id = "models/text-bison-001"

x = "y"
while(x=="y"):
    prompt = input("Enter your query:")
    completion = palm.generate_text(
        model=model_id,
        prompt=prompt,
        temperature=0.99,
        max_output_tokens=800,
    )
    print(completion.result)
    x = input("do you want to ask another question: y or n")
    if (x=="n"):
        print("bye!!")
