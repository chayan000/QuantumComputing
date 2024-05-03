#creating 3 qubit system
from qiskit import QuantumRegister,QuantumCircuit,Aer,execute

S_simulator=Aer.backends(name='statevector_simulator')[0]
q=QuantumRegister(3)
hello_qubit=QuantumCircuit(q)
hello_qubit.id(q[0])
hello_qubit.x(q[1])
hello_qubit.id(q[2])
job=execute(hello_qubit,S_simulator)
result=job.result()
print(result.get_statevector())

