# 🗺️ Project 57: Agent: Travel Itinerary Creator

## 📝 Description
An intelligent AI agent capable of generating structured, multi-day travel itineraries. The agent uses iterative chaining to ensure logical flow, generating a high-level theme first, followed by detailed day-by-day plans that respect budget and time constraints without repetition.

## ✨ Key Features
* **Iterative Planning:** Break down complex tasks into theme generation and daily scheduling.
* **State Management:** Passes context (previous day's plan) to the next step to ensure continuity.
* **Constraint Handling:** Respects user budget and time duration.
* **Local Privacy:** Runs entirely offline using local LLMs.

## 🛠️ Technology Stack
* **Language:** Python
* **AI Model:** Llama 3 (via Ollama)
* **Hardware:** Local GPU (RTX 3090)

## 🚀 Setup Instructions
1.  Clone the repository.
2.  Create a virtual environment: `python -m venv venv`
3.  Install dependencies: `pip install -r requirements.txt`
4.  Ensure Ollama is running (`ollama serve`).
5.  Run the agent: `python itinerary_agent.py`

## 👨‍💻 Author
**mmainomad-ship-it**
[GitHub Profile](https://github.com/mmainomad-ship-it)