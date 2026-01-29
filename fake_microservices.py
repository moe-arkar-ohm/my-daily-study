import time

# --- SERVICE A (The Math Service) ---
# In real life, this would be running on a different server (e.g., Port 8001)
def microservice_math_add(x, y):
    print(f"[Service A] Received request: {x} + {y}")
    time.sleep(0.5) # Simulate Network Latency
    if x < 0 or y < 0:
        raise ValueError("Negative numbers not allowed in Service A")
    return x + y

# --- SERVICE B (The Main App) ---
# In real life, this is your frontend or main API
def main_app():
    print("[Service B] I need to calculate 10 + 20.")
    print("[Service B] Calling Service A over the network...")
    
    try:
        # NETWORK CALL
        result = microservice_math_add(10, 20)
        print(f"[Service B] Got result: {result}")
        
        print("\n[Service B] Now trying -5 + 10...")
        result = microservice_math_add(-5, 10)
    
    except Exception as e:
        print(f"[Service B] NETWORK ERROR or REMOTE EXCEPTION: {e}")

main_app()