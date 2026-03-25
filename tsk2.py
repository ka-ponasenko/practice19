class NotSleeping:
    """A class representing a person who cannot sleep and counts sheep."""
    
    def __init__(self, name, count_sheeps=0): 
        """Initialize a person with a name and initial sheep count.
        
        Args:
            name (str): The name of the person.
            count_sheeps (int, optional): Initial number of sheep counted. Defaults to 0.
        """
        self.name = name
        self.count_sheeps = count_sheeps 
    
    def add_sheep(self):
        """Add one sheep to the count.
        
        Returns:
            None: This method does not return a value.
        """
        self.count_sheeps += 1 





