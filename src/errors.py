class Error(Exception):
    pass

class OutOfBoundsError(Error):
    """Raised if the user or machine places an object past the limits of the table"""
    pass

class PositionOccupiedError(Error):
    """Raised when a ship is placed in a position where there already is a boat"""
    pass