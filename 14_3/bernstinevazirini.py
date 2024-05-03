from qiskit import QuantumCircuit,transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Balanced oracle for BV algo
def bernstein_vazirani_oracle(secret_string):
    n = len(secret_string)
    qc = QuantumCircuit(n + 1)
    qc.x(n)
    for i in range(n):
        if secret_string[i] == '1':
            qc.cx(i, n)
    oracle_gate = qc.to_gate()
    oracle_gate.name = "Oracle"
    print(qc.draw())
    return oracle_gate


def bernstein_vazirani_algorithm(oracle, n):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)  
    qc.h(range(n + 1))  
    qc.append(oracle, range(n + 1))  
    qc.h(range(n))  
    qc.measure(range(n), range(n))  
    return qc

# Secret string S of 4 bit
secret_string = input("enter 4 bit secret string\t")
oracle = bernstein_vazirani_oracle(secret_string)

n = len(secret_string)
qc = bernstein_vazirani_algorithm(oracle, n)
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
qobj = assemble(transpiled_qc)
result = backend.run(qobj).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())

secret_string = secret_string[::-1]
if secret_string in counts:
    print("The secret string is:", secret_string[::-1])
else:
    print("Could not identify the secret string.")
