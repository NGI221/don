class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(c):
    return c in '+-*/'

def construct_expression_tree(prefix_expr):
    stack = []
    # Process prefix expression from right to left
    for symbol in reversed(prefix_expr):
        if not is_operator(symbol):
            stack.append(Node(symbol))
        else:
            node = Node(symbol)
            node.left = stack.pop()
            node.right = stack.pop()
            stack.append(node)
    return stack[-1] if stack else None

def post_order_non_recursive(root):
    if root is None:
        return []
    stack = []
    result = []
    current = root
    last_visited = None
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                result.append(peek_node.value)
                last_visited = stack.pop()
    return result

def delete_tree(root):
    # Post-order deletion: clear pointers explicitly
    if root is None:
        return
    delete_tree(root.left)
    delete_tree(root.right)
    root.left = None
    root.right = None
    root.value = None

# Interactive CLI
prefix_expr = input("Enter prefix expression (e.g., +--a*bc/def): ").strip()
root = construct_expression_tree(prefix_expr)

print("Non-recursive Post-order traversal:")
post_order = post_order_non_recursive(root)
print(" ".join(post_order))

delete_tree(root)
root = None
print("Expression tree deleted.")