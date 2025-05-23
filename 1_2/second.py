from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer

M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

q=QuantumRegister(3)
c=ClassicalRegister(3)
qc=QuantumCircuit(q,c)

qc.x(q[0])
qc.h(q[1])
qc.id(q[2])

S=execute(qc,S_simulator).result().get_statevector()
print(S)
qc.measure(q,c)
M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
print(M)
#S=execute(qc,S_simulator).result().get_statevector()
#print(S)
print(qc.draw())

