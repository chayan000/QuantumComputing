from qiskit import QuantumCircuit,transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#Calculate the dot product of the results
def bdotz(secret, z):
    accum = 0
    for i in range(len(secret)):
        accum += int(secret[i]) * int(z[i])
    return (accum % 2)

# Oracle for simons algo
def simons_oracle(secret_string):
    n = len(secret_string)
    secret_string=secret_string[::-1]
    qc = QuantumCircuit(2*n)
    for i in range(n):
        qc.cx(i,n+i)
    for i in range(n):
        if secret_string[i] == '1':
            qc.cx(0, n+i)
    oracle_gate = qc.to_gate()
    oracle_gate.name = "Simons Oracle"
    print("diagram of the oracle:\n")
    print(qc.draw())
    return oracle_gate

#simons algorithm
def simons_algorithm(oracle, n):
    qc = QuantumCircuit(2*n, n) 
    qc.h(range(n))  
    qc.append(oracle, range(2*n))  
    qc.h(range(n))  
    qc.measure(range(n), range(n))  
    return qc

# Secret string
secret_string = input("enter secret string\t")
oracle = simons_oracle(secret_string)

n = len(secret_string)
qc = simons_algorithm(oracle, n)
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
qobj = assemble(transpiled_qc)
result = backend.run(qobj).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())
for z in counts:
    print( '{}.{}(mod 2) = {}'.format(secret_string, z, bdotz(secret_string,z)) )


