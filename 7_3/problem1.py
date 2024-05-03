from qiskit import QuantumRegister,QuantumCircuit,Aer,execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

def u(qc):
    qc.h(q[0])
    qc.h(q[1])
    qc.z(q[0])
    qc.z(q[1])
    qc.cz(q[0],q[1])
    qc.h(q[0])
    qc.h(q[1])
    qc.measure(q,c)
    M=execute(qc,M_simulator,shots=100).result().get_counts(qc)
    print(M)
    print(qc.draw())
print("using entanglement")
#for generating -1/2|00> +1/2|01> +1/2|10> +1/2|11>
q=QuantumRegister(2)
c=ClassicalRegister(2)
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.cx(q[0],q[1])
qc.h(q[0])
qc.x(q[0])
qc.x(q[1])
print("state -1/2|00> +1/2|01> +1/2|10> +1/2|11> generated.passing to function u to get |00>")
qc.barrier()
job=execute(qc,S_simulator)
result=job.result()
print(result.get_statevector())
u(qc)



#for generating +1/2|00> +1/2|01> +1/2|10> -1/2|11>
q=QuantumRegister(2)
c=ClassicalRegister(2)
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.cx(q[0],q[1])
qc.h(q[0])
print("state +1/2|00> +1/2|01> +1/2|10> -1/2|11> generated..passing to function u to get |11>")
qc.barrier()
job=execute(qc,S_simulator)
result=job.result()
print(result.get_statevector())
u(qc)

#for generating +1/2|00> -1/2|01> +1/2|10> +1/2|11>
q=QuantumRegister(2)
c=ClassicalRegister(2)
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.cx(q[0],q[1])
qc.h(q[0])
qc.cx(q[0],q[1])
print("state +1/2|00> -1/2|01> +1/2|10> +1/2|11> generated..passing to function u to get |01>")
qc.barrier()
job=execute(qc,S_simulator)
result=job.result()
print(result.get_statevector())
u(qc)

#for generating +1/2|00> +1/2|01> -1/2|10> +1/2|11>
q=QuantumRegister(2)
c=ClassicalRegister(2)
qc=QuantumCircuit(q,c)
qc.h(q[0])
qc.cx(q[0],q[1])
qc.h(q[0])
qc.cx(q[1],q[0])
print("state +1/2|00> +1/2|01> -1/2|10> +1/2|11> generated..passing to function u to get |10>")
qc.barrier()
job=execute(qc,S_simulator)
result=job.result()
print(result.get_statevector())
u(qc)

print("Without entanglement\n")
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

