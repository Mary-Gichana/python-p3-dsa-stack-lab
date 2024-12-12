class Stack:
    def __init__(self, items=None, limit=100):
        # Initialize items to an empty list if None is provided
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack if it is not full."""
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            # Allow tests to expect silent acceptance if limit exceeded
            pass

    def pop(self):
        """Remove and return the top item from the stack."""
        if not self.isEmpty():
            return self.items.pop()
        else:
            # The test expects None when popping from an empty stack
            return None

    def peek(self):
        """Return the top item without removing it."""
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None  # Allow peek to return None for an empty stack

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def full(self):
        """Check if the stack is full."""
        return len(self.items) >= self.limit

    def search(self, target):

      try:
        return self.items[::-1].index(target)  # 0-based index from the top
      except ValueError:
        return -1  # Target not found


