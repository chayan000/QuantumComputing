from qiskit import QuantumRegister,ClassicalRegister,QuantumCircuit,execute,Aer
import Our_Qiskit_Functions as oq
S_simulator = Aer.backends(name='statevector_simulator')[0]
q=QuantumRegister(2)
hello=QuantumCircuit(q)
hello.h(q[0])
hello.h(q[1])

#job=execute(hello,S_simulator)
#result=job.result()
#print(result.get_statevector())

oq.Wavefunction(hello)
