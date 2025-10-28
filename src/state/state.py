class State:
    def __init__(self, persistent_data = None):
        self.persistent_data = persistent_data
        
        self.next_state = None
        self.done = False

    def handle_event(self, event): 
        pass

    def update(self, dt): 
        pass

    def draw(self, screen): 
        pass