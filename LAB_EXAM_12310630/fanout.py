from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

q=QuantumRegister(3)
c=ClassicalRegister(1)
qc=QuantumCircuit(q,c)

for i in ["0","1"]:
    if(i[0]=="1"):
        qc.x(q[1])
    print("value to be fanout "+i)
    qc.ccx(q[0],q[1],q[2])
    qc.measure(q[1],c)
    M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
    print("after fanout")
    print(M)
    print(qc.draw())