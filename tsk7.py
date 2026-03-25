class TrafficLight:
    """
    A traffic light class that cycles through signals in a specific order.
    
    The signals cycle in the following order:
    green -> yellow -> red -> yellow -> green -> ...
    """
    
    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']

    
    def __init__(self):
        """
        Initialize the traffic light with the starting signal.
        
        The initial signal is set to 'зеленый' (green).
        """
        self.current_signal = 'зеленый'
        self.index = 0
    
    def next_signal(self):
        """
        Change the current signal to the next one in the cycle.
        
        The method updates the index to the next position in the
        permissible_values list (cycling back to the beginning when
        reaching the end) and sets current_signal to the corresponding value.
        """
        self.index = (self.index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self.index]

