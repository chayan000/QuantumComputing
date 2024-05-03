from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

q=QuantumRegister(4)
c=ClassicalRegister(2)
qc=QuantumCircuit(q,c)
for i in ["00","01","10","11"]:
    qc=QuantumCircuit(q,c)
    if(i[0]=="1"):
        qc.x(q[0])
    if(i[1]=="1"):
        qc.x(q[1])    
    print(i)    
    qc.ccx(q[0],q[1],q[2])
    qc.x(q[3])
    qc.ccx(q[0],q[3],q[1])
    qc.measure(q[1],c[0])
    qc.measure(q[2],c[1])
    M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
    print("the Lsb is the sum(xor) and the Msb is the carry(and)")
    print(M)
    print(qc.draw())