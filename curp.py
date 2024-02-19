class Automaton:
    def __init__(self):
        self.states = [0, 1, 2, 3, 4]
        self.final_states = [1, 2, 3, 4]
        self.alphabet = ['G', 'U', 'A', 'D', 'g', 'u', 'a', 'd']
        self.transition_table = {
            (0, 'G'): 1, (0, 'g'): 1,
            (1, 'U'): 2, (1, 'u'): 2,
            (2, 'A'): 3, (2, 'a'): 3,
            (3, 'D'): 4, (3, 'd'): 4
        }
        self.current_state = 0

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) not in self.transition_table:
            self.current_state = None
        else:
            self.current_state = self.transition_table[(self.current_state, input_value)]

    def in_accept_state(self):
        return self.current_state in self.final_states

    def go_to_initial_state(self):
        self.current_state = 0

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            if self.current_state is None:
                return False
        return self.in_accept_state()

dfa = Automaton()

user_input = input("Inserte la cadenita: ")

is_valid = dfa.run_with_input_list(user_input)

if is_valid:
    print(f"La cadena '{user_input}' es correcto deacuerdo al DFA.")
else:
    print(f"La cadena '{user_input}' es incorrecta.")
    
# Curp/RFC con mis 4 iniciales  ->  GUAD
#Expresión regular              ->  ^[gG][uU]?[aA]?[dD]?$