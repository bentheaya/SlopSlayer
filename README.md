# SlopSlayer Live
**Real-Time Gen-Z Deepfake & AI Slop Buster** *Built for the Gemini Live Agent Challenge 2026*

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
- **Grounding:** Vertex AI Search (RAG) integrated with Reuters & FactCheck.org APIs.
- **Frontend:** React + Vite (Tailwind CSS)
- **Backend:** Node.js / Cloud Run (Google Cloud)
- **Math Overlay:** Spatial Reasoning algorithms to detect geometric diffusion errors (Sixth-finger merges, non-Euclidean shadows).

## Installation & Spin-up
1. **Clone the repo:** `git clone https://github.com/bentheaya/SlopSlayer.git`
2. **Setup Environment:** Create a `.env` file with your `VITE_GCP_PROJECT_ID` and `VITE_GCP_LOCATION`.
3. **Install Dependencies:** `npm install`
4. **Run Local:** `npm run dev`
5. **Deploy to Cloud Run:** `gcloud run deploy --source .`

## Innovation Points
- **Two-Tier Grounding:** Combines visual artifact detection with real-time fact-check retrieval.
- **Barge-In Ready:** Optimized for natural interruptions and gasps.
- **Digital Literacy:** Doesn't just "detect"; it *teaches* the user.
