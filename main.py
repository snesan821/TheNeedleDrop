from fastapi import FastAPI
import discogs_client
import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. Load keys from the .env file
load_dotenv()

DISCOGS_TOKEN = os.getenv('DISCOGS_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_KEY')

# Safety Check: Stop if keys are missing
if not DISCOGS_TOKEN or not GEMINI_KEY:
    print("❌ ERROR: Keys not found in .env file.")
    print("Make sure your .env file looks like this:\nDISCOGS_TOKEN=abc...\nGEMINI_KEY=xyz...")
    exit()

# 2. Setup Clients
app = FastAPI()
d_client = discogs_client.Client('VinylScout/1.0', user_token=DISCOGS_TOKEN)
genai.configure(api_key=GEMINI_KEY)

# Using the latest available flash model
model = genai.GenerativeModel('gemini-2.5-flash')

@app.get("/")
def home():
    return {"status": "VinylScout AI is Online"}

@app.get("/scout/{artist_name}")
def scout_artist(artist_name: str):
    try:
        # --- DISC SCOUTING ---
        print(f"Scouting {artist_name}...")
        results = d_client.search(artist_name, type='artist')
        if not results:
            return {"error": "Artist not found"}
            
        artist = results[0]
        releases = artist.releases.page(1)[:5] # Get top 5
        
        market_data = []
        for r in releases:
            market_data.append(f"Title: {r.title}, Year: {r.year}, ID: {r.id}")
        
        # --- AI ANALYSIS ---
        print("Analyzing with Gemini...")
        prompt = f"""
        Act as a cynical music critic and vinyl investor.
        Review these 5 releases by {artist.name}:
        {market_data}
        
        Tell me which ONE is the best investment and why. Be brief.
        """
        
        response = model.generate_content(prompt)
        
        return {
            "artist": artist.name,
            "ai_analysis": response.text
        }

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)