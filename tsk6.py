class Point:
    """A class representing a point on a 2D plane."""
    
    def __init__(self, coordinates=None):
        """
        Initialize a point with given coordinates.
        
        Args:
            coordinates (tuple, optional): A tuple (x, y) representing the point's coordinates.
                Defaults to None, which sets the point at the origin (0, 0).
        """
        if coordinates is None:
            self.x = 0
            self.y = 0
        else:
            self.x = coordinates[0]
            self.y = coordinates[1]

    
    def get_x(self):
        """
        Get the x-coordinate of the point.
        
        Returns:
            int or float: The x-coordinate value
        """
        return self.x


    def get_y(self):
        """
        Get the y-coordinate of the point.
        
        Returns:
            int or float: The y-coordinate value
        """
        return self.y
    

    def distance(self, other):
        """
        Calculate the Euclidean distance between this point and another point.
        
        Args:
            other (Point): Another point object
            
        Returns:
            float: The Euclidean distance between the two points
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    

    def sum(self, other):
        """
        Create a new point whose coordinates are the sum of this point and another point.
        
        Args:
            other (Point): Another point object
            
        Returns:
            Point: A new point with coordinates (self.x + other.x, self.y + other.y)
        """
        return Point((self.x + other.x, self.y + other.y))
    

    def __str__(self):
        """
        Return a string representation of the point.
        
        Returns:
            str: A string in the format "(x, y)"
        """
        return f"({self.x}, {self.y})"