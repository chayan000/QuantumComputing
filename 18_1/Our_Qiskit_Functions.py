# Our Qiskit Functions.py
import numpy as np
from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
S_simulator=Aer.backends(name='statevector_simulator')[0]

def Wavefunction(qubit_state):
    job=execute(qubit_state,S_simulator)
    result=job.result()
    stv=result.get_statevector()
    
    for i in range(len(stv)):
        magnitude=np.absolute(stv[i])
        if magnitude>0:
            print(magnitude,end=" |")
            print(format(i,'b').zfill(len(qubit_state.qubits))[::-1],end=">")
            print("\n")

