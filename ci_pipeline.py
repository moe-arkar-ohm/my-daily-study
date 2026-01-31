import time

# --- THE CODEBASE ---
def add_numbers(a, b):
    return a + b  # <--- Try changing this to 'a - b' later to see it fail!

# --- THE TEST SUITE (CI) ---
def run_tests():
    print("🤖 [CI ROBOT] Running tests...")
    time.sleep(1) # Simulate checking
    
    # Test Case 1
    result = add_numbers(2, 3)
    if result != 5:
        print(f"   ❌ TEST FAILED: Expected 5, got {result}")
        return False # Fail
    
    print("   ✅ Test Passed: 2 + 3 = 5")
    return True # Pass

# --- THE DEPLOYMENT (CD) ---
def deploy_to_server():
    print("🚀 [CD ROBOT] Deploying to Production Server...")
    time.sleep(1)
    print("✨ SUCCESS: New version is live!")

# --- THE PIPELINE ---
def main_pipeline():
    print("--- STARTING PIPELINE ---")
    
    # Step 1: CI
    tests_passed = run_tests()
    
    if tests_passed:
        # Step 2: CD (Only if CI passed)
        deploy_to_server()
    else:
        print("🛑 [STOP] Deployment cancelled due to broken tests.")

main_pipeline()
