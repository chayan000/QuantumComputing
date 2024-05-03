from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer

M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name='statevector_simulator')[0]

# Function to apply CNOT gate
def apply_cnot(qc, q, inputstate):
    print("Input state:", inputstate)
    qc.cx(q[0], q[1])
    S = execute(qc, S_simulator).result().get_statevector()
    #print("CNOT gate output state vector:", S)

    qc.measure(q, c)
    M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
    print("CNOT gate output counts:", M)
    #print(qc.draw())

print("CNOT gate:\n")
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

# Apply CNOT gate for all possible inputs
for inputstate in ["00", "01", "10", "11"]:
    qc = QuantumCircuit(q, c)
    if inputstate[0] == "1":
        qc.x(q[0])
    if inputstate[1] == "1":
        qc.x(q[1])

    apply_cnot(qc, q, inputstate)

# Function to apply new design gate
def apply_new_design(qc, q, inputstate):
    print("Input state:", inputstate)
    if inputstate[0] == "1":
        qc.x(q[0])
    if inputstate[1] == "1":
        qc.x(q[1])

    qc.h(q[0])
    qc.h(q[1])
    qc.cx(q[0], q[1])
    qc.h(q[0])
    qc.h(q[1])
    S = execute(qc, S_simulator).result().get_statevector()
    #print("New design output state vector:", S)

    qc.measure(q, c)
    M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
    print("New design output counts:", M)
    print(qc.draw())

print("\nNew design:\n")

# Apply new design gate for all possible inputs
for inputstate in ["00", "01", "10", "11"]:
    qc = QuantumCircuit(q, c)
    apply_new_design(qc, q, inputstate)
