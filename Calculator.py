class Calculator:
    current_value = 0
    def add(self, value):
        self.current_value += value
    def subtract(self, value):
        self.current_value -= value
    def multiply(self, value):
        self.current_value *= value
    def divide(self, value):
        self.current_value /= value
    def get_current(self):
        return self.current_value

