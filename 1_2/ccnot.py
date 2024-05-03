from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

q=QuantumRegister(3)
c=ClassicalRegister(3)
qc=QuantumCircuit(q,c)

qc.h(q[0])
qc.x(q[1])
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print("before ccnot")
print(M)
qc.ccx(q[0],q[1],q[2])
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print("after ccnot")
print(M)
print(qc.draw())