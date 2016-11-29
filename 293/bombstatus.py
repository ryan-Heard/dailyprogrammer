
class BombSate:

    def __init__(self):
        self.state = None
        self.states = ['red', 'white', 'blue', 'black',
                       'green', 'orange', 'purple']

    def bomb_blows(self, wire_to_cut):
        if self.state is None:
            pass
        if self.state == 'white' and wire_to_cut in ['white', 'black']:
            return True
        elif self.state == 'red' and wire_to_cut not in ['green']:
            return True
        elif self.state == 'black' and wire_to_cut in ['green', 'black',
                                                       'orange']:
            return True
        elif self.state == 'orange' and wire_to_cut not in ['red', 'black']:
            return True
        elif self.state == 'green' and wire_to_cut not in ['orange', 'white']:
            return True
        elif self.state == 'purple' and wire_to_cut in ['purple', 'green',
                                                        'orange', 'white']:
            return True
        else:
            return False

    def check_input(self, input):
        if input not in self.states:
            print("That's not a cable")
            return False

    def cut_wires(self, wires):
        for wire in wires:
            if self.bomb_blows(wire):
                return True

            self.state = wire

        return False
