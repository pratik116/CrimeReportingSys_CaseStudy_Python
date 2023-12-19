class SuspectNotFound(Exception):
    def __init__(self):
        super().__init__("SuspectNotFound")