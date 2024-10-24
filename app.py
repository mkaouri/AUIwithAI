import gradio as gr
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load Hugging Face model for text generation
llm = pipeline("text-generation", model="gpt2")

# Load sentence transformer model for similarity calculations
sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

# List of buttons (actions)
actions = ["Analyze data", "Get advice", "Make a plan", 
           "Summarize text", "Help me write", "Code"]

# Global variable to hold the current prioritized actions
prioritized_actions = actions.copy()

# Function to prioritize buttons based on similarity to prompt or chatbot response
def prioritize_buttons(text):
    # Encode the prompt or chatbot response
    text_embedding = sentence_model.encode(text, convert_to_tensor=True)
    
    # Encode all action buttons
    action_embeddings = sentence_model.encode(actions, convert_to_tensor=True)
    
    # Calculate cosine similarity between the prompt and each action
    similarities = util.pytorch_cos_sim(text_embedding, action_embeddings)[0]
    
    # Rank the actions based on similarity (highest similarity first)
    ranked_indices = np.argsort(-similarities)  # Sort in descending order
    
    # Reorder the buttons based on similarity ranking
    global prioritized_actions
    prioritized_actions = [actions[i] for i in ranked_indices]
    
    return prioritized_actions

# Function to generate a response and prioritize buttons
def chatbot_interface(prompt):
    try:
        # Generate a response from the LLM
        response = llm(prompt)[0]['generated_text']
    except Exception as e:
        response = f"Error: {str(e)}"
    
    # Prioritize buttons based on the prompt or the chatbot response
    priorities = prioritize_buttons(prompt)
    
    # Create the updates for the buttons
    button_updates = [gr.update(visible=True, value=action) for action in priorities]
    
    return [response] + button_updates

# Function to handle button click, clear prompt_input, and display sorted button label
def button_click(index, current_prompt):
    # Clear the input and add the new label from the sorted button list
    new_prompt = prioritized_actions[index]  # Get the label from the new sorted order
    return new_prompt

# Create the Gradio Interface
with gr.Blocks() as demo:
    # Input box for user prompt
    prompt_input = gr.Textbox(label="Enter your prompt")
    
    # Output for the chatbot response
    chatbot_output = gr.Textbox(label="Chatbot response")
    
    # Buttons for suggested actions, placed in a horizontal layout
    with gr.Row():  # Wrapping buttons in a Row to display them horizontally
        button_list = []
        for idx, action in enumerate(actions):
            button = gr.Button(action, visible=True)
            button.click(button_click, inputs=[gr.State(idx), prompt_input], outputs=prompt_input)
            button_list.append(button)

    # Update chatbot response and buttons when prompt is submitted
    prompt_input.submit(chatbot_interface, inputs=prompt_input, outputs=[chatbot_output] + button_list)

# Launch the app
demo.launch()
