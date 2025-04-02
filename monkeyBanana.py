class State:
    def __init__(self, monkey, box, banana):
        self.monkey = monkey  # Position of the monkey (A, B, or C)
        self.box = box        # Position of the box (A, B, or C)
        self.banana = banana  # Position of the banana (A, B, or C)

    def __str__(self):
        return f"Monkey: {self.monkey}, Box: {self.box}, Banana: {self.banana}"

def move_monkey(state, new_position):
    return State(new_position, state.box, state.banana)

def push_box(state, new_position):
    if state.monkey == state.box:
        return State(new_position, new_position, state.banana)
    return state

def climb_box(state):
    if state.monkey == state.box and state.monkey == state.banana:
        return State(state.monkey, state.box, True)
    return state

def grab_banana(state):
    if state.monkey == state.box == state.banana:
        print("Banana grabbed!")
        return State(state.monkey, state.box, True)
    return state

def monkey_banana_problem():
    initial_state = State("A", "C", "B")
    print("Initial State:", initial_state)

    # Step 1: Move Monkey to Box
    state = move_monkey(initial_state, "C")
    print("After moving the monkey to the box:", state)

    # Step 2: Push Box to Banana
    state = push_box(state, "B")
    print("After pushing the box to the banana:", state)

    # Step 3: Climb Box to Grab Banana
    state = climb_box(state)
    print("After climbing the box:", state)

    # Step 4: Grab Banana
    state = grab_banana(state)

if __name__ == "__main__":
    monkey_banana_problem()
