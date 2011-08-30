##Example: {1 : 1} would denote row 1, column 1
##Example 2: {{1 : 1}
class piece():
    """initializing a piece class..."""
    def __init__(self, col, stat):
        self.color = col
        self.status = stat
    def get_color(self):
        print self.color
    def get_status(self):
        print self.status
    def set_color(self, new_color):
        self.color = new_color
    def set_status(self, new_status):
        self.status = new_status
        
