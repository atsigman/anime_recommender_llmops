# Anime Recommendation System App

## Installation:
### Local/Virtual Environment:
Run `pip install -r requirements.txt`

### Docker: 
A `Dockerfile` is included. Build the image via `docker build -t llmops-app:latest .` or using `docker-compose`

## Groq API Key and Huggingface Hub User API Access Token:
It will be necessary to create a Groq API key and a Huggingface Hub API token. These should be stored in a `.env` file in the project
root directory. 

Groq: https://console.groq.com/keys
Huggingface Hub: https://huggingface.co/settings/tokens

## Running the App:
From the project root directory, execute: `streamlit run app/app.py`
(If targeting a specific python version, run `python3.x -m streamlit run app/app.py`) 

