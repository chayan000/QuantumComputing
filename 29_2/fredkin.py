from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

for i in ["000","001","010","011","100","101","110","111"]:
    q=QuantumRegister(3)
    c=ClassicalRegister(3)
    qc = QuantumCircuit(q, c)
    print("input:"+i+"\t")
    if(i[2]=='1'):
        qc.x(q[2])   
    if(i[1]=='1'):
        qc.x(q[1])   
    if(i[0]=='1'):
        qc.x(q[0])           
    qc.cswap(q[0],q[1],q[2])    
    qc.measure(q,c)
    M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
    print("output:"+"|"+list(M.keys())[0]+">")
    print("\n")
    
