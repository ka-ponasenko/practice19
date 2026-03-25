class StrandsDNA:
    def __init__(self):
        """Initialize StrandsDNA object with empty list."""
        self.all_strands = []
    
    def add_strands(self, strands):
        """Add DNA strands to the collection.
        
        Args:
            strands: String containing DNA strands separated by spaces
        """
        self.all_strands.extend(strands.split())
    
    def __str__(self):
        """Return all strands as space-separated string."""
        return ' '.join(self.all_strands)
    
    def get_max_strands(self):
        """Get unique strands of maximum length in alphabetical order.
        
        Args:
            None
        
        Returns:
            String containing unique strands of maximum length,
            separated by spaces, sorted alphabetically
        """
        if not self.all_strands:
            return ""
        
        max_len = max(len(s) for s in self.all_strands)
        unique_strands = {s for s in self.all_strands if len(s) == max_len}
        
        return ' '.join(sorted(unique_strands))