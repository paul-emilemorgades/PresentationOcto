import math 
import numpy as np 
from qiskit import QuantumCircuit, execute, Aer


def bellState():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0,1)
    return circuit

circuit = bellState()

#Lets verify the state vector
sim = Aer.get_backend('statevector_simulator')
job = execute(circuit, sim)
arr = job.result().get_statevector(circuit) 
b0 = (np.isclose(arr,[1/math.sqrt(2),0,0, 1/math.sqrt(2)]).all()) 
b1 = (np.isclose(arr,[0, 1/math.sqrt(2), 1/math.sqrt(2),0]).all() )
if(b0 or b1):
    print("It is a bell state! ")
#Lets execute our circuit
circuit.measure_all()
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1000)
result = job.result()
counts = result.get_counts(circuit) 
print(counts)

