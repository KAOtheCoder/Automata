from TuringMachine import TuringMachine
from TuringTransition import Transition

machine = TuringMachine("00011", 's')

machine.addRule(Transition('s', 'p', '0', 'X', 'R'))
machine.addRule(Transition('s', 'r', 'Y', 'Y', 'R'))
machine.addRule(Transition('p', 'p', '0', '0', 'R'))
machine.addRule(Transition('p', 'q', '1', 'Y', 'L'))
machine.addRule(Transition('p', 'p', 'Y', 'Y', 'R'))
machine.addRule(Transition('q', 'q', '0', '0', 'L'))
machine.addRule(Transition('q', 's', 'X', 'X', 'R'))
machine.addRule(Transition('q', 'q', 'Y', 'Y', 'L'))
machine.addRule(Transition('r', 'r', 'Y', 'Y', 'R'))
machine.addRule(Transition('r', 't', '#', '#', 'R'))

machine.setStartState('s')
machine.start("00011")