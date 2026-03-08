# OpenRouter Python Examples

Example project based on the Real Python tutorial  
"How to Use the OpenRouter API to Access Multiple AI Models via Python".

https://realpython.com/openrouter-api/

This project demonstrates how to access multiple AI providers through the OpenRouter API using Python.

## Features

- Connect to OpenRouter API
- Retrieve available models
- Send prompts to AI models
- Automatically route requests to providers
- Implement model fallbacks for reliability

## Requirements

- Python 3.9+
- OpenRouter API Key

## Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/openrouter-python-demo.git
cd openrouter-python-demo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Git

git init
git add .
git commit -m "Initial commit: OpenRouter Python examples"
git remote add origin https://github.com/YOUR_USERNAME/openrouter-python-demo.git
git branch -M main
git push -u origin main

git status
git add .
git commit -m "Update README documentation"
git push