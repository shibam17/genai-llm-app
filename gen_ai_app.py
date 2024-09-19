import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
def load_model():
    print("Loading model...")
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

# Generate text based on user input
def generate_text(prompt, model, tokenizer, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, do_sample=True)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

if __name__ == "__main__":
    model, tokenizer = load_model()
    user_input = input("Enter a prompt: ")
    response = generate_text(user_input, model, tokenizer)
    print("\nGenerated Text:\n")
    print(response)
