class TrafficLight:
    """
    A traffic light class that cycles through signals in a specific order.
    
    The signals cycle in the following order:
    green -> yellow -> red -> yellow -> green -> ...
    """
    
    permissible_values: list[str] = ['зеленый', 'желтый', 'красный', 'желтый']

    
    def __init__(self) -> None:
        """
        Initialize the traffic light with the starting signal.
        
        The initial signal is set to 'зеленый' (green).
        """
        self.current_signal: str = 'зеленый'
        self.index: int = 0
    
    def next_signal(self) -> None:
        """
        Change the current signal to the next one in the cycle.
        
        The method updates the index to the next position in the
        permissible_values list (cycling back to the beginning when
        reaching the end) and sets current_signal to the corresponding value.
        """
        self.index = (self.index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self.index]

