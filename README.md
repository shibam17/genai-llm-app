# Custom GenAI LLM Application

## Overview
This is a simple application that uses a pre-trained GPT-2 model from Hugging Face to generate text based on user input.

## Setup

### 1. Clone this repository:

```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 2. Install dependencies:

```bash
pip install transformers
```

### 3. Run the application:

```bash
python gen_ai_app.py
```

## How It Works
- The script loads a GPT-2 model and tokenizer.
- You provide a text prompt, and the model generates a continuation of the prompt using GPT-2.

## Example
```
$ python gen_ai_app.py
Enter a prompt: Once upon a time,  
Generated Text:  
Once upon a time, in a land far away, there was a kingdom ruled by a wise and kind king...
```




### 3. Git Commands
These commands don't go into any specific file but are to be executed in the terminal to push your project to GitHub:

1. Initialize the repository and make the first commit:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Push to a remote GitHub repository:
   ```bash
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
