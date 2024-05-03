from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Balanced oracle
def quantum_oracle(f, n):
    print("passed to balanced Oracle")
    qc = QuantumCircuit(n + 1)
    qc.x(n)
    qc.cx(n-1,n)
    oracle_gate = qc.to_gate()
    oracle_gate.name = "balanced Oracle"
    #print(qc.draw())
    return oracle_gate
# Constant 1 oracle
def quantum_oracle1(f, n):
    print('passed to constant oracle 1')
    qc = QuantumCircuit(n + 1)
    qc.x(n)
    oracle_gate = qc.to_gate()
    oracle_gate.name = "const 1 Oracle"
    #print(qc.draw())
    return oracle_gate
#constant 0 oracle
def quantum_oracle0(f, n):
    print('passed to constant oracle 0')
    qc = QuantumCircuit(n + 1)
    oracle_gate = qc.to_gate()
    oracle_gate.name = "const 0 Oracle"
    #print(qc.draw())
    return oracle_gate

def deutsch_jozsa_algorithm(oracle, n):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)  
    qc.h(range(n + 1))  
    qc.append(oracle, range(n + 1))  
    qc.h(range(n))  
    #qc.measure(range(n), range(n))  
    return qc


def f(x):
    return 0 

n = 3
oracle = quantum_oracle(f, n)
qc = deutsch_jozsa_algorithm(oracle, n)
qc.measure(range(n), range(n))
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
result = backend.run(transpiled_qc).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())
if '000' in counts and counts['000'] == 1024:
    print("The function is constant.")   
else:
    print("The function is balanced.")


n = 3
oracle = quantum_oracle1(f, n)
qc = deutsch_jozsa_algorithm(oracle, n)
qc.measure(range(n), range(n))
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
result = backend.run(transpiled_qc).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())
if '000' in counts and counts['000'] == 1024:
    print("The function is constant.")  
else:
    print("The function is balanced.")


n = 3
oracle = quantum_oracle0(f, n)
qc = deutsch_jozsa_algorithm(oracle, n)
qc.measure(range(n), range(n))
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
result = backend.run(transpiled_qc).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())
if '000' in counts and counts['000'] == 1024:
    print("The function is constant.") 
else:
    print("The function is balanced.")
