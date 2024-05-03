from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]
for i in("00","01","10","11"):
    print("for state\t"+i)
    q=QuantumRegister(2)
    c=ClassicalRegister(2)
    qc=QuantumCircuit(q,c)
    if(i[0]=='0'):
        qc.x(q[1])
    if(i[1]=='0'):
        qc.x(q[0])   
    qc.h(q[0])
    qc.h(q[1])
    qc.cz(q[0],q[1])
    qc.h(q[0])
    qc.h(q[1])
    job=execute(qc,S_simulator)
    result=job.result()
    print(result.get_statevector())
    qc.measure_all()
    #M=execute(qc,M_simulator,shots=1000).result().get_counts(qc)
    #print(M)

    print(qc.draw())