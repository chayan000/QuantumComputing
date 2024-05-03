from qiskit import QuantumRegister,QuantumCircuit,Aer,execute, ClassicalRegister

S_simulator=Aer.backends(name='qasm_simulator')[0]
q=QuantumRegister(2)
c=ClassicalRegister(2)
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.h(q[1])
qc.measure(q[0],c[0])
job=execute(qc,S_simulator)
result=job.result()
M=result.get_counts(qc)
print(M)

