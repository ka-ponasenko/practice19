from typing import Optional, Any

class User:
    """A class representing a website user."""
    
    def __init__(self, id: int, nick_name: str, first_name: str, last_name: Optional[str] = None, middle_name: Optional[str] = None, gender: Optional[str] = None) -> None:
        """Initialize a user with required and optional attributes.
        
        Args:
            id (int): Unique user identifier.
            nick_name (str): User nickname.
            first_name (str): User first name.
            last_name (str, optional): User last name. Defaults to None.
            middle_name (str, optional): User middle name. Defaults to None.
            gender (str, optional): User gender. Defaults to None.
        """
        self.id: int = id
        self.nick_name: str = nick_name
        self.first_name: str = first_name
        self.last_name: Optional[str] = last_name
        self.middle_name: Optional[str] = middle_name
        self.gender: Optional[str] = gender
    
    def update(self, *args: Any) -> None:
        """Update user attributes. Empty strings are ignored.
        
        Args:
            *args: Variable number of arguments in order:
                   id, nick_name, first_name, last_name, middle_name, gender
        """
        values = [arg for arg in args if arg != '']
        match len(values):
            case 1:
                self.id = values[0]
            case 2:
                self.id, self.nick_name = values
            case 3:
                self.id, self.nick_name, self.first_name = values
            case 4:
                self.id, self.nick_name, self.first_name, self.last_name = values
            case 5:
                self.id, self.nick_name, self.first_name, self.last_name, self.middle_name = values
            case 6:
                self.id, self.nick_name, self.first_name, self.last_name, self.middle_name, self.gender = values
    
    def __str__(self) -> str:
        """Return string representation of the user.
        
        Returns:
            str: Formatted user information.
        """
        name_parts = [p for p in [self.last_name, self.first_name, self.middle_name] if p]
        result = f"ID: {self.id} LOGIN: {self.nick_name} NAME: {' '.join(name_parts)}"
        if self.gender:
            result += f" GENDER: {self.gender}"
        return result

    
        
