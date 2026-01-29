import sqlite3
import time
import random

# 1. Setup Database
conn = sqlite3.connect(':memory:') # Use RAM disk for fairness, or 'test.db' for disk
cursor = conn.cursor()
cursor.execute('CREATE TABLE numbers (val INTEGER)')

# 2. Insert 1 Million Rows (This takes a few seconds)
print("Inserting 1,000,000 rows... (Please wait)")
data = [(random.randint(1, 100000000),) for _ in range(1000000)]
cursor.executemany('INSERT INTO numbers VALUES (?)', data)
conn.commit()

# 3. Search WITHOUT Index
target = data[500000][0] # Pick a random number we know exists
print(f"Searching for {target}...")

start = time.time()
cursor.execute('SELECT * FROM numbers WHERE val=?', (target,))
result = cursor.fetchone()
end = time.time()
print(f"❌ Without Index: {end - start:.6f} seconds")

# 4. Create Index
print("Creating Index... (Organizing the B-Tree)")
start_index = time.time()
cursor.execute('CREATE INDEX idx_val ON numbers(val)')
conn.commit()
print(f"Index Built in: {time.time() - start_index:.4f} seconds")

# 5. Search WITH Index
start = time.time()
cursor.execute('SELECT * FROM numbers WHERE val=?', (target,))
result = cursor.fetchone()
end = time.time()
print(f"✅ With Index:    {end - start:.6f} seconds")

# Calculate Improvement
improvement = (0.1 / (end - start)) if (end-start) > 0 else 0
print("\nLook at the difference. That is the power of the B-Tree.")