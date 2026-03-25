class Point:
    """A class representing a point on the coordinate plane."""
    
    def __init__(self, coordinates):
        """Initialize point with coordinates.
        
        Args:
            coordinates: Tuple (x, y) containing point coordinates
        """
        self.x = coordinates[0]
        self.y = coordinates[1]
    
    def __str__(self):
        """Return string representation of point.
        
        Returns:
            String in format (x; y)
        """
        return f"({self.x}; {self.y})"
    
    def __repr__(self):
        """Return string representation for debugging."""
        return str(self)


class Segment:
    """A class representing a line segment between two points."""
    
    def __init__(self, point1, point2):
        """Initialize segment with two points.
        
        Args:
            point1: Point object - start point
            point2: Point object - end point
        """
        self.point1 = point1
        self.point2 = point2
    
    def __str__(self):
        """Return string representation of segment.
        
        Returns:
            String in format ((x1; y1), (x2; y2))
        """
        return f"({self.point1}, {self.point2})"
    
    def __repr__(self):
        """Return string representation for debugging."""
        return str(self)
    
    def one_intersection(self):
        """Check if segment intersects exactly one coordinate axis.
        
        Returns:
            Boolean: True if segment intersects exactly one axis (X or Y),
                    False otherwise
        """
        x1, y1 = self.point1.x, self.point1.y
        x2, y2 = self.point2.x, self.point2.y
        
        crosses_x = (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0)
        
        crosses_y = (x1 > 0 and x2 < 0) or (x1 < 0 and x2 > 0)
        
        return crosses_x ^ crosses_y


class CoordinateSystem:
    """A class representing a coordinate plane with segments."""
    
    def __init__(self):
        """Initialize empty coordinate system."""
        self.segments = []
    
    def add_segment(self, segment):
        """Add a segment to the coordinate system.
        
        Args:
            segment: Segment object to add
        """
        self.segments.append(segment)
    
    def __str__(self):
        """Return string representation of all segments.
        
        Returns:
            String containing all segments in list format with proper formatting
        """
        formatted_segments = [str(segment) for segment in self.segments]
        return "[" + ", ".join(formatted_segments) + "]"
    
    def axis_intersection(self):
        """Count segments that intersect exactly one coordinate axis.
        
        Returns:
            Integer: Number of segments that intersect exactly one axis
        """
        count = 0
        for segment in self.segments:
            if segment.one_intersection():
                count += 1
        return count