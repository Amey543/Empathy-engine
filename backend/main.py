from fastapi import FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles

from fastapi.responses import FileResponse

from pydantic import BaseModel

import os

import yaml



# Import our engine logic

from backend.engine import analyze_and_generate



# 1. Setup absolute paths

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

CONFIG_PATH = os.path.join(BASE_DIR, "config.yaml")



# 2. Load the YAML Configuration

try:

    with open(CONFIG_PATH, "r") as file:

        config = yaml.safe_load(file)

except FileNotFoundError:

    raise RuntimeError(f"Configuration file not found at {CONFIG_PATH}")



# 3. Extract the audio directory from the config and build the path

audio_folder_name = config.get("storage", {}).get("audio_export_dir", "generated_audio")

AUDIO_DIR = os.path.join(BASE_DIR, audio_folder_name)



# Ensure the audio storage directory exists

os.makedirs(AUDIO_DIR, exist_ok=True)



app = FastAPI(title="The Empathy Engine")



# Allow CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"],

)



# Mount the audio directory

app.mount("/audio", StaticFiles(directory=AUDIO_DIR), name="audio")



class TextPayload(BaseModel):

    text: str



@app.post("/process")

def process_text(payload: TextPayload):

    try:

        # We pass the dynamically loaded AUDIO_DIR to the engine

        emotion, filename = analyze_and_generate(payload.text, AUDIO_DIR)

        return {

            "status": "success",

            "emotion": emotion,

            "audio_url": f"/audio/{filename}"

        }

    except Exception as e:

        raise HTTPException(status_code=500, detail=str(e))



@app.get("/")

def serve_ui():

    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))