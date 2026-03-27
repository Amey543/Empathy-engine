# 🎭 The Empathy Engine

> **🎥 Watch the Demo:** [Insert Link to your Loom/YouTube video here]
> 
> *Note: Because this service taps into the host machine's native Text-to-Speech (TTS) drivers, it is currently configured to run on `localhost`. Watch the video above to see it in action!*

The **Empathy Engine** is a lightweight, local web application that dynamically modulates the vocal characteristics of synthesized speech based on the detected emotional sentiment of the source text. It bridges the gap between text-based sentiment and expressive audio output, moving beyond monotonic delivery.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI
* **Frontend:** Vanilla HTML, CSS, JavaScript (Fetch API)
* **Intelligence:** TextBlob (Lexicon-based sentiment analysis)
* **Audio Synthesis:** `pyttsx3` (Offline Text-to-Speech)

---

## 📂 Project Structure

This project follows a clean, decoupled architecture:

```text
empathy-engine/
├── backend/                  # 🧠 The Server & Logic
│   ├── __init__.py           # Marks the directory as a Python package
│   ├── main.py               # FastAPI application routing and static file mounting
│   ├── engine.py             # Core NLP sentiment analysis and TTS processing logic
│   └── requirements.txt      # Python dependencies
├── frontend/                 # 🎨 The Client Interface
│   └── index.html            # The UI and inline JavaScript to communicate with the API
├── config.yaml       # ⚙️ Configuration template for directory paths
└── .gitignore                # Keeps the repository clean of virtual environments and media files
```
## 🚀 How to Run Locally

Follow these steps to spin up the Empathy Engine on your own machine.

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Clone the Repository
```bash
git clone [https://github.com/Amey543/Empathy-engine.git](https://github.com/Amey543/Empathy-engine.git)
cd Empathy-engine
```
