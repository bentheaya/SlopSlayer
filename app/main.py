import os
import logging
from datetime import datetime
from dotenv import load_dotenv
from slopslayer.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService

# Load environment variables from .env
load_dotenv()

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
        logger.info("Starting SlopSlayer Agent...")
        
        # Initialize Runner with default in-memory session service
        session_service = InMemorySessionService()
        runner = Runner(
            app_name="SlopSlayer",
            agent=root_agent,
            session_service=session_service,
            auto_create_session=True
        )
        
        logger.info("Agent is ready. (In a real deployment, this would be wrapped in a server like FastAPI)")
        
        # Note: For real-time interaction, ADK usually runs a server.
        # This script serves as a programmatic entry point for testing/initialization.
        
    except Exception as e:
        logger.error(f"Failed to start agent: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    main()
