from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from qiskit.visualization import circuit_drawer
from qiskit.visualization import plot_histogram
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

M_simulator = Aer.get_backend('qasm_simulator')
S_simulator = Aer.get_backend('statevector_simulator')
q = QuantumRegister(4)
c = ClassicalRegister(1)
print("Balanced Oracle,alternating 1 and 0 in output")
for i in ("000", "001", "010", "011", "100", "101", "110", "111"):
    print("input:"+i+"\t")
    qc = QuantumCircuit(q, c)
    if i[2]=='1':
        qc.x(q[2])
    if i[1]=='1':
        qc.x(q[1]) 
    if i[0]=='1':
        qc.x(q[0])        
    qc.x(q[3])
    qc.cx(q[2],q[3])
    qc.measure(q[3],c[0])
    job = execute(qc, M_simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print("output:"+str(counts))
 
print("\nconstant 1 oracle")
for i in ("000", "001", "010", "011", "100", "101", "110", "111"):
    print("input:"+i+"\t")
    if i[2]=='1':
        qc.x(q[2])
    if i[1]=='1':
        qc.x(q[1]) 
    if i[0]=='1':
        qc.x(q[0])   
    qc = QuantumCircuit(q,c)
    qc.x(q[3])
    qc.measure(q[3],c[0])
    job = execute(qc, M_simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print("output:"+str(counts))

print("\nconstant 0 oracle")
for i in ("000", "001", "010", "011", "100", "101", "110", "111"):
    print("input:"+i+"\t")
    if i[2]=='1':
        qc.x(q[2])
    if i[1]=='1':
        qc.x(q[1]) 
    if i[0]=='1':
        qc.x(q[0])   
    qc = QuantumCircuit(q, c)
    qc.measure(q[3],c[0])
    job = execute(qc, M_simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)
    print("output:"+str(counts))  
        
