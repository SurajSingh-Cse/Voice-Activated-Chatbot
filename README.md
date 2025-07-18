# VOICE ACTIVATED AI CHATBOT

A Python-based voice assistant inspired by J.A.R.V.I.S. from Iron Man. It responds to voice commands and performs actions like playing music, opening apps, searching Google/Wikipedia, taking notes, and even asking questions to OpenAI's GPT.

## 🚀 Features

- 🎤 Voice Recognition (SpeechRecognition)
- 🗣️ Text-to-Speech (pyttsx3)
- 🔍 Wikipedia & Google search
- 🎵 Play music from your system
- 📂 Open apps/websites
- 📝 Write & read notes
- ✅ To-do manager
- 🤖 Ask OpenAI questions using GPT

## 📦 Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt


```
## How to Run
```
Main file.py
```
Make sure your microphone and internet are working properly.

## Project Structure

main file.py
openai_request.py
user_config.env
requirements.txt
README.md

## Voice Commands Examples
"play music"

"say time"

"open youtube"

"search google who is Elon Musk"

"wikipedia artificial intelligence"

"new task buy groceries"

"read note"

"exit"

## Author
```
-Suraj Singh
-LinkedIn:www.linkedin.com/in/singh-suraj-negi
-GitHub: https://github.com/SurajSingh-Cse/Voice-Activated-Chatbot

```


---

## ⚙️ Setup Instructions

### ✅ Prerequisites
---
- Python 3.8+
- A working microphone
- Works best on **Windows** (due to TTS engine and COM support)
---
### 🧪 Install Required Packages

```
pip install -r requirements.txt
```

##Set OpenAI API Key (Optional - For GPT feature)
```
Create a .env file in the project folder.
```
# Add this line:
```
OPENAI_API_KEY=your_openai_api_key_here
```

##  Screenshots
<img width="1920" height="1080" alt="screenshot" src="https://github.com/user-attachments/assets/11d9ca3b-cfa2-4042-a798-e78b54a24fe3" />

## Voice Commands Supported
~~~
Category            Example Commands
Greetings	        "hello jarvis", "good morning"
Music	            "play music"
Time            	"say time", "what is the time"
Notes/Tasks	      "write a note", "read note", "new task"
Web              	"open youtube", "search google", "wikipedia"
System Control	  "shutdown", "restart", "lock screen"
AI	              "ask ai what is machine learning"
Exit            	"exit", "quit"
~~~
## 🧠 AI Integration
This project supports GPT interaction using OpenAI. You can ask it intelligent questions and get AI-generated answers via:
```
ask ai <your question>
```
## Tech Stack
pyttsx3

speech_recognition

pyautogui

plyer

wikipedia

pywhatkit

openai

comtypes

dotenv (for API key)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

 ## License
This project is licensed under the MIT License.
Feel free to use and modify it!


⭐ Don’t forget to give this repo a star if you like it!





