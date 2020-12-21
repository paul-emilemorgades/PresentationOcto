import math 
import numpy as np 
from qiskit import QuantumCircuit, execute, Aer

def AND():
    circuit = QuantumCircuit(3)
    circuit.ccx(0,1,2)
    circuit.swap(0,2)
    circuit.x(1)
    circuit.x(2)
    return circuit

circuit = AND()

#Lets verify the state vector, with |110> as input
yourCircuit = circuit.to_gate()
circuitForTest = QuantumCircuit(3)
circuitForTest.x(0)
circuitForTest.x(1)
circuitForTest.append(yourCircuit,[0,1,2])
sim = Aer.get_backend('statevector_simulator')
job = execute(circuitForTest, sim)
arr = job.result().get_statevector(circuitForTest) 
print(arr)
tab = [0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]
tab2 = [0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j]
tab3 = [0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j, 0.+0.j, 0.+0.j]
tab4 = [0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 1.+0.j]
if(np.isclose(arr,tab).all()  or np.isclose(arr,tab2).all() 
or np.isclose(arr,tab3).all() or np.isclose(arr,tab4).all()):
    print("\nBest 'AND' EU!\n")    



