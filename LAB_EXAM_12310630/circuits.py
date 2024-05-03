from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

q=QuantumRegister(2)
c=ClassicalRegister(2)


#1st
print("circuit for 00+11")
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.cx(q[0],q[1])
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print(M)
print(qc.draw())
#2nd
print("circuit for 01+10")
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.x(q[1])
qc.cx(q[0],q[1])
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print(M)
print(qc.draw())
#3rd
print("circuit for 00-11")
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.cz(q[0],q[1])
qc.cx(q[0],q[1])
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print(M)
print(qc.draw())
#4th
print("circuit for 01-10")
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.x(q[1])
qc.cx(q[0],q[1])
qc.cz(q[1],q[0])
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print(M)
print(qc.draw())
#5th
print("circuit of last question")
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.h(q[1])
qc.cx(q[0],q[1])
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print(M)
print(qc.draw())
