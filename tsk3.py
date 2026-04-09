class NotSleeping:
    """A class representing a person who cannot sleep and counts sheep."""
    
    def __init__(self, name: str, count_sheeps: int = 0) -> None:
        """Initialize a person with a name and initial sheep count.
        
        Args:
            name (str): The name of the person.
            count_sheeps (int, optional): Initial number of sheep counted. Defaults to 0.
        """
        self.name: str = name
        self.count_sheeps: int = count_sheeps
    
    def add_sheep(self) -> None:
        """Add one sheep to the count.
        
        Returns:
            None: This method does not return a value.
        """
        self.count_sheeps += 1
    
    def lost(self) -> None:
        """Reset the sheep count to zero when the person loses count.
        
        Returns:
            None: This method does not return a value.
        """
        self.count_sheeps = 0
    
    def get_count_sheeps(self) -> int:
        """Return the current number of sheep counted.
        
        Returns:
            int: The number of sheep counted.
        """
        return self.count_sheeps
