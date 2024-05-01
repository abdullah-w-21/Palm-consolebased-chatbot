# Palm-consolebased-chatbot
Simple Palmai console based chatbot.


## Chatbot using Google's Palm API

This is a simple chatbot script that interacts with users using Google's Palm API. The Palm API is a Generative AI model developed by Google for natural language processing tasks.

### Usage

1. **Initialization**: The script initializes the Palm API by configuring it with the required API key.
   
   import google.generativeai as palm

   palm.configure(api_key="")

   
2. **Model Selection**: The script selects a specific model for generating text. In this case, it uses the "text-bison-001" model.

   model_id = "models/text-bison-001"

3. **Chat Loop**: The script enters a loop where it continuously interacts with the user until the user decides to exit.

   x = "y"
   while(x=="y"):

4. **User Input**: The user is prompted to enter a query.

   prompt = input("Enter your query:")

5. **Text Generation**: The script generates a text response using the selected model and the user's query as input.

   completion = palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
    )

6. **Output**: The generated text response is printed to the console.

   print(completion.result)


### Example

Enter your query: How are you?
Response: I'm doing well, thank you!

do you want to ask another question: y or n y
Enter your query: What is the weather today?
Response: The weather today is sunny.

do you want to ask another question: y or n n
bye!!


