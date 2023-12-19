class VictimNotFound(Exception):
    def __init__(self):
        super().__init__("VictimNotFound")