# SlopSlayer Live
**Real-Time Gen-Z Deepfake & AI Slop Buster**
*Built for the Gemini Live Agent Challenge 2026*

## The Problem
In 2026, the internet is flooded with "AI Slop"—deepfakes, synthetic voices, and misleading synthetic content. Gen-Z, the heaviest users of social media, are targeted by election misinformation, digital bullying, and "truth fatigue."

## The Solution
**SlopSlayer Live** is a conversational AI agent that lives in your pocket. Using the **Gemini Multimodal Live API**, it acts as a real-time critical thinking coach.
- **See:** Point your camera at any screen (TikTok, IG, X).
- **Hear:** Analyze synthetic speech and tone.
- **Speak:** A witty, protective Gen-Z "big sibling" persona roasts the slop and teaches the user how to spot it.

## Technical Architecture
- **Model:** Gemini 2.5 Flash (via Vertex AI)
- **Real-time Stream:** Multimodal Live API (WebSockets)
- **Grounding:** Vertex AI Search (RAG) integrated with Google Search for real-time fact-checking.
- **Deployment:** Google Cloud Run (Containerized)

## Installation & Spin-up
1.  **Clone the repo:** `git clone https://github.com/bentheaya/SlopSlayer.git`
2.  **Setup Environment:** Create a `.env` file with your `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`.
3.  **Install Dependencies:** `pip install -r requirements.txt`
4.  **Run Local:** `python app/main.py`

## Web UI Access
- **Developer UI**: [http://localhost:8080/dev-ui](http://localhost:8080/dev-ui)
- **Base URL**: [http://localhost:8080](http://localhost:8080)

## Deployment to Google Cloud Run

To deploy SlopSlayer to the cloud:

1.  **Build the Container**:
    ```bash
    gcloud builds submit --tag gcr.io/[PROJECT_ID]/slopslayer
    ```
2.  **Deploy to Cloud Run**:
    ```bash
    gcloud run deploy slopslayer \
      --image gcr.io/[PROJECT_ID]/slopslayer \
      --platform managed \
      --allow-unauthenticated \
      --set-env-vars="GOOGLE_CLOUD_PROJECT=[PROJECT_ID],GOOGLE_CLOUD_LOCATION=us-central1,GOOGLE_GENAI_USE_VERTEXAI=True"
    ```
3.  **Access the URL**: Cloud Run will provide a `.a.run.app` URL. Append `/dev-ui` to access the interface.

> [!NOTE]
> Ensure your Google Cloud Project has the **Vertex AI API** enabled.

## Innovation Points
- **Two-Tier Grounding:** Combines visual artifact detection with real-time fact-check retrieval.
- **Barge-In Ready:** Optimized for natural interruptions and gasps.
- **Digital Literacy:** Doesn't just "detect"; it *teaches* the user.
