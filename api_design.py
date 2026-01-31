import json
import sys

# The "Database" Row (Huge data)
user_db = {
    "id": 1,
    "username": "coder_hero",
    "email": "hero@gmail.com",
    "address": "123 Python Lane",
    "phone": "555-0199",
    "social_security": "SECRET-123", # Sensitive!
    "preferences": {"theme": "dark", "lang": "en"},
    "posts": ["Post 1", "Post 2", "Post 3"]
}

# --- 1. REST SIMULATION ---
def rest_get_user():
    # REST usually returns the WHOLE resource
    return user_db

# --- 2. GRAPHQL SIMULATION ---
def graphql_query(fields_requested):
    # GraphQL creates a custom dictionary with ONLY requested fields
    response = {}
    for field in fields_requested:
        if field in user_db:
            response[field] = user_db[field]
    return response

# --- COMPARISON ---
print("--- SCENARIO: Profile Widget (Only needs username & avatar) ---\n")

# REST Approach
rest_data = rest_get_user()
rest_size = sys.getsizeof(str(rest_data))
print(f"🌍 [REST] Response:\n{json.dumps(rest_data, indent=2)}")
print(f"❌ SIZE: {rest_size} bytes (Sent sensitive SSN and Address!)\n")

# GraphQL Approach
print("--- Switching to GraphQL ---")
query = ["username", "posts"] # We only ask for these
graphql_data = graphql_query(query)
graphql_size = sys.getsizeof(str(graphql_data))
print(f"🚀 [GraphQL] Response:\n{json.dumps(graphql_data, indent=2)}")
print(f"✅ SIZE: {graphql_size} bytes (Clean and Small)")
