class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_recursive(node, target):
    # 1. Base Case: The "Stop Sign" (End of the line)
    if node is None:
        return False # We hit the bottom, didn't find it
    
    # 2. Base Case: We found it!
    if node.value == target:
        return True
    
    # 3. Recursive Step: Decide where to go
    if target < node.value:
        print(f"Checking {node.value}... Too big. Going Left.")
        # TODO: Call search_recursive on the LEFT child
        return search_recursive(node.left, target)
    else:
        print(f"Checking {node.value}... Too small. Going Right.")
        # TODO: Call search_recursive on the RIGHT child
        return search_recursive(node.right, target)

# --- Setup the Tree ---
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
# Let's add one more layer manually for the test
root.right.right = TreeNode(30) # 10 -> 20 -> 30

# --- The Test ---
print("--- Looking for 30 ---")
found = search_recursive(root, 30)
print(f"Result: {found}")

print("\n--- Looking for 99 ---")
found = search_recursive(root, 99)
print(f"Result: {found}")
