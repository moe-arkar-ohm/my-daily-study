import sys
import structlog
import uuid

# 1. Configure the "Guru" Logger (JSON Output)
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer() # <--- The Magic. Turns logs into Data.
    ],
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
)

log = structlog.get_logger()

# 2. Simulate a Web Request (Middleware Style)
def simulate_request(user_id, action):
    # A. Generate the Correlation ID (The Red String)
    request_id = str(uuid.uuid4())
    
    # B. Bind it. All logs in this function now have this ID.
    request_log = log.bind(request_id=request_id, user_id=user_id)
    
    request_log.info("request_started", path="/buy", method="POST")
    
    # Simulate DB Call
    try:
        if action == "fail":
            raise ValueError("Database Connection Timeout")
        
        request_log.info("payment_processed", amount=5000, currency="MMK")
        request_log.info("request_finished", status=200)
        
    except Exception as e:
        # Guru Trick: Logging the exception object properly
        request_log.error("request_crashed", error=str(e), status=500)

# --- RUN IT ---
print("--- Request 1: Success ---")
simulate_request("user_admin", "success")

print("\n--- Request 2: Failure ---")
simulate_request("user_junior", "fail")
