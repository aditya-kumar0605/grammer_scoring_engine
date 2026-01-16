GRAMMAR SCORING ENGINE FROM VOICE SAMPLES
=======================================

PROJECT OVERVIEW
----------------
This project is a Grammar Scoring Engine that evaluates spoken English audio
and assigns a grammar score based on detected grammatical errors.

The system performs:
1. Speech-to-text transcription using OpenAI Whisper
2. Grammar analysis using LanguageTool
3. Grammar scoring logic (1–10 scale)
4. Interactive user interface using Streamlit

This project was developed as part of a Research Intern / AI assessment task.


ARCHITECTURE
------------
Audio File (.wav / .mp3)
        ↓
Whisper (Speech-to-Text)
        ↓
Text Cleaning
        ↓
LanguageTool (Grammar Checking)
        ↓
Grammar Score + Error Count
        ↓
Streamlit UI


PROJECT STRUCTURE
-----------------
grammer_scoring_engine/
│
├── app.py
├── src/
│   ├── transcribe.py
│   ├── grammar_score.py
│   └── preprocess.py
│
├── requirements.txt
├── README.txt
└── venv/   (not shared)


REQUIREMENTS
------------
- Python 3.10 or 3.11 (recommended)
- FFmpeg (required for audio processing)
- Java 17 or higher (required by LanguageTool)
- Operating System: Windows / Linux / macOS


SETUP INSTRUCTIONS
------------------

1. Clone or download the project
   git clone <repository_url>
   cd grammer_scoring_engine

2. Create a virtual environment
   python -m venv venv

3. Activate the virtual environment

   Windows:
   venv\Scripts\activate

   Linux / macOS:
   source venv/bin/activate

4. Install Python dependencies
   pip install -r requirements.txt

5. Install FFmpeg
   Download from:
   https://www.gyan.dev/ffmpeg/builds/

   Extract the files and ensure ffmpeg is accessible.

6. Install Java
   Install Java version 17 or higher.
   Verify with:
   java -version

7. Run the application
   streamlit run app.py

   The application will open in your browser at:
   http://localhost:8501


FEATURES
--------
- Upload English audio files (.wav / .mp3)
- Automatic speech transcription
- Grammar error detection
- Grammar score generation (1–10)
- Error count with feedback
- Clean and interactive Streamlit UI


SCORING LOGIC
-------------
Grammar Errors     Score
0                  10
1                  9
2–3                7–8
4–5                5–6
6+                 1–4


SAMPLE OUTPUT
-------------
Grammar Score: 7 / 10
Errors Found: 3
Feedback: Average grammar, some improvements needed


DESIGN DECISIONS
----------------
- Whisper is used for robust speech recognition.
- LanguageTool provides explainable grammar feedback.
- Virtual environments ensure dependency isolation.
- Explicit FFmpeg handling improves Windows compatibility.


FUTURE IMPROVEMENTS
-------------------
- Fluency and pronunciation scoring
- Grammar error highlighting in text
- ML-based grammar scoring models
- Cloud deployment


AUTHOR
------
Aditya Kumar
Computer Science Graduate
Skills: Python, Data Engineering, AI Automation


NOTES
-----
- The virtual environment (venv) is not shared.
- Users must install dependencies locally.
- Tested successfully on Windows systems.

