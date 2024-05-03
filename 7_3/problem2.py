from qiskit import QuantumCircuit,transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
print("Quantum Method")
#balanced oracle
def quantum_oracle(f):
    qc = QuantumCircuit(2)
    qc.x(1)
    qc.cx(0, 1)  
    oracle_gate = qc.to_gate()
    oracle_gate.name = "balanced Oracle"
    return oracle_gate
#constant 0 oracle
def quantum_oracle0(f):
    qc = QuantumCircuit(2)
    oracle_gate = qc.to_gate()
    oracle_gate.name = "constant 0 Oracle"
    return oracle_gate
#constant 1 oracle
def quantum_oracle1(f):
    qc = QuantumCircuit(2)
    qc.x(1)  
    oracle_gate = qc.to_gate()
    oracle_gate.name = "constant 1 Oracle"
    return oracle_gate

def deutsch_algorithm(oracle):
    qc = QuantumCircuit(2, 1)
    qc.x(1)  
    qc.h(0)  
    qc.h(1)  
    qc.append(oracle, [0, 1])  
    qc.h(0)  
    #qc.measure(0, 0)  
    return qc


def f(x):
    return x  

oracle = quantum_oracle(f)
qc = deutsch_algorithm(oracle)
qc.measure(0, 0)  
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
result = backend.run(transpiled_qc).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())
if '0' in counts and counts['0'] == 1024:
    print("The function is constant.")
else:
    print("The function is balanced.")

oracle = quantum_oracle1(f)
qc = deutsch_algorithm(oracle)
qc.measure(0, 0)  
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
result = backend.run(transpiled_qc).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())
if '0' in counts and counts['0'] == 1024:
    print("The function is constant.")
else:
    print("The function is balanced.")

oracle = quantum_oracle0(f)
qc = deutsch_algorithm(oracle)
qc.measure(0, 0)  
backend = Aer.get_backend('qasm_simulator')
transpiled_qc = transpile(qc, backend)
result = backend.run(transpiled_qc).result()
counts = result.get_counts(qc)
print("Measurement result:", counts)
print(qc.draw())
if '0' in counts and counts['0'] == 1024:
    print("The function is constant.")
else:
    print("The function is balanced.")

print("Classicle method")
def balance(binary_string):
    return int(binary_string[-1])

def constant_0(binary_string):
    return 0

def constant_1(binary_string):
    return 1

functions = [(balance, "Balanced function"), (constant_0, "Constant 0 function"), (constant_1, "Constant 1 function")]

for func, func_name in functions:
    print("\nClassical", func_name, "\n")
    for binary_input in ["000", "001", "010", "011", "100", "101", "110", "111"]:
        print("input", binary_input, "output:", func(binary_input))
