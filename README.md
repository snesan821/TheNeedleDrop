# VinylScout AI Agent
**An Intelligent Market Intelligence Tool for Vinyl Collectors & Investors**

VinylScout is a containerized backend service that automates the identification of high-value vinyl records. By combining real-time market data with generative AI, it provides collectors with actionable insights into record rarity and investment potential.

##  The Tech Stack
* **Language:** Python 3.11
* **Framework:** FastAPI (Asynchronous API)
* **AI Engine:** Google Gemini 2.0 (Analysis & Market Sentiment)
* **Data Source:** Discogs API (Market Pricing & Metadata)
* **DevOps:** Docker (Containerization)
* **Cloud Infrastructure:** AWS (ECR, ECS/Fargate), CloudWatch (Monitoring)

##  Architecture
VinylScout operates as a microservice. It receives a search query, fetches technical metadata and historical pricing from Discogs, and then feeds that data into a specialized Gemini AI prompt to determine if a record is a "Buy," "Hold," or "Pass."

##  Local Setup & Containerization
1. **Clone the repo:** `git clone https://github.com/snesan821/TheNeedleDrop.git`
2. **Setup Env:** Create a `.env` with `DISCOGS_KEY` and `GEMINI_API_KEY`.
3. **Build Container:** `docker build -t vinyl-scout .`
4. **Run:** `docker run -p 8000:8000 --env-file .env vinyl-scout`