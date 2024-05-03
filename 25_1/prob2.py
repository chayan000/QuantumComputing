from qiskit import QuantumRegister,QuantumCircuit,Aer,execute, ClassicalRegister
S_simulator=Aer.backends(name='qasm_simulator')[0]
q=QuantumRegister(1)
c=ClassicalRegister(1)
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.measure(q,c)
job=execute(qc,S_simulator)
result=job.result()
M=result.get_counts(qc)
out=list(M.keys())[0]
if(out=="1"):
    print("it's head")
if(out=="0"):
    print("it's tail")    

