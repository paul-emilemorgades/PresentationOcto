import math
import numpy as np

#TOdo complex number change to dtype
#name of all variable
#lint test  



class QuantumGate:
    """
    Virtual class for quatum gates.
    
    Attribute:
        f_qubit (int): is the index of the first operand of the gate.
    """
    def __init__(self, f_qubit):
        self.f_qubit = f_qubit

    def create_matrix(self, nb_qubits):
        """
        Virtual function to create the corresponding matrix of a given gate.
        
        Args:
            nb_qubits (int): number of qubits in the circuit.
        """
        raise Exception("Not implement methods")

class OneOperandGate(QuantumGate):
    """
    Class for one operand gate.
    
    Atributes:
        f_matric (list of list of np.complex128): the corresponding matrix of 
        the gate.
    """
    def __init__(self, f_qubit, f_matric):
        super().__init__(f_qubit)
        self.f_matric = f_matric
    def create_matrix(self, nb_qubits):
        return compute_matrix(self.f_matric, nb_qubits, self.f_qubit)

class NotGate(OneOperandGate):
    """
    Class for not gate.
    """
    def __init__(self, f_qubit):
        super().__init__(f_qubit, np.array([[0, 1], [1, 0]]))

class HadamardGate(OneOperandGate):
    """
    Class for Hadamrd gate.
    """
    def __init__(self, f_qubit):
        inv_root = 1 / math.sqrt(2)
        super().__init__(f_qubit, np.array([[inv_root, inv_root],
             [inv_root, -inv_root]]))

class CNotGate(QuantumGate):
    """
    Class for cnot gate.
    
    Attributes:
        
        s_qubit (int): is the index of the seconf operand of the gate.
    """
    def __init__(self, f_qubit, s_qubit):
        super().__init__(f_qubit)
        self.s_qubit = s_qubit
        
    def create_matrix(self, nb_qubits):
        return compute_cnot(nb_qubits, self.f_qubit, self.s_qubit)


def quantum_computer(nb_qubits: int, quatum_gates: list):
    """
    Compute the state vector of a quantum computer according after executing 
    many quantum gates on it.
    
    Args:
        nb_qubits (int): is the number of Qbits of the circuit.
        quatum_gates (array of QuantumGate): each quantum gate that wil be
        executed on the quantum computer.
    
    Returns: 
        tab (array of numpy.complex128):
        
    """
    tab = np.zeros([2**nb_qubits])#, dtype = np.dtype(np.complex128))
    tab[0] = 1
    for i in quatum_gates:
        tab = np.matmul(i.create_matrix(nb_qubits), np.transpose(tab))
    return tab


def compute_matrix(base_matrix, nb_qbits, f_qubit):
    """
    Compute the correspnding matrix of a one operand gate.
    
    Args:
        base_matrix (numpy array): the corresponding matrix a gate.
        nb_qbits (int): the number of qubits in the circuit.
        f_qubit (int): the first operand of the gate.
        
    Returns: 
        res (array of array of complex numbers):  The correspnding matrix of a 
        one operand gate.
        
    """
    res = np.identity(1)
    for j in range(nb_qbits):
        i = nb_qbits - 1 - j
        if i == f_qubit:
            res = np.kron(res, base_matrix)
        else:
            res = np.kron(res, np.array([[1, 0], [0, 1]]))
    return res

def check(combinaison, card):
    """
    Check if the card^{th} bit if combinaison is to one
    
    Args:
        combinaison (int): the number from which the cardt^{th} bit will be
        checked.
        
        card (card): the cardinal of the bit of the number that will be checked
        
    Returns (bool): return if the card^{th} bit of combinaison is true 
    """
    combinaison = combinaison >> card
    return combinaison %2

def oppo(combinaison, card):
    """
    negate the card^{th} bit of combinaison 
    
    Args:
        combinaision (int): the number from which we will negate a number
        card (int): the card of the bit that will be negate
        
    Returns (bool): return the combinaison with his card^{th} bit negated/
    """
    mask = 1 << card
    return mask ^ combinaison

def compute_cnot(nb_qubits, f_qubit, s_qubit):
    """
    Compute the corresponding matrix of a cnot gate.
    
    Args:
        nb_qubits (int): number of qubits in the circuit.
        f_qubit (int): first operand of the cnot gate.
        s_qubit (int): second operand of the cnot gate.
    
    Returns:
        res (array of array of complex numbers): The corresponding matrix of the cnot gate.
    """
    size = 2**nb_qubits
    res = np.zeros([size, size])
    for combinaison in range(size):
        if check(combinaison, f_qubit):
            res[combinaison][oppo(combinaison, s_qubit)] = 1
        else:
            res[combinaison][combinaison] = 1
    return res

def compute_probability(tab):
    """
    Compute the probability of each possible output of a quantum computer
    from his state array.
    
    Parameters:
        tab (list of complex numbers): The quatum computer's state array.
    
    Returns:
        array_of_probabilities (list of floats): which is the probability of each possible output
        of the state array.

    """
    array_of_probabilities = [abs(i)**2 for i in tab]
    return array_of_probabilities/sum(array_of_probabilities)
