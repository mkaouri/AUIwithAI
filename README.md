# Enhancing User Experience with AI-Driven Adaptive User Interfaces
This solution uses AUI with AI in an LLM-enabled chatbot by offering quick access from a list of dynamically ranked buttons as the most frequent starting point based on the user's previous prompt.
For a simple implementation, I used a pre-trained model like sentence-transformers to find the semantic similarity between the prompt and the potential button actions. The most semantically similar buttons to the prompt can then be prioritized from highest to lowest. I created a simple chatbot interface in Python using a library like Gradio for the user interface and Hugging Face's LLM models to process user prompts. Then, I used NLP techniques to prioritize the buttons based on the input prompt dynamically.
## Features:
1.	Display Default Button Order: Initially, the buttons are displayed in the default order.
2.	Sort Buttons After Prompt: Once a prompt is entered, the AI will reorder the buttons based on the context.
3.	Display Button Label in Prompt: When a button is clicked, previous prompt will be cleared and the button label will be displayed in the prompt input.
## Steps on how to do it:
1.	Use Sentence Embeddings: Convert both the user prompt and the button actions into sentence embeddings.
2.	Calculate Similarity: Use cosine similarity to rank the actions based on how similar they are to the user prompt.
3.	Prioritize the Buttons: Sort the buttons by similarity and display them accordingly.
## How this works:
1.	Sentence Transformer Model: The all-MiniLM-L6-v2 model from Hugging Face is used to convert both the user’s prompt and the predefined button labels into embeddings.
2.	Cosine Similarity: The cosine similarity between the prompt embedding and the button embeddings is calculated. This gives a measure of how similar the user's prompt is to each of the buttons' actions.
3.	Ranking: The buttons are sorted based on their similarity to the prompt, and those with higher similarity are prioritized.
4.	Gradio Interface: The UI is built using Gradio, which allows for an input box, response area, and dynamically updated buttons based on user input.
## Example workflow:
•	If the user inputs something like "I want to write some code," the buttons like "Code" and "Help me write" would be ranked higher.
•	If the user enters something like "Summarize this text," the button "Summarize text" would be prioritized.
## Install required libraries:
pip install gradio transformers sentence-transformers
## Python code: 
Run the Code on the local command prompt:
I used Anaconda Powershell Prompt to troubleshoot the code execution instead of Google Colab because I encountered an unknown issue while running it. Navigate to the location of the Code and run: 
python app.py
After successfully receiving the URL on the terminal, navigate it on an internet browser like Chrome or Edge. Example URL: http://127.0.0.1:7860
## Final result:
At the launch of the Python code, a Gradio web interface is displayed. The list of buttons is sorted by default in the following order: Analyze data, Get advice, Make a plan, Summarize text, Help me write, Code. 
