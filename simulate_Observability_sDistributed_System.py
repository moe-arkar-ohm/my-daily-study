import logging
import uuid
import json
import contextvars
import time

# 1. The "Trace ID" Storage (This represents the 'Request Context')
correlation_id = contextvars.ContextVar("correlation_id", default="N/A")

# 2. Guru-Level Structured Logger
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": time.ctime(),
            "level": record.levelname,
            "message": record.getMessage(),
            "trace_id": correlation_id.get(),  # We inject the ID into every log automatically
            "module": record.module
        }
        return json.dumps(log_record)

logger = logging.getLogger("GuruLogger")
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# --- THE MOCK SYSTEM ---

def database_save():
    # Simulation of a DB operation
    logger.info("Saving record to Database...")
    time.sleep(0.1)
    logger.info("Database save successful.")

def logic_engine():
    # Simulation of business logic
    logger.info("Processing business logic...")
    database_save()

def handle_request(user_request):
    # Every time a request starts, we generate a NEW unique ID
    token = correlation_id.set(str(uuid.uuid4())) 
    
    logger.info(f"Received request: {user_request}")
    try:
        logic_engine()
    finally:
        # Clean up after request is done
        correlation_id.reset(token)

# --- RUNNING THE SIMULATION ---
print("--- STARTING REQUEST 1 ---")
handle_request("Place Bet #101")

print("\n--- STARTING REQUEST 2 ---")
handle_request("Withdrawal #999")
