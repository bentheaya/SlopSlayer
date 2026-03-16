# SlopSlayer Live: Project Overview

## What We Built
We built a real-time, interactive **Gen-Z AI Bestie** named **SlopSlayer**. The agent is designed to use a live video and audio feed from your phone's camera to visually analyze short-form content (like TikToks, Reels, or Tweets), spot AI-generated artifacts (like weird geometry, missing shadows, or messed up hands), and verbally "roast" the deepfake or slop, while using a grounded fact-checking tool to verify claims.

It was built using the experimental **Google Agent Development Kit (ADK)** and the **Gemini 2.5 Flash Native Audio** model via the **Vertex AI Live API**.

---

## Technical Architecture & Setup

### 1. The Core AI Agent (`app/slopslayer/agent.py`)
This is the "brain" of SlopSlayer. 
- **Model**: `gemini-live-2.5-flash-native-audio` (A special Vertex AI model optimized for low-latency, bidirectional audio, and video streaming).
- **System Instructions**: We gave the agent a strict persona. It must speak with 2026 Gen-Z slang, respond in very short, punchy 15-second sentences, and follow a two-tier verification system:
  1. **Visual Analysis**: Look at the camera feed first to spot visual anomalies.
  2. **Fact Check**: If a claim is made, use the `google_search` tool to prove whether it's real or slop before confirming it to the user.
- **Live Mode Forcing**: We explicitly passed `generate_content_config={"response_modalities": ["AUDIO"]}` into the ADK Agent setup. This forces the framework to load the WebRTC Audio/Video interface instead of reverting to a standard text chatbot.

### 2. The ADK Web Server & Mobile Optimizations (`index.html` injections)
The ADK framework provides a pre-built web interface for testing agents locally. However, this interface was not optimized for the SlopSlayer use-case (a mobile user pointing their phone at a screen). We "hacked" the underlying frontend source code (`site-packages/google/adk/cli/browser/index.html`) to make it work beautifully on your phone:
- **Mobile Responsive CSS**: Shrank the margins and contained the video element so it fits comfortably on a mobile screen without horizontal scrolling.
- **Camera Switching**: Wrote a custom JavaScript interceptor for `navigator.mediaDevices.getUserMedia` that captures the browser's camera requests. We added a floating **"🔄 Switch Camera"** button that lets you toggle between the front "selfie" camera (to talk to the agent) and the back "environment" camera (to point at slop on a laptop/TV).
- **Disabling Text Input**: We added a CSS rule to hide the text-chat `textarea`. Why? Because the Live Voice model crashes (`400 INVALID_ARGUMENT`) if it receives standard REST API text messages instead of WebSocket streams. This guarantees the user only interacts naturally via voice.

### 3. Networking, Tunnels, and WebRTC
A massive challenge was getting a Live WebRTC Audio/Video stream (which requires HTTPS and strict security) to run from your local Windows dev server (`127.0.0.1:8000`) securely to your mobile phone over the public internet.
- **The LocalTunnel Failure**: Our first attempt used `localtunnel`, but it was highly unstable. It kept randomly dropping our long-lived WebSocket connections, causing the SlopSlayer stream to freeze and die after 10-15 seconds.
- **The Ngrok Success**: We switched to **Ngrok**. We authenticated your account, bound the tunnel to `0.0.0.0:8000`, and instantly gained an incredibly stable, low-latency HTTPS tunnel that reliably supports bidirectional streaming media.

---

## How It All Connects (The Flow)
1. You open the `ngrok` link on your phone.
2. The ADK Dev UI loads (with our mobile hacks) and asks for Microphone and Camera permissions.
3. Once granted, a secure **WebSocket** connects to your laptop's Python ADK server.
4. Your phone begins streaming raw video frames and audio chunks into the `gemini-live-2.5-flash-native-audio` model on Vertex AI.
5. SlopSlayer watches the stream. If you hold up a fake TikTok and gasp "Wait, is this real?", the model interprets the audio, analyzes the current frame of video, checks Google if necessary, and streams synthetic voice audio back down the WebSocket to speakers instantly.
