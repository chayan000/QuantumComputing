from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]
print("OR using fredkin\n")
print("output is in the middle qubit\n")
for i in ["00","01","10","11"]:
    q=QuantumRegister(3)
    c=ClassicalRegister(3)
    qc = QuantumCircuit(q, c)
    qc.x(q[2])
    print("input:"+i+"\t")  
    if(i[1]=='1'):
        qc.x(q[1])   
    if(i[0]=='1'):
        qc.x(q[0])           
    qc.cswap(q[0],q[1],q[2])    
    qc.measure(q,c)
    M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
    print("output:"+"|"+list(M.keys())[0]+">")
    print("\n")
    
