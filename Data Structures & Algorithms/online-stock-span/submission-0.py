class StockSpanner:

    def __init__(self):
        # Stack stores pairs of [price, span]
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Merge all previous days whose price is less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
            
        # Push the current price along with its total accumulated span
        self.stack.append((price, span))
        
        return span