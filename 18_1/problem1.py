#rollno-12310630

from qiskit import QuantumRegister,QuantumCircuit,Aer,execute

S_simulator=Aer.backends(name='statevector_simulator')[0]
q=QuantumRegister(4)
hello_qubit=QuantumCircuit(q)
hello_qubit.x(q[0])
hello_qubit.x(q[1])
hello_qubit.id(q[2])
hello_qubit.id(q[3])
job=execute(hello_qubit,S_simulator)
result=job.result()
print("rollno: 12310630")
print(result.get_statevector())

