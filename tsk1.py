class Dog:
    """
    A class representing a dog.
    
    Attributes:
        name (str): The dog's name
    """
    
    def __init__(self, name: str) -> None:
        """
        Initializes a Dog object with the given name.
        
        Args:
            name (str): The dog's name
        """
        self.name = name
    
    def say(self) -> None:
        """
        Prints the sound that the dog makes.
        """
        print("Гав!")
