from typing import List, Tuple

class Point:
    """A class representing a point on the coordinate plane."""
    
    def __init__(self, coordinates: Tuple[float, float]) -> None:
        """Initialize point with coordinates.
        
        Args:
            coordinates: Tuple (x, y) containing point coordinates
        """
        self.x: float = coordinates[0]
        self.y: float = coordinates[1]
    
    def __str__(self) -> str:
        """Return string representation of point.
        
        Returns:
            String in format (x; y)
        """
        return f"({self.x}; {self.y})"
    
    def __repr__(self) -> str:
        """Return unambiguous string representation for debugging."""
        return f"Point({self.x}, {self.y})"


class Segment:
    """A class representing a line segment between two points."""
    
    def __init__(self, point1: Point, point2: Point) -> None:
        """Initialize segment with two points.
        
        Args:
            point1: Point object - start point
            point2: Point object - end point
        """
        self.point1: Point = point1
        self.point2: Point = point2
    
    def __str__(self) -> str:
        """Return string representation of segment.
        
        Returns:
            String in format ((x1; y1), (x2; y2))
        """
        return f"({self.point1}, {self.point2})"
    
    def __repr__(self) -> str:
        """Return unambiguous string representation for debugging."""
        return f"Segment({repr(self.point1)}, {repr(self.point2)})"
    
    def one_intersection(self) -> bool:
        """Check if segment intersects exactly one coordinate axis.
        
        Returns:
            Boolean: True if segment intersects exactly one axis (X or Y),
                    False otherwise
        """
        x1: float = self.point1.x
        y1: float = self.point1.y
        x2: float = self.point2.x
        y2: float = self.point2.y
        
        crosses_x: bool = (y1 > 0 and y2 < 0) or (y1 < 0 and y2 > 0)
        
        crosses_y: bool = (x1 > 0 and x2 < 0) or (x1 < 0 and x2 > 0)
        
        return crosses_x ^ crosses_y


class CoordinateSystem:
    """A class representing a coordinate plane with segments."""
    
    def __init__(self) -> None:
        """Initialize empty coordinate system."""
        self.segments: List[Segment] = []
    
    def add_segment(self, segment: Segment) -> None:
        """Add a segment to the coordinate system.
        
        Args:
            segment: Segment object to add
        """
        self.segments.append(segment)
    
    def __str__(self) -> str:
        """Return string representation of all segments.
        
        Returns:
            String containing all segments in list format with proper formatting
        """
        formatted_segments: List[str] = [str(segment) for segment in self.segments]
        return "[" + ", ".join(formatted_segments) + "]"
    
    def __repr__(self) -> str:
        """Return unambiguous string representation for debugging."""
        return f"CoordinateSystem({repr(self.segments)})"
    
    def axis_intersection(self) -> int:
        """Count segments that intersect exactly one coordinate axis.
        
        Returns:
            Integer: Number of segments that intersect exactly one axis
        """
        count: int = 0
        for segment in self.segments:
            if segment.one_intersection():
                count += 1
        return count
