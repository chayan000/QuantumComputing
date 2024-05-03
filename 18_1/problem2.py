from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
import Our_Qiskit_Functions as oq
S_simulator=Aer.backends(name='statevector_simulator')[0]
q=QuantumRegister(4)
hello_qubit=QuantumCircuit(q)
hello_qubit.x(q[0])
hello_qubit.x(q[1])
hello_qubit.id(q[2])
hello_qubit.id(q[3])
print("rollno: 12310630")
oq.Wavefunction(hello_qubit)
