import os
import logging
import uvicorn
import certifi
from dotenv import load_dotenv

# Set SSL_CERT_FILE for WebRTC/Live API BEFORE loading anything else
os.environ["SSL_CERT_FILE"] = certifi.where()

# Load environment variables from .env
load_dotenv()

from google.adk.cli.fast_api import get_fast_api_app

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app/slopslayer.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('slopslayer.main')

def main():
    try:
        host = os.environ.get("HOST", "0.0.0.0")
        port = int(os.environ.get("PORT", 8080))
        
        logger.info(f"Starting SlopSlayer Web Server on http://{host}:{port}...")
        
        # Get the ADK FastAPI app
        # 'app' directory contains the 'slopslayer' agent folder
        app = get_fast_api_app(
            agents_dir="app",
            web=True,
            host=host,
            port=port
        )
        
        logger.info("Access the Developer UI at http://localhost:8000/dev-ui")
        
        # Start uvicorn
        uvicorn.run(app, host=host, port=port, log_level="info")
        
    except Exception as e:
        logger.error(f"Failed to start server: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
